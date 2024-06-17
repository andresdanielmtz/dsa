#define max 100

int key[max + 2], next[max + 2];
int x, head, z;

void listInitialize() {
  head = 0;
  z = 1;
  x = 2;
  next[head] = z;
  next[z] = z;
}

void deleteNext(int t) {
  next[t] = next[next[t]];
  int insertAfter(int v, int t);
}

int insertAfter(int v, int t) {
  key[x] = v;
  next[x] = next[t];
  next[t] = x;
  return x++;
}

int main() { return 0; }
