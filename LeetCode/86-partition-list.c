#include "utils/linked-list.h"

struct ListNode *partition(struct ListNode *head, int x)
{
    if (head == NULL)
    {
        return head;
    }

    struct ListNode *p;
    struct ListNode *tmp;
    struct ListNode *biger = NULL;
    struct ListNode *smaller = NULL;
    struct ListNode *pb = NULL;
    struct ListNode *ps = NULL;

    p = head;
    while (p != NULL)
    {
        if (p->val >= x)
        {
            if (pb == NULL)
            {
                biger = p;
                pb = p;
            }
            else
            {
                pb->next = p;
                pb = pb->next;
            }
        }
        else
        {
            if (ps == NULL)
            {
                smaller = p;
                ps = p;
            }
            else
            {
                ps->next = p;
                ps = ps->next;
            }
        }
        tmp = p;
        p = p->next;
        tmp->next = NULL;
    }
    if (smaller == NULL)
        return biger;
    else
    {
        ps->next = biger;
        return smaller;
    }
}