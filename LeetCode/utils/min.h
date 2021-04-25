#pragma once

int min(int a, int b)
{
    return a < b ? a : b;
}
int min3(int a, int b, int c)
{
    return a < min(b, c) ? a : min(b, c);
}