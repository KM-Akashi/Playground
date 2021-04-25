#include "utils/min.h"

int minDistance(char *word1, char *word2)
{
    int lens1 = strlen(word1);
    int lens2 = strlen(word2);

    int levGrid[lens1 + 1][lens2 + 1];

    levGrid[0][0] = 0;
    for (int i = 1; i < lens1 + 1; i++)
        levGrid[i][0] = i;
    for (int i = 1; i < lens2 + 1; i++)
        levGrid[0][i] = i;

    for (int i = 1; i < lens1 + 1; i++)
    {
        for (int j = 1; j < lens2 + 1; j++)
        {
            if (*(word1 + i - 1) == *(word2 + j - 1))
                levGrid[i][j] = levGrid[i - 1][j - 1];
            else
                levGrid[i][j] = 1 + min3(levGrid[i - 1][j - 1], // Update levGrid[i-1][j-1],
                                         levGrid[i][j - 1],     // Insert levGrid[i][j-1],
                                         levGrid[i - 1][j]);    // Delete levGrid[i-1][j]
        }
    }

    return levGrid[lens1][lens2];
}