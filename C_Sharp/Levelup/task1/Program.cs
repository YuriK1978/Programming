// Сумма всех четных элементов массива
// Минимальное четное число
// Максимальное нечетное число массива
// Сформировать новый массив с уникальными элементами на основе текущего массива
// Упорядочить массив по возрастанию 
// Упорядочить массив по убыванию 
// Перевернуть массив

using System;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        int[] array = { 111, 23, 4, 111, 56, 88, 99, 76, 4, 54, 2, 91, 91 };

        Console.WriteLine("Сумма четных чисел исходного массива: " + array.Where(i => i % 2 == 0).Sum());

        Console.WriteLine("Минимальное четное число: " + array.Where(i => i % 2 == 0).Min());

        Console.WriteLine("Максимальное нечетное число: " + array.Where(i => i % 2 != 0).Max());

        // Формирование массива с уникальными элементами
        Console.WriteLine("Массив с уникальными элементами: ");
        int[] unic = array.Distinct().ToArray();
        unic.ToList().ForEach(i => Console.Write(i.ToString() + "  "));

        // Сортировка по возрастанию
        Console.WriteLine("\n" + "Сортировка по возрастанию: ");
        int[] sortedup = (array.OrderBy(i => i).ToArray());
        sortedup.ToList().ForEach(i => Console.Write(i.ToString() + "  "));

        // Сортировка по убыванию
        Console.WriteLine("\n" + "Сортировка по убыванию: ");
        int[] sorteddown = (array.OrderByDescending(i => i).ToArray());
        sorteddown.ToList().ForEach(i => Console.Write(i.ToString() + "  "));

        // Reverse
        Console.WriteLine("\n" + "Исходный массив: ");
        array.ToList().ForEach(i => Console.Write(i.ToString() + "  "));
        Console.WriteLine("\n" + "Перевернутый массив: ");
        int[] result = array.Reverse().ToArray();
        result.ToList().ForEach(i => Console.Write(i.ToString() + "  "));


    }

}



