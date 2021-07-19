bool hasCycle(struct ListNode *head)
{
    if (head == NULL || head->next == NULL || head->next->next == NULL)
        return false;
    struct ListNode *p = head->next->next, *q = head->next;
    while (p != q && p->next != NULL && p->next->next != NULL)
    {
        p = p->next->next;
        q = q->next;
    }
    return p == q;
}