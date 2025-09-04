class euclidean { 
    public static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        int remainder = a % b;
        return gcd(b, remainder);
    }

    public static void main(String[] args) {
        int a = 270;
        int b = 192;
        System.out.println("GCD of " + a + " and " + b + " is: " + gcd(a, b));
    }
}