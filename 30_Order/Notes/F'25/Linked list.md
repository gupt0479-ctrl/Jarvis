---
type: input
input_kind: book
status: sprout
created: 2025-09-30
source_url: DIS
related_progress:
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2021/Midterm - 1]]"
  - "[[C Language]]"
tags:
  - input
next: "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2021/Week - 3|Week - 3]]"
---
This example code snippet creates a linked list containing three elements (the list itself is referred to by the `head` variable that points to the first node in the list):

```c
struct node *head, *temp;
int i;

head = NULL;  // an empty linked list

head = malloc(sizeof(struct node));  // allocate a node
if (head == NULL) {
    printf("Error malloc\n");
    exit(1);
}
head->data = 10;    // set the data field
head->next = NULL;  // set next to NULL (there is no next element)

// add 2 more nodes to the head of the list:
for (i = 0; i < 2; i++) {
    temp = malloc(sizeof(struct node));  // allocate a node
    if (temp == NULL) {
        printf("Error malloc\n");
        exit(1);
    }
    temp->data = i;     // set data field
    temp->next = head;  // set next to point to current first node
    head = temp;        // change head to point to newly added node
}
```
