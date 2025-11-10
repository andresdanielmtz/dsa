class euclidean { 
    // ?? Recursive approach
    public static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        int remainder = a % b;
        return gcd(b, remainder);
    }

    // ?? Common, simpler method
    public static int gcd_common_method(int a, int b)
    {
        if (b == 0) return a; 
        int remainder = a % b; // TODO: Check if this method currently works.
        return gcd_common_method(b, remainder);
    }

    public static void main(String[] args) {
        int a = 270;
        int b = 192;
        System.out.println("GCD of " + a + " and " + b + " is: " + gcd(a, b));
        System.out.println("GCD of " + a + " and " + b + " is: " + gcd_common_method(a, b));
    }
}