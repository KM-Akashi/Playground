#pragma once

int min(int a, int b)
{
    if (a < b)
        return a;
    else
        return b;
}
int min(int a, int b, int c)
{
    if (a < min(b, c))
        return a;
    else
        return min(b, c);
}