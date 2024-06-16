#include <stdlib.h>

struct node {
  int key;
  struct node *next;
};

void listInitalize() {
  struct node *head, *z, *t;
  head = (struct node *)malloc(sizeof *head);
  z = (struct node *)malloc(sizeof *z);
  head->next = z;
  z->next = z;
}

void deleteNext(struct node *t) { t->next = t->next->next; }

struct node *insertAfter(int v, struct node *t) {
  struct node *x;
  x = (struct node *)malloc(sizeof *x);
  x->key = v;
  x->next = t->next;
  t->next = x;
  return x;
}

int main() {}
