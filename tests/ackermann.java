class Debug{
    int ackermann(int m,int n) {
        int i = -1, j = -1;
        if (m>-1 && n>-1) {
            if (m == 0) {
                i = n + 1;
            }
            else if (n == 0) {
                i = ackermann(m - 1, 1);
            }
            else {
                j = ackermann(m, n - 1);
                i = ackermann(m - 1, j);
            }
        }
        return i;
    }
    int main(){
        int x = ackermann(3,1);
        System.out.println(x);
    }
}