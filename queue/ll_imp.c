#include <stdlib.h>


struct node { 
  int key; struct node * next;
};

static struct node *head, *tail, *z, *temp;

void queue_init() {
  head = (struct node *) malloc(sizeof *head);
  tail = (struct node *) malloc(sizeof *tail);

  z = (struct node *)malloc(sizeof *z);
  head->next = z;
  head->key = 0;
  tail = head;
  z->next = z;
}

int get() {  // get latest val
  struct node * tmp = head;
  while (tmp != NULL) {
    tmp=tmp->next;
  }
  return tmp->key; 
}

int get_first_val(){
  return head->key; 
}


void push(int v) { 
  temp = (struct node *) malloc(sizeof *temp); 
  temp->key = v; 
  temp->next = head->next;
  head->next = temp;
  temp->next = tail; // ??? 
}
