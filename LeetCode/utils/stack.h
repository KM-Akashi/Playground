#pragma once
#include <stdlib.h>
#include <stdio.h>

struct Stack
{
    int top;
    int max;
    int *stack;
};

struct Stack *CreateStack(int lens)
{
    struct Stack *s = (struct Stack *)malloc(sizeof(struct Stack));
    s->top = 0;
    s->max = lens - 1;
    s->stack = (int *)malloc(sizeof(int) * lens);
    return s;
}

int PopStack(struct Stack *s)
{
    if (s->top <= 0)
    {
        s->top = 0;
        return NULL;
    }

    int res = s->stack[s->top];
    s->top -= 1;
    return res;
}

void PushStack(struct Stack *s, int v)
{
    if (s->top >= s->max)
    {
        s->top = s->max;
    }

    s->top += 1;
    s->stack[s->top] = v;
}

void CleanStack(struct Stack *s)
{
    s->top = 0;
}