package firecode.level1;

public class Fibonacci {

    // Fibonacci Number
    public static int fib(int n) {
        return recursiveFibonacci(n);
    }

    public static int recursiveFibonacci(int n) {
        if (n == 0 || n == 1)
            return  n;
        else
            return fib(n-1) + fib(n-2);
    }

}