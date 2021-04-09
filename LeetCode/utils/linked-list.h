#pragma once
#include <stdlib.h>
#include <stdio.h>

// Definition for singly-linked list.
struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *NewListNode(int val)
{
    struct ListNode *newNode = (struct ListNode *)malloc(sizeof(struct ListNode));
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

struct ListNode *CreateListNode(int *vals, int n)
{
    if (n <= 0)
    {
        return NULL;
    }
    struct ListNode *root = NewListNode(vals[0]);
    struct ListNode *p = root;
    for (int i = 1; i < n; i++)
    {
        p->next = NewListNode(vals[i]);
        p = p->next;
    }
    return root;
}

void PrintList(struct ListNode *l)
{
    for (struct ListNode *p = l; p != NULL; p = p->next)
        printf("%d", p->val);
}