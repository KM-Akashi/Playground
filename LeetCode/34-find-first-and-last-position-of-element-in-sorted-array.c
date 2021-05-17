/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int BinarySearch(int *vals, int size, int key)
{
    int low = 0;
    int high = size - 1;
    while (low <= high)
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

int *searchRange(int *nums, int numsSize, int target, int *returnSize)
{
    int index = BinarySearch(nums, numsSize, target);

    int *result = (int *)malloc(sizeof(int) * 2);
    result[0] = -1;
    result[1] = -1;
    *returnSize = 2;

    if (index == -1)
        return result;

    int left = index;
    int right = index;
    while (left > 0 && nums[left - 1] == target)
        left--;
    while (right < numsSize - 1 && nums[right + 1] == target)
        right++;

    result[0] = left;
    result[1] = right;
    return result;
}