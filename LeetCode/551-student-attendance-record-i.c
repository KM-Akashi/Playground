bool checkRecord(char *s)
{
    int countLate = 0, countAbsent = 0;

    for (char *p = s; *p != '\0'; p++)
    {
        if (*p == 'A')
            countAbsent++;
        if (*p == 'L')
            countLate++;
        else
            countLate = 0;

        if (countAbsent >= 2 || countLate >= 3)
            return false;
    }
    return true;
}