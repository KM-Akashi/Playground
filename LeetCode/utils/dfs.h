#pragma once
#include <stdbool.h>
#include "linked-list.h"

bool dfs(struct ListNode *A, struct ListNode *B)
{
    if (B == NULL)
        return true;
    if (A == NULL)
        return false;
    return A->val == B->val && dfs(A->left, B->left) && dfs(A->right, B->right);
}