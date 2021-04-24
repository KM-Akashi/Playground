int decodeRoman(char *p)
{
    switch (*p)
    {
    case 'I':
        return 1;
    case 'V':
        return 5;
    case 'X':
        return 10;
    case 'L':
        return 50;
    case 'C':
        return 100;
    case 'D':
        return 500;
    case 'M':
        return 1000;
    default:
        return 0;
    }
}

int romanToInt(char *s)
{
    // ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    // (1  , 5  , 10 , 50 , 100, 500,1000)
    char *p;
    int sum = 0;
    for (p = s; *p != '\0'; p++)
    {
        int now = decodeRoman(p);
        if (*(p + 1) != '\0' && now < decodeRoman(p + 1))
        {
            sum -= now;
        }
        else
        {
            sum += now;
        }
    }
    return sum;
}