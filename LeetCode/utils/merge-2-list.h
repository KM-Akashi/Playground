#pragma once
int *merge(int *nums1, int nums1Size, int *nums2, int nums2Size)
{
    int merged[nums1Size + nums2Size];
    int i = 0;
    int n1 = 0;
    int n2 = 0;
    while (n1 < nums1Size && n2 < nums2Size)
    {
        if (nums1[n1] <= nums2[n2])
        {
            merged[i] = nums1[n1];
            n1++;
        }
        else
        {
            merged[i] = nums2[n2];
            n2++;
        }
        i++;
    }

    while (n1 < nums1Size)
        merged[i++] = nums1[n1++];

    while (n2 < nums2Size)
        merged[i++] = nums2[n2++];

    return merged;
}