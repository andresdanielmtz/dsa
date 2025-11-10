#include <stdio.h>

typedef struct {
  int numerator; 
  int denominador;
} fraction;

int euclidean(fraction frac) { 
  return 2; // TODO: Finish this 
}

void convert(float num) {
}

int gcd(int dividend, int divisor) {
  int tempValue; 
  while (dividend > 0) {
    if (dividend < divisor)
    {
      tempValue = dividend; dividend = divisor; divisor = tempValue; 
    }
    dividend = dividend - divisor;
  }
  return divisor; 
}

int main() {
  int x, y;
  while (scanf("%d %d", &x, &y) != EOF)
    if (x > 0 && y > 0)
      printf("%d %d %d\n", x, y, gcd(x, y));
}
