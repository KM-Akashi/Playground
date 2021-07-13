struct ListNode *mergeTwoLists(struct ListNode *l1, struct ListNode *l2)
{
    if (l1 == NULL)
    {
        return l2;
    }
    else if (l2 == NULL)
    {
        return l1;
    }

    struct ListNode *root = NULL;
    struct ListNode *p1, *p2;

    p1 = l1;
    p2 = l2;
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

void dissectList(struct ListNode **head, struct ListNode **tail)
{
    if (*head == NULL)
    {
        *tail = NULL;
        return;
    }

    struct ListNode *p, *q;
    p = *head;
    q = *head;
    while (1)
    {
        if (p->next != NULL)
            p = p->next;
        else
            break;

        if (p->next != NULL)
        {
            q = q->next;
            p = p->next;
        }
        else
            break;
    }
    *tail = q->next;
    q->next = NULL;
}

int lenList(struct ListNode *l)
{
    struct ListNode *p = l;
    int len = 0;
    while (p != NULL)
    {
        len++;
        p = p->next;
    }
    return len;
}

struct ListNode *sortList(struct ListNode *head)
{
    if (head == NULL)
        return head;

    int len = lenList(head);
    if (len == 1)
        return head;

    struct ListNode *tail;
    dissectList(&head, &tail);
    return mergeTwoLists(sortList(head), sortList(tail));
}