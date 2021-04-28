#include "utils/stack.h"
#include <stdbool.h>

int longestValidParentheses(char *s)
{
    int len = strlen(s);
    if (len == 0 || len == 1)
        return 0;
    bool count[len];
    struct Stack *stack = CreateStack(len + 1);

    for (int i = 0; i < len; i++)
    {
        count[i] = false;
        switch (*(s + i))
        {
        case '(':
            PushStack(stack, i);
            break;
        case ')':
            if (stack->top != 0)
            {
                count[PopStack(stack)] = true;
                count[i] = true;
            }
            break;
        }
    }

    int max_continuity_len = 0;
    int continuity_len = 0;
    for (int i = 0; i < len; i++)
    {
        if (count[i])
            continuity_len++;
        else
            continuity_len = 0;

        if (continuity_len > max_continuity_len)
            max_continuity_len = continuity_len;
    }

    return max_continuity_len;
}