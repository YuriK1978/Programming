// Задайте произвольный массив. Выведете его элементы, начиная с конца. Использовать рекурсию, не использовать циклы.

int[] CreateRandomArray(int size, int min = 0, int max = 10)
{
    int[] array = new int[size];
    for (int i = 0; i < size; i++)
    {
        array[i] = new Random().Next(min, max + 1);
    }
    return array;
}

void ShowArray(int[] array)
{
    foreach (int item in array)
    {
        Console.Write($"{item}\t");
    }
}

void ArrayReversal(int[] array, int size)
{
    if (size == 0)
    {
        return;
    }
    Console.Write($"{array[size - 1]}\t");
    ArrayReversal(array, size - 1);

}

int size = 7;
int[] array = CreateRandomArray(size);
ShowArray(array);
Console.WriteLine();
ArrayReversal(array, size); 