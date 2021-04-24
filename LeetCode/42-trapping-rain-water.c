int trap(int *height, int heightSize)
{
    int sum = 0;
    if (heightSize <= 0)
        return sum;

    int lastTop = height[0];
    int lastTopIndex = 0;
    for (int i = 0; i < heightSize; i++)
    {
        if (height[i] >= lastTop)
        {
            // count
            for (int j = lastTopIndex; j < i; j++)
                sum += lastTop - height[j];

            lastTop = height[i];
            lastTopIndex = i;
        }
    }

    lastTop = height[heightSize - 1];
    lastTopIndex = heightSize - 1;
    for (int i = heightSize - 1; i >= 0; i--)
    {
        if (height[i] > lastTop)
        {
            // count
            for (int j = lastTopIndex; j > i; j--)
                sum += lastTop - height[j];

            lastTop = height[i];
            lastTopIndex = i;
        }
    }

    return sum;
}