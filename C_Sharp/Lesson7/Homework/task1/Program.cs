// Задайте значения M и N. Напишите программу, которая выведет все натуральные числа 
// в промежутке от M до N. Использовать рекурсию, не использовать циклы.
// Пример:  
// M = 1; N = 5 -> "1, 2, 3, 4, 5"              
// M = 4; N = 8 -> "4, 5, 6, 7, 8"

void OutputNumbers(int m, int n)
{
    if (n == m - 1)
    {
        return;
    }
    OutputNumbers(m, n - 1);

    Console.Write(n + " ");
}

Console.Write("Введите первое число: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите второе число: ");
int n = Convert.ToInt32(Console.ReadLine());

OutputNumbers(m, n);

