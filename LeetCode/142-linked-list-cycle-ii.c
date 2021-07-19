// 设入口为a， 设快指针走了 a+b， 慢指针走了 a+c
// 则可得 2(a+c) = a+b
// => a = b-2c = 1环-c
// ps:其中环长 (a+b)-(a+c) = b-c
// 则慢指针再走a次，得 a+c+a = 2环 - c
// 或快指针再走a次，得 a+b+a = 3环 - c
// 环环抵消 意味着从头走a次和某个指针再走a次必重逢
struct ListNode *detectCycle(struct ListNode *head)
{
    if (head == NULL || head->next == NULL || head->next->next == NULL)
        return NULL;
    struct ListNode *p = head->next->next, *q = head->next;
    int pos = 0;
    while (p != q && p->next != NULL && p->next->next != NULL)
    {
        p = p->next->next;
        q = q->next;
    }
    if (p != q)
        return NULL;
    struct ListNode *t = head;
    while (q != t)
    {
        q = q->next;
        t = t->next;
    }
    return t;
}