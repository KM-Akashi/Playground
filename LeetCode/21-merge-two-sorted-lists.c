#include "utils/linked-list.h"

struct ListNode *merge2Lists(struct ListNode *list1, struct ListNode *list2)
{
    if (list1 == NULL)
    {
        return list2;
    }
    else if (list2 == NULL)
    {
        return list1;
    }

    struct ListNode *root = NULL;
    struct ListNode *p1, *p2;

    p1 = list1;
    p2 = list2;
    if (p1->val <= p2->val)
    {
        root = p1;
        p1 = p1->next;
    }
    else
    {
        root = p2;
        p2 = p2->next;
    }
    struct ListNode *p = root;
    while (p1 != NULL && p2 != NULL)
    {
        if (p1->val <= p2->val)
        {
            p->next = p1;
            p = p->next;
            p1 = p1->next;
        }
        else
        {
            p->next = p2;
            p = p->next;
            p2 = p2->next;
        }
    }
    if (p1 == NULL)
        p->next = p2;
    else if (p2 == NULL)
        p->next = p1;
    return root;
}