class ifib{

    int ifib (int n) {
        int f1 = 0;
        int f2 = 1;
        int fn;
        if (n==0) {
            fn = 0;
        }
        else if (n==1) {
            fn = 1;
        }
        for (int i = 1; i<n ; i++) {
            fn = f1 + f2;
            f1 = f2;
            f2 = fn;
        }
        return fn;
    }
    int main() {
        float a = 6.5;

    }
}
