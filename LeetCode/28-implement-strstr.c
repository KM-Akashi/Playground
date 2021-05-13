int strStr(char *haystack, char *needle)
{
    int strLen2 = strlen(needle);
    if (strLen2 == 0)
        return 0;
    int strLen1 = strlen(haystack);
    if (strLen2 > strLen1)
        return -1;

    int left = 0, right = 0, p = 0;
    while (right < strLen1 && p < strLen2)
    {
        if (haystack[right] != needle[p])
        {
            left++;
            right = left;
            p = 0;
        }
        else
        {
            right++;
            p++;
        }
    }
    if (p == strLen2)
        return left;
    else
        return -1;
}