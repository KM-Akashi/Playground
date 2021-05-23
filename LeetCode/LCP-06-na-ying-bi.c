int minCount(int *coins, int coinsSize)
{
    int count = 0;
    for (int i = 0; i < coinsSize; i++)
    {
        count += coins[i] / 2;
        count += coins[i] % 2;
    }
    return count;
}