#include "utils/linked-list.h"

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    struct ListNode *p1 = l1;
    struct ListNode *p2 = l2;

    int result[100];
    int i = 0;
    int carry = 0;
    while (!(p1 == NULL && p2 == NULL))
    {
        int a, b;
        if (p1 == NULL)
            a = 0;
        else
        {
            a = p1->val;
            p1 = p1->next;
        }
        if (p2 == NULL)
            b = 0;
        else
        {
            b = p2->val;
            p2 = p2->next;
        }

        int sum = a + b + carry;
        carry = 0;

        if (sum >= 10)
        {
            carry = 1;
            sum -= 10;
        }

        result[i] = sum;
        i++;
    }
    if (carry > 0)
    {
        result[i] = 1;
        i++;
    }
    return CreateListNode(result, i);
}
