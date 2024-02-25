// Задать массив из вещественных чисел с ненулевой дробной частью.
// Найти разницу между максимальным и минимальным элементами массива.

double [] array = new double [] {22.23, 34.53, 28.82, 78.16, 10.17, 99.91, 55.55, 87.56};

Console.WriteLine("Minimum number is " + array.Min());
Console.WriteLine("Maximum number is " + array.Max());

double max = array.Max();
double min = array.Min();

Console.WriteLine("Differense between maximun and minimum is " + (max - min));