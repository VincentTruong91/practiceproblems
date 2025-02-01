#include <stdio.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* reverseList(struct Node* head){

    struct Node *curr = head;
    struct Node *prev = NULL;
    struct Node *next;

    while (curr != NULL){
        next = curr->next;
        curr->next = prev; //reverse current node's next pointer
        prev = curr;
        curr = next;
    }
    return prev;
}

struct Node* createNode(int new_data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = NULL;
    return new_node;
}