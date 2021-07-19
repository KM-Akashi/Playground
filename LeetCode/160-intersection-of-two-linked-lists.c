struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB)
{
    struct ListNode *A = headA, *B = headB;
    int lenA = 0, lenB = 0;
    while (A != NULL && A->next != NULL)
    {
        A = A->next;
        lenA++;
    }
    while (B != NULL && B->next != NULL)
    {
        B = B->next;
        lenB++;
    }
    A = headA;
    B = headB;
    if (lenA > lenB)
        for (int i = 0; i < lenA - lenB; i++)
            A = A->next;
    else
        for (int i = 0; i < lenB - lenA; i++)
            B = B->next;

    while (A != NULL || B != NULL)
    {
        if (A == B)
            return A;
        A = A->next;
        B = B->next;
    }
    return NULL;
}