// Принимаем на вход число и проверяем: кратно ли оно одновременно 7 и 23?

int num_1 = 7;
int num_2 = 23;
int user_input = 322;

if(user_input % num_1 == 0 && user_input % num_2 == 0){
    Console.WriteLine ("Введенное число является кратным 7 и 23 одновременно!");
}
else {
    Console.WriteLine ("Введенное число НЕ кратно 7 и 23 одновременно!");
}
