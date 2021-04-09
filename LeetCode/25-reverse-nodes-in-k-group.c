#include "utils/linked-list.h"

struct Stack
{
    int top;
    int max;
    struct ListNode **stack;
};

struct Stack *CreateStack(int lens)
{
    struct Stack *s = (struct Stack *)malloc(sizeof(struct Stack));
    s->top = -1;
    s->max = lens;
    s->stack = (struct ListNode **)malloc(sizeof(struct ListNode *) * lens);
    return s;
}

void PopStack(struct Stack *s, struct ListNode **v)
{
    if (s->top > -1)
    {
        s->top -= 1;
        *v = s->stack[s->top + 1];
    }
}

void PushStack(struct Stack *s, struct ListNode *v)
{
    if (s->top < s->max)
    {
        s->top += 1;
        s->stack[s->top] = v;
    }
}

void CleanStack(struct Stack *s)
{
    s->top = -1;
}

struct ListNode *reverse(struct ListNode *head, struct Stack *stack)
{
    if (head == NULL)
    {
        CleanStack(stack);
        return NULL;
    }

    int i;
    struct ListNode *p = head;
    for (i = 0; i < stack->max; i++)
    {
        if (p != NULL)
        {
            PushStack(stack, p);
            p = p->next;
        }
        else
            break;
    }
    if (i < stack->max)
    {
        CleanStack(stack);
        return head;
    }

    struct ListNode *newHead;
    PopStack(stack, &newHead);
    struct ListNode *nextGroup = newHead->next;
    p = newHead;
    while (stack->top != -1)
    {
        PopStack(stack, &(p->next));
        p = p->next;
    }
    CleanStack(stack);
    p->next = reverse(nextGroup, stack);
    return newHead;
}

struct ListNode *reverseKGroup(struct ListNode *head, int k)
{
    struct Stack *stack = CreateStack(k);
    return reverse(head, stack);
}