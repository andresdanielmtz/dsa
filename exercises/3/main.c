// #include <stdio.h>

// CHAPTER 3 - EXERCISES

// Exercise 1

// Write a program to fill in a two-dimensional array of boolean values by
// setting a[i][j] to 1 if the greatest common divisor of i and j is 1 and to 0
// otherwise.

int gcd(int n1, int n2) {
  int i, gcd;
  for (i = 1; i <= n1 && i <= n2; ++i) {
    if (n1 % i == 0 && n2 % i == 0)
      gcd = i;
  }
  return gcd;
}

void boolean_matrix(int limit) {
  int i, j;
  int arr[limit][limit];
  for (i = 0; i <= limit; i++) {
    for (j = 0; j <= limit; j++) {
      if (gcd(i, j) == 1) {
        arr[i][j] = 1;
      } else {
        arr[i][j] = 0;
      }
    };
  };
}



