// Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.

// Подсказка № 1
// Создайте функцию, которая вычисляет сумму каждой строки в двумерном массиве, результат складывает в одномерный массив.

// Подсказка № 2
// Одномерный массив должен иметь размер, равный количеству строк.

// Подсказка № 3
// Напишите функцию, определяющую индекс минимального элемента, в одномерном массиве (туда будем подставлять массив сумм).

// Подсказка № 4
// Вызовите последовательно, функцию, вычисляющую суммы по строкам, а затем, функцию, определящую индекс минимального элемента.


int[,] Create2dArray(int min, int max, int rows, int cols)
{
    int[,] array = new int[rows, cols];
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            array[i, j] = new Random().Next(min, max + 1);
        }
    }
    return array;
}

void Show2dArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write(array[i, j] + "\t");
        }
        Console.WriteLine();
    }
}

void ShowArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write($"{array[i]} ");
    }
}

int MinIndex(int[] array)
{
    int idx = Array.IndexOf(array, array.Min());
    return idx;
}

int[] SumRows(int[,] array)
{
    int[] newArr = new int[array.GetLength(0)];

    for (int i = 0; i < array.GetLength(0); i++)
    {
        int sum = 0;

        for (int j = 0; j < array.GetLength(1); j++)
        {
            sum += array[i, j];
        }

        newArr[i] = sum;
    }

    return newArr;
}

int[,] array = Create2dArray(6, 50, 3, 4);
Show2dArray(array);
int[] newarr = SumRows(array);
ShowArray(newarr);
MinIndex(newarr);
Console.Write(MinIndex(newarr));


// Автопроверка
using System;

//Тело класса будет написано студентом. Класс обязан иметь статический метод PrintResult()
class UserInputToCompileForTest
{
    /// Вычисление сумм по строкам (на выходе массив с суммами строк)
    public static int[] SumRows(int[,] array)
    {
      int[] sum_rows = new int[array.GetLength(0)];
      for(int i = 0; i < array.GetLength(0);i++)
      {
        int sum_of_row = 0;
        for (int j = 0; j < array.GetLength(1); j++)
        {
          sum_of_row = sum_of_row+array[i,j];
        }
        sum_rows[i] = sum_of_row;
      }
      return sum_rows;
    }
    
    // Получение индекса минимального элемента в одномерном массиве
    public static int MinIndex(int[] array)
    {
       int min_index = 0;
      int min = array[0];
      for(int i = 0; i < array.Length;i++)
      {
        if (min > array[i])
        {
          min = array[i];
          min_index = i;
      }
     }
     return min_index;
    }
    public static void PrintResult(int[,] numbers)
    {   
       Console.Write(MinIndex(SumRows(numbers)));
    }
}

//Не удаляйте и не меняйте класс Answer!
class Answer
{
    public static void Main(string[] args)
    {
        int[,] numbers;

        if (args.Length >= 1)
        {
            // Предполагается, что строки разделены запятой и пробелом, а элементы внутри строк разделены пробелом
            string[] rows = args[0].Split(',');

            int rowCount = rows.Length;
            int colCount = rows[0].Trim().Split(' ').Length;

            numbers = new int[rowCount, colCount];

            for (int i = 0; i < rowCount; i++)
            {
                string[] rowElements = rows[i].Trim().Split(' ');

                for (int j = 0; j < colCount; j++)
                {
                    if (int.TryParse(rowElements[j], out int result))
                    {
                        numbers[i, j] = result;
                    }
                    else
                    {
                        Console.WriteLine($"Error parsing element {rowElements[j]} to an integer.");
                        return;
                    }
                }
            }
        }
        else
        {
            // Если аргументов на входе нет, используем примерный массив
            
            numbers = new int[,] {
                {1, 2, 3},
                {1, 1, 0},
                {7, 8, 2},
                {9, 10, 11}
    };      
        }
        UserInputToCompileForTest.PrintResult(numbers);
    }
}