#include "utils/linked-list.h"

struct ListNode *swapPairs(struct ListNode *head)
{
    if (head == NULL)
        return NULL;
    if (head->next == NULL)
        return head;

    struct ListNode *newHead = head->next;
    head->next = swapPairs(head->next->next);
    newHead->next = head;

    return newHead;
}