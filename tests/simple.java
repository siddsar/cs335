// class ackermann{
//     // int Ack(int m,int n) {
//     //     int i = -1, j = -1;
//     //     if (m>=0 && n>=0) {
//     //         if (m == 0) {
//     //             i = n + 1;
//     //         } else if (n == 0) {
//     //             i = Ack(m - 1, 1);
//     //         } else {
//     //             j = Ack(m, n - 1);
//     //             i = Ack(m - 1, j);
//     //         }
//     //     }
//     //     return i;
//     // }
//     int main(){
//         // int i = Ack(3,4);
//         // System.out.println(i);
//         // int m = -1;
//         // int n = -1;
//         // int i=0;
//         // int j=0;
//         // if (m>=0 && n>=0) {
//         //     if (m == 0) {
//         //         i = n + 1;
//         //     } else if (n == 0) {
//         //         // /i = Ack(m - 1, 1);
//         //     	i=4;
//         //     } else {
//         //     	j=4;
//         //         // j = Ack(m, n - 1);
//         //         // i = Ack(m - 1, j);
//         //     }
//         // }
//     	int[][] arr = new int[8][5];
//         arr[0][3] = 2;
//         arr[1][4] = 5;

//     }
// }
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
        for (int i=1;i<n;i++) {
            fn = f1 + f2;
            f1 = f2;
            f2 = fn;
        }
        return fn;
    }
    int main() {
        System.out.println(ifib(0));
     	System.out.println(ifib(1));
        System.out.println(ifib(2));
        System.out.println(ifib(3));
        System.out.println(ifib(4));
        System.out.println(ifib(5));
        System.out.println(ifib(6));
        System.out.println(ifib(7));
    }
}
