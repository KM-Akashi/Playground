#pragma once

void sort(int *list, int low, int high)
{
    if (low >= high)
        return;

    int i = low;
    int j = high;
    int pivotkey = list[i];
    while (i < j)
    {
        while (i < j && list[j] > pivotkey)
            j--;

        if (i < j)
            list[i++] = list[j];
        else
            break;

        while (i < j && list[i] < pivotkey)
            i++;

        if (i < j)
            list[j--] = list[i];
        else
            break;
    }

    list[i] = pivotkey;
    sort(list, low, i - 1);
    sort(list, i + 1, high);
}