// На вод принимаются два числа
// Вывести: является ли первое число кратным второму, тначе вывести остаток от деления

int num = 101;
int num_2 = 5;

if (num % num_2 == 0 ){
    Console.WriteLine("Да");
}

if (num % num_2 != 0){
    Console.WriteLine(num % num_2);
}