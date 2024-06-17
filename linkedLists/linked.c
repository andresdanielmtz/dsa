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

void deleteNext(struct node *t) { 
  /*
   * This deletes the next value by assigning its next to the next-next.
   * */
  t->next = t->next->next; 
}

void terminateList(struct node *head) { 
  struct node *traversal_node; 
  struct node *temp_head;

  traversal_node = head; temp_head = head; 
  while (traversal_node!=NULL){ 
    traversal_node = traversal_node->next; 
  }
  temp_head = traversal_node; 
}

// TODO: Traverse List (and print each element)


struct node *insertAfter(int v, struct node *t) {
  struct node *x; // Creates new node
  x = (struct node *)malloc(sizeof *x);
  x->key = v; // Asign new value
  x->next = t->next;
  t->next = x;
  return x;
}

int main() {}
