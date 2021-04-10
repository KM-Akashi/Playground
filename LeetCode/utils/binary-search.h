#pragma once
#include <stdlib.h>
#include <stdio.h>

int BinarySearch(int *vals, int size, int key)
{
    int low = 0;
    int high = size - 1;
    while (low < high)
    {
        int mid = (int)((low + high) / 2);
        if (vals[mid] == key)
            return mid;
        else if (key < vals[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }

    return -1;
}