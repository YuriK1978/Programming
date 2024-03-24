// Принимаем на вход трехзначное число и удаляем второе число

int num = 123;
int first = num / 100;
int last = num % 10;

// Первый вариант:
// int sum = (first*10) + last;
// Console.Write (sum);


// Второй вариант:

Console.Write("Number without second digit is " + first + last);

// Если сделать так: Console.Write("Number without second digit is " + (first + last));
// То ответ будет: 4, т.к. 1+3=4, а не конкатенация строк: first + last

