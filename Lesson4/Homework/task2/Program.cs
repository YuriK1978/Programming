// Задайте массив заполненный случайными положительными трёхзначными числами. 
// Напишите программу, которая покажет количество чётных чисел в массиве.

void InputArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
        array[i] = new Random().Next(100, 999);
}

int CountEven(int[] array)
{
    int counter = 0;
    foreach (int i in array)
    {
        if (i % 2 == 0)
            counter++;
    }

    return counter;
}

Console.Clear();
Console.Write("Введите количествово элементов: ");
int n = Convert.ToInt32(Console.ReadLine());
int[] array = new int[n];
InputArray(array);
int s = CountEven(array);
Console.WriteLine($"Количество чётных чисел в массиве: [{string.Join(", ", array)}] -> {s} ");
