bool isValidBSTWithBound(struct TreeNode *root, int lowerBound, int upperBound)
{
    if (root == NULL)
        return true;
    return (root->left == NULL || (root->left->val < root->val && (root->left->val > lowerBound || lowerBound == NULL))) &&
           (root->right == NULL || (root->right->val > root->val && (root->right->val < upperBound || upperBound == NULL))) &&
           isValidBSTWithBound(root->left, lowerBound, root->val) && isValidBSTWithBound(root->right, root->val, upperBound);
}

bool isValidBST(struct TreeNode *root)
{
    if (root == NULL)
        return true;
    return (root->left == NULL || root->left->val < root->val) &&
           (root->right == NULL || root->right->val > root->val) &&
           isValidBSTWithBound(root->left, NULL, root->val) && isValidBSTWithBound(root->right, root->val, NULL);
}