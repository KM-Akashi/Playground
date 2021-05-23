char *defangIPaddr(char *address)
{
    char *res = (char *)malloc(sizeof(char) * (strlen(address) + 1 + 6));
    char *p = address;
    char *q = res;
    while (*p != '\0')
    {
        if (*p == '.')
        {
            *q++ = '[';
            *q++ = '.';
            *q++ = ']';
            *p++;
        }
        else
        {
            *q++ = *p++;
        }
    }
    *q = *p;
    return res;
}