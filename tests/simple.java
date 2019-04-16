<<<<<<< HEAD
class ifib{
    int iifiii();
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
        iifiii();
    }
}
=======
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
>>>>>>> 4aac6ae767f24a3d1727c99d87829f0010804aa0
