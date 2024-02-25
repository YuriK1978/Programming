// Принимаем на вход целое число из отрезка [10..99] и показывает наибольшую цифру числа.

Console.WriteLine("Введите число от 10 до 99");

int num = Convert.ToInt32(Console.ReadLine());

int first_digit = num / 10;

int second_digit = num % 10;

if (first_digit > second_digit){

    Console.WriteLine("Наибольшая цифра числа: " + first_digit);
    }

    else

    {

    Console.WriteLine("Наибольшая цифра числа: " + second_digit);
} 
