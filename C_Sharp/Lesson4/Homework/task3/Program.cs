// Напишите программу, которая перевернёт одномерный массив 
//(первый элемент станет последним, второй – предпоследним и т.д.)

void InputArray(int[] array)
{
  for (int i = 0; i < array.Length; i++)
    array[i] = new Random().Next(1, 11);
}

void ReverseArray(int[] array)
{
  for (int i = 0; i < array.Length / 2; i++)
  {
    int temp = array[i];
    array[i] = array[array.Length - 1 - i];
    array[array.Length - 1 - i] = temp;
  }
}

Console.Clear();
Console.Write("Введите кол-во элементов массива: ");
int n = Convert.ToInt32(Console.ReadLine());
int[] array = new int[n];
InputArray(array);
Console.WriteLine($"Начальный массив: [{string.Join(", ", array)}]");
ReverseArray(array);
Console.WriteLine($"Конечный массив: [{string.Join(", ", array)}]");