#include "utils/linked-list.h"

struct ListNode *removeNthFromEnd(struct ListNode *head, int n)
{
    struct ListNode *p1 = head;
    struct ListNode *p2 = head;
    bool flag = false;
    for (int i; i < n + 1; i++)
    {
        if (p1 == NULL)
        {
            flag = true;
            break;
        }
        p1 = p1->next;
    }
    if (flag)
        return head->next;
    while (p1 != NULL)
    {
        p1 = p1->next;
        p2 = p2->next;
    }
    if (p2->next == NULL)
        return NULL;
    else if (p2->next->next == NULL)
        p2->next = NULL;
    else
        p2->next = p2->next->next;
    return head;
}