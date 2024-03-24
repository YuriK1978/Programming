﻿// Задать одномерный массив из 10 целых чисел от 1 до 100.
// Найдите количество элементов массива, которые лежат в отрезке 20..90. 

// Пример: [10, 21, 14, 93, 23] --> 2

int [] array = new int [] { 90, 24, 70, 6, 50, 9, 20, 55, 98, 99 };
int counter = 0;

  foreach (int element in array)
  {
    if (element >= 20 && element <= 90)
      counter++;
  }
   
Console.Write($"Количество элементов массива, лежащих в заданном интервале: {counter}");



   
