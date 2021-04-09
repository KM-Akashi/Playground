#include "utils/linked-list.h"

struct ListNode *deleteDuplicates(struct ListNode *head)
{
    if (head == NULL)
    {
        return head;
    }

    int count = 0;
    struct ListNode *p = head;
    int thisVal = head->val;
    while (p != NULL && p->val == thisVal)
    {
        p = p->next;
        count++;
    }
    head->next = deleteDuplicates(p);
    return head;
}