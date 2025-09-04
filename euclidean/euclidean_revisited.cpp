#include <iostream>

// The euclidean algorithm is an efficient method for computing the greatest
// common divisor (gdc) of two integers

// ?? A teacher a couple of years ago asked us to implement this algorithm in
// Java. I'll try to do it once I get to understand it.

// Method as described in Khan Academy
double gcd(int a, int b) {
  if (a == 0)
    return b;
  if (b == 0)
    return a;

  int quotient = a / b;
  int remainder = a % b;
  a = (b * quotient) + remainder;

  return gcd(b, remainder);
}

// Common method
double gcd_improved(int a, int b) {
  if (b == 0)
    return a;

  int remainder = a % b;

  return gcd_improved(b, remainder);
}

int main() {
  int result = gcd(270, 192);
  std::cout << "result: " << result;
}