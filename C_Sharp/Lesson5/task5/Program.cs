﻿// В следующем примере используются GetLowerBound методы и GetUpperBound методы для отображения границ одномерного и двумерного массива и отображения значений элементов массива.

// GetLowerBound(0) возвращает начальный индекс первого измерения массива и GetLowerBound(Rank - 1) возвращает начальный индекс последнего измерения массива.

// Метод GetLowerBound всегда возвращает значение, указывающее индекс нижней границы массива, даже если массив пуст.

using System;

public class Example
{
    public static void Main()
    {
        // Create a one-dimensional integer array.
        int[] integers = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 };
        // Get the upper and lower bound of the array.
        int upper = integers.GetUpperBound(0);
        int lower = integers.GetLowerBound(0);
        Console.WriteLine($"Elements from index {lower} to {upper}:");
        // Iterate the array.
        for (int ctr = lower; ctr <= upper; ctr++)
            Console.Write($"{(ctr == lower ? "   " : "")}{integers[ctr]}" +
                          $"{(ctr < upper ? ", " : Environment.NewLine)}");

        Console.WriteLine();

        // Create a two-dimensional integer array.
        int[,] integers2d = { {2, 4}, {3, 9}, {4, 16}, {5, 25},
                           {6, 36}, {7, 49}, {8, 64}, {9, 81} };
        // Get the number of dimensions.
        int rank = integers2d.Rank;
        Console.WriteLine($"Number of dimensions: {rank}");
        for (int ctr = 0; ctr < rank; ctr++)
            Console.WriteLine($"   Dimension {ctr}: " +
                              $"from {integers2d.GetLowerBound(ctr)} to {integers2d.GetUpperBound(ctr)}");

        // Iterate the 2-dimensional array and display its values.
        Console.WriteLine("   Values of array elements:");
        for (int outer = integers2d.GetLowerBound(0); outer <= integers2d.GetUpperBound(0);
             outer++)
            for (int inner = integers2d.GetLowerBound(1); inner <= integers2d.GetUpperBound(1);
                 inner++)
                Console.WriteLine($"      {'\u007b'}{outer}, {inner}{'\u007d'} = " +
                                  $"{integers2d.GetValue(outer, inner)}");
    }
}