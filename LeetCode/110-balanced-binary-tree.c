int max(int a, int b)
{
    return a > b ? a : b;
}

int maxDepth(struct TreeNode *root)
{
    if (root == NULL)
        return 0;
    return max(maxDepth(root->left), maxDepth(root->right)) + 1;
}

bool isBalanced(struct TreeNode *root)
{
    if (root == NULL)
        return true;
    return abs(maxDepth(root->left) - maxDepth(root->right)) <= 1 && isBalanced(root->left) && isBalanced(root->right);
}