int max(int a, int b)
{
    if (a < b)
        return b;
    else
        return a;
}

int climbStairs(int n)
{
    int count[n + 1];
    for (int i = 0; i < n + 1; i++)
    {
        if (i == 0)
            count[i] = 0;
        else if (i == 1)
            count[i] = 1;
        else if (i == 2)
            count[i] = 2;
        else
            count[i] = count[i - 1] + count[i - 2];
    }
    return count[n];
}