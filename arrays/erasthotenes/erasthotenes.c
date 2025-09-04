#include <stdio.h>

void erasthotenesSieve(int arr[], int N) {
  int i, j;

  printf("The limit (N/2) is %d \n", N / 2);
  // First, we fill out all entries with 1;
  for (arr[1] = 0, i = 2; i <= N; i++)
    arr[i] = 1;

  //  It checks for the elements up until half of N, so 500
  //  Then, for those, it checks up until each multiple of i
  //  If Both elements are divisible (by N and by itself), it is therefore its
  //  prime.
  for (i = 2; i <= N / 2; i++)
    for (j = 2; j <= N / i; j++) {
      printf("[%d, %d] = [%d]\n", i, j, i * j);

      arr[i * j] = 0;
    }

  // Print those elements that are still 1.
  for (i = 1; i <= N; i++)
    if (arr[i])
      printf("%4d", i);
}

int main() {
  int N = 1000;
  int arr[N];
  int size_arr = sizeof(arr) / sizeof(arr[0]);

  printf("Array Size: %d\n", size_arr);
  erasthotenesSieve(arr, size_arr);
  return 0;
}
