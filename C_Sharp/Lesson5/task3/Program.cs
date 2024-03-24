// Задайте двумерный массив. Найдите сумму элементов, находящихся на главной диагонали (с индексами (0,0); (1;1) и т.д.

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

int GetSumArray(int[,] array)
{
  int sum = 0;

  for (int i = 0; i < array.GetLength(0); i++)
  {
    for (int j = 0; j < array.GetLength(1); j++)
    {
      if (i == j)
      {
        sum += array[i, j];
      }

    }
  }
  return sum;
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

int[,] array = Create2dArray(0, 50, 3, 4);
Show2dArray(array);
Console.WriteLine();
int getSum = GetSumArray(array);
Console.WriteLine($"Сумма элементов главной диагонали равна {getSum}");
