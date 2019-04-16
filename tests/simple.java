class Debug{
    int ackermann(int m,int n) {
        int i = -1, j = -1;
        System.out.println(m);
        System.out.println(n);
        if (m>-1 && n>-1) {
        	System.out.println(m);
        	System.out.println(n);
            if (m == 0) {
                i = n + 1;
            } else if (n == 0) {
                i = ackermann(m - 1, 1);
            } else {
                j = ackermann(m, n - 1);
                i = ackermann(m - 1, j);
            }
        }
        return i;
    }
    int main(){
    	// int m=1;
    	// int n=2;
    	// int i = -1, j = -1;
     //    System.out.println(m);
     //    System.out.println(n);
     //    if (m>0 && n>0) {
     //    	System.out.println(m);
     //    	System.out.println(n);
     //        if (m == 0) {
     //            i = n + 1;
     //        } else if (n == 0) {
     //            i = Ack(m - 1, 1);
     //        } else {
     //            j = Ack(m, n - 1);
     //            i = Ack(m - 1, j);
     //        }
     //    }
        int i = ackermann(4,1);
        // // int i = 5;
        System.out.println(i);
        // int x = i>4 && i>1;

        // int m = -1;
        // int n = -1;
        // int i=0;
        // int j=0;
        // if (m>=0 && n>=0) {
        //     if (m == 0) {
        //         i = n + 1;
        //     } else if (n == 0) {
        //         // /i = Ack(m - 1, 1);
        //     	i=4;
        //     } else {
        //     	j=4;
        //         // j = Ack(m, n - 1);
        //         // i = Ack(m - 1, j);
        //     }
        // }
    	// int[][] arr = new int[8][5];
     //    arr[0][3] = 2;
     //    arr[1][4] = 5;
    }

}


// public class MyBinarySearch {

//     public int binarySearch(int inputArr, int len, int key) {
//         int start = 0,
//         int mid;
//         int end = len - 1;
//         // while (start <= end) {
//         // 	System.out.println(3);
//         //     // mid = (start + end) / 2;
//         //     // if (key == inputArr[mid]) {
//         //     //     return mid;
//         //     // }
//         //     // if (key < inputArr[mid]) {
//         //     //     end = mid - 1;
//         //     // } else {
//         //     //     start = mid + 1;
//         //     // }
//         // }
//         return -1;
//     }
//     public static void main() {
//         //MyBinarySearch mbs = new MyBinarySearch();
//         int arr[] = new int[8];
//         arr[0] = 2;
//         arr[1] = 4;
//         arr[2] = 6;
//         arr[3] = 8;
//         arr[4] = 10;
//         arr[5] = 12;
//         arr[6] = 14;
//         arr[7] = 16;
//         System.out.println(binarySearch(arr, 8, 14));

//         int arr1[] = new int[6];
//         arr1[0] = 6;
//         arr1[1] = 34;
//         arr1[2] = 78;
//         arr1[3] = 123;
//         arr1[4] = 432;
//         arr1[5] = 900;
//         System.out.println(binarySearch(arr1, 6, 431));
//     }
// }
