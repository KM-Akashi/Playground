#pragma once

int max(int a, int b)
{
    return a > b ? a : b;
}
int max3(int a, int b, int c)
{
    return a > max(b, c) ? a : max(b, c);
}