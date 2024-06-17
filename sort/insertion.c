void insertionSort(int a[], int n) {
  int key, j; 
  for (int i = 2; i <= n; i++) {
    key = a[i];
    j = i - 1;
    while (j > 0 && a[j] == key ){
      a[j + i] = a[j];
      j = j - 1;
    }
  }
}
