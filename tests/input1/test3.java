import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.util.Arrays;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.math.BigInteger;
import java.io.BufferedReader;
import java.util.Collections;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        public void solve(int testNumber, FastScanner in, PrintWriter out) {
            int n = in.nextInt();
            long k = in.nextLong();
            Judge[] judges = new Judge[n];
            long g = 0;
            for (int i = 0; i < n; i++) {
                judges[i] = new Judge();
                judges[i].a = in.nextLong();
                g = gcd(g, judges[i].a);
            }
            for (int i = 0; i < n; i++) {
                judges[i].e = in.nextInt();
            }

            Factor[] factors = factorize(g);

            for (int i = 0; i < n; i++) {
                long na = 1;
                // Remove the prime factors that do not occur in the gcd
                // by leaving only those that do.
                for (Factor f : factors) {
                    while (judges[i].a % f.p == 0) {
                        judges[i].a /= f.p;
                        na *= f.p;
                    }
                }
                judges[i].a = na;
            }
            Arrays.sort(judges);

//        if (true) {
            if (false) {
                countEquivalenceClassesWorstCase();
            }

            int m = factors.length;
            {
                List<Judge> bestJudges = new ArrayList<>();
                for (int i = 0; i < n; ) {
                    int j = i;
                    while (j < n && judges[i].a == judges[j].a) {
                        ++j;
                    }

                    // At most |m| judges in every equivalence class are needed.
                    for (int it = i; it < j && it < i + m; it++) {
                        bestJudges.add(judges[it]);
                    }
                    i = j;
                }
                judges = bestJudges.toArray(new Judge[0]);
                n = judges.length;
                for (int i = 0; i < n; i++) {
                    judges[i].sortedId = i;
                }
            }

            long[] prod = new long[1 << m];
            long[] factorRaisedToPow = new long[m];
            List<Judge>[] judgesThatCanCoverMask = new List[1 << m];
            for (int mask = 0; mask < 1 << m; mask++) {
                judgesThatCanCoverMask[mask] = new ArrayList<>();
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    Factor f = factors[j];
                    long x = judges[i].a;
                    long y = 1;
                    while (x % f.p == 0) {
                        x /= f.p;
                        y *= f.p;
                    }
                    factorRaisedToPow[j] = y;
                }
                prod[0] = 1;
                for (int mask = 1; mask < 1 << m; mask++) {
                    int j = Integer.numberOfTrailingZeros(mask);
                    prod[mask] = prod[mask ^ (1 << j)] * factorRaisedToPow[j];
                    if (prod[mask] <= k) {
                        judgesThatCanCoverMask[mask].add(judges[i]);
                    }
                }
            }

            List<Integer>[] masksCoveredByJudge = new List[n];
            for (int mask = 0; mask < 1 << m; mask++) {
                List<Judge> js = judgesThatCanCoverMask[mask];
                Collections.sort(js, (u, v) -> Integer.compare(u.e, v.e));

                // By the exchange argument, only |m| best judges
                // that can cover this mask are needed.
                for (int it = 0; it < m && it < js.size(); it++) {
                    int id = js.get(it).sortedId;
                    if (masksCoveredByJudge[id] == null) {
                        masksCoveredByJudge[id] = new ArrayList<>();
                    }
                    masksCoveredByJudge[id].add(mask);
                }
            }

            final long infinity = Long.MAX_VALUE / 2;
            long[][] d = new long[m + 1][1 << m];
            for (long[] arr : d) {
                Arrays.fill(arr, infinity);
            }
            d[0][0] = 0;
            for (int judgeId = 0; judgeId < n; judgeId++) {
                if (masksCoveredByJudge[judgeId] == null) {
                    continue;
                }
                for (int used = m - 1; used >= 0; used--) {
                    // At most m*(1<<m) masks are in total in all the |masksCoveredByJudge| lists combined.
                    // Every mask occurs at most m times (so we cannot have, say, the worst mask occur too often).
                    // Therefore, the overall complexity of these nested 4 for loops is O(m^3 * 3^m).
                    for (int mask : masksCoveredByJudge[judgeId]) {
                        int other = ((1 << m) - 1) ^ mask;
                        for (int covered = other; ; covered = (covered - 1) & other) {
                            if (d[used + 1][covered | mask] > d[used][covered] + judges[judgeId].e) {
                                d[used + 1][covered | mask] = d[used][covered] + judges[judgeId].e;
                            }
                            if (covered == 0) {
                                break;
                            }
                        }
                    }
                }
            }

            long ans = infinity;
            for (int x = 0; x <= m; x++) {
                long y = d[x][(1 << m) - 1];
                if (y < infinity) {
                    ans = Math.min(ans, x * y);
                }
            }
            if (ans >= infinity) {
                ans = -1;
            }
            out.println(ans);
        }

        private void countEquivalenceClassesWorstCase() {
            final long LIMIT = (long) 1e12;
            final int N = 100;
            boolean[] isPrime = new boolean[N];
            Arrays.fill(isPrime, true);
            int[] primes = new int[N];
            int numPrimes = 0;
            BigInteger prod = BigInteger.ONE;
            for (int i = 2; i < N; i++) {
                if (!isPrime[i]) {
                    continue;
                }
                primes[numPrimes++] = i;
                prod = prod.multiply(BigInteger.valueOf(i));
                if (prod.compareTo(BigInteger.valueOf(LIMIT)) > 0) {
                    break;
                }
                for (int j = i + i; j < N; j += i) {
                    isPrime[j] = false;
                }
            }
            System.out.printf("Product of the first %d primes exceeds the limit of %d\n", numPrimes, LIMIT);
            primes = Arrays.copyOf(primes, numPrimes - 1);
            System.out.printf("Number of equivalence classes when using only the first several primes:\n");
            System.out.printf("num primes: num classes\n");
            for (int i = 1; i <= primes.length; i++) {
                System.out.printf("%d: %d\n", i, rec(0, 1, LIMIT, Arrays.copyOf(primes, i)));
            }
        }

        private long rec(int pos, long prod, long limit, int[] primes) {
            if (pos == primes.length) {
                return prod <= limit ? 1 : 0;
            }
            long res = 0;
            while (prod <= limit / primes[pos]) {
                prod *= primes[pos];
                // Every prime must occur at least once.
                res += rec(pos + 1, prod, limit, primes);
            }
            return res;
        }

        private long gcd(long a, long b) {
            return b == 0 ? a : gcd(b, a % b);
        }

        private Factor[] factorize(long n) {
            List<Factor> res = new ArrayList<>();
            for (long p = 2; p * p <= n; p++) {
                if (n % p == 0) {
                    Factor f = new Factor();
                    f.p = p;
                    while (n % p == 0) {
                        n /= p;
                        ++f.s;
                    }
                    res.add(f);
                }
            }
            if (n > 1) {
                Factor f = new Factor();
                f.p = n;
                f.s = 1;
                res.add(f);
            }
            return res.toArray(new Factor[0]);
        }

        class Judge implements Comparable<Judge> {
            long a;
            int e;
            int sortedId;

            public int compareTo(Judge o) {
                if (a != o.a) {
                    return a < o.a ? -1 : 1;
                }
                if (e != o.e) {
                    return e < o.e ? -1 : 1;
                }
                return 0;
            }

        }

        class Factor {
            long p;
            int s;

        }

    }

    static class FastScanner {
        private BufferedReader in;
        private StringTokenizer st;

        public FastScanner(InputStream stream) {
            in = new BufferedReader(new InputStreamReader(stream));
        }

        public String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(in.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

    }
}
