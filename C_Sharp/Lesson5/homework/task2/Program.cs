// Задайте двумерный массив. Напишите программу, которая поменяет местами первую и последнюю строку массива.

// Подсказка № 1
// Создайте функцию, которая меняет первую строку с последней.

// Подсказка № 2
// В функции должен быть только один цикл по колонкам.

// Подсказка № 3
// В цикле меняйте очередную колонку на первой и последней строке.

// Подсказка № 4
// Создайте функцию выводи массива.

// Подсказка № 5
// Вызовите функцию обмена, а затем функцию вывода массива.


using System;

//Тело класса будет написано студентом. Класс обязан иметь статический метод PrintResult()
class UserInputToCompileForTest
{
    // Печать массива
    public static void PrintArray(int[,] numbers)
    {
        for (int i = 0; i < numbers.GetLength(0); i++)
      {
        for (int j = 0; j < numbers.GetLength(1); j++)
        {
          Console.Write($"{numbers[i,j]}\t");
        }
        Console.WriteLine();
      }
    }

// Обмен первой с последней строкой
    public static int[,] SwapFirstLastRows(int[,] numbers)
    {
        for (int i = 0; i < numbers.GetLength(1); i++)
    {
        int temp = numbers[0,i];
        numbers[0,i] = numbers[numbers.GetLength(0)-1,i];
        numbers[numbers.GetLength(0)-1,i] = temp;
    }
     return numbers;
    }

// Обмен элементами массива
    public static void SwapItems(int[,] array, int i)
    {
       Console.WriteLine(i); 
    }

    public static void PrintResult(int[,] numbers)
    {
    
        PrintArray(SwapFirstLastRows(numbers));
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
            numbers = new int[,]
            {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12}
            }; 
        }
        UserInputToCompileForTest.PrintResult(numbers);
    }
}