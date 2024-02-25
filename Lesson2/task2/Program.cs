// На вход подается трехзначное число.
// Нужно возвести второе число в степень, равную третьему числу

int num = 745;
int num_2 = num / 10;
int second = num_2 % 10;
int last = num % 10;
int result = second;

for (int i=0; i < last; i++){
    result *= second;
}
Console.WriteLine(result);

// Можно сделать с помощью Math.Pow
// Основание и показатель степени должны быть double, что может привести к необходимости преобразования типов.

// double baseNumber = 2;
// double exponent = 3;
// double result = Math.Pow(baseNumber, exponent);
// Console.WriteLine(result);  // Вывод: 8
