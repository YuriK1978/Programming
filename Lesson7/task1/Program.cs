// Напишите программу, которая будет принимать на вход число и возвращать сумму его цифр.
// Указание: использовать рекурсию.

// Пример:
// 123 => 6
// 63 => 9

int SumOfDigits(int num){
    if(num == 0){
        return 0;
    }
    int sum = num%10 + SumOfDigits(num/10);
    return sum;
}


Console.Clear();
int num = 1006;
int result = SumOfDigits(num);
Console.Write(result);
