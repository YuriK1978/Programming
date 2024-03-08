// Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от 1 до N.
// Указание: использовать рекурсию. Не использовать цикл.

// Пример
// N=5 => 1 2 3 4 5

void GetSumDigit(int number)
{
    if (number == 0) 
        return;

    GetSumDigit(number - 1);
    
    Console.Write(number+" ");
}
GetSumDigit (5);
