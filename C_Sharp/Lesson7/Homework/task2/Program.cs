// Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.

static int AkkermanFunc(int m, int n)
{
    if (m == 0)
    {
        return n + 1;
    }
    else if (m > 0 && n == 0)
    {
        return AkkermanFunc(m - 1, 1);
    }
    else if (m > 0 && n > 0)
    {
        return AkkermanFunc(m - 1, AkkermanFunc(m, n - 1));
    }
    return -1;
}

Console.Write(AkkermanFunc(3, 2));