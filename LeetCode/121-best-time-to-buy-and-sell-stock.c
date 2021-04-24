int maxProfit(int *prices, int pricesSize)
{
    int maxEarning = -1;
    int minPrice = prices[0];
    for (int i = 0; i < pricesSize; i++)
    {
        if (minPrice > prices[i])
            minPrice = prices[i];
        int earning = prices[i] - minPrice;
        if (earning > maxEarning)
            maxEarning = earning;
    }
    return maxEarning;
}