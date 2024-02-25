// Задать массив из 10 целых чисел. Определить количество четных чисел в массиве.

int [] array = new int [] {6, 7, 20, 36, 3, 1, 21, 55, 98, 100};
int counter = 0;

foreach(int item in array){

if(item % 2 == 0){
counter ++;
}

}

Console.Write($"Количество четных чисел в массиве: {counter}");