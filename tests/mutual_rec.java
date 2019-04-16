class mutual_recursion{


    int odd_function(int n){
        int odd;
	System.out.println(-1);
	System.out.println(n);
        if (n==0){
            odd = 0;
        }
        else{
            odd = even_function(n-1);
        }
        return odd;
    }
    int even_function(int n){
        int even;
	System.out.println(-2);
	System.out.println(n);
        if (n==0){
            even = 1;
        }
        else{
            even = odd_function(n-1);
        }
        return even;
    }
    public static void main(){
        System.out.println(odd_function(16));
    }
}
