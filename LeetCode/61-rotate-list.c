#include "utils/linked-list.h"

struct ListNode *rotateRight(struct ListNode *head, int k)
{
    if (head == NULL)
        return head;
    int count = 0;
    struct ListNode *p = head;
    struct ListNode *tail;
    while (p != NULL)
    {
        count++;
        tail = p;
        p = p->next;
    }
    tail->next = head;
    int realK = count - (k % count);

    p = head;
    for (int i = 0; i < realK - 1; i++)
    {
        p = p->next;
    }
    struct ListNode *newHead = p->next;
    p->next = NULL;
    return newHead;
}