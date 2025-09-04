#include <iostream>

// Passed to CPP for consistency purposes.
// This algorithm was taken from Robert Sedgewick's Algorithms in C

// ?? A teacher a couple of years ago asked us to implement this algorithm in
// Java. I'll try to do it once I get to understand it.
void erasthotenesSieve(int arr[], int N) {
  int i, j;
  std::cout << "The limit (n/2) is " << N / 2 << "\n";
  for (arr[1] = 0, i = 2; i <= N; i++)
    arr[i] = 1;

  //  It checks for the elements up until half of N, so 500
  //  Then, for those, it checks up until each multiple of i
  //  If Both elements are divisible (by N and by itself), it is therefore its
  //  prime.
  for (i = 2; i <= N / 2; i++)
    for (j = 2; j <= N / i; j++) {
      std::cout << "[" << i << ", " << j << "] = [" << i * j << "]" << "\n";

      arr[i * j] = 0;
    }

  for (i = 1; i <= N; i++)
    if (arr[i])
      std::cout << i << "\n";
}

int main() {
  int N = 1000;
  int arr[N];
  int size_arr = sizeof(arr) / sizeof(arr[0]);

  printf("Array Size: %d\n", size_arr);
  erasthotenesSieve(arr, size_arr);
  return 0;
}