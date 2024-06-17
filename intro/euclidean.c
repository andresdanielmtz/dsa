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


// TODO: Correctly learn about this algorithm, please. 
int gcd(int u, int v) {
  int t; 
  while (u > 0) {
    if (u < v)
    {
      t = u; u = v; v = t; 
    }
    u = u - v;
  }
  return v; 
}

int main() {

  int x, y;
  while (scanf("%d %d", &x, &y) != EOF)
    if (x > 0 && y > 0)
      printf("%d %d %d\n", x, y, gcd(x, y));
}
