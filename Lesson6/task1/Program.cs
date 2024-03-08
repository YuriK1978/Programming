// Соединение массивов

int [] array = new int [] {1, 2, 3};
int [] array2 = new int [] {4, 5, 6};
int [] arraytotal = array.Concat(array2).ToArray();

foreach(int item in arraytotal)
{
    Console.Write($"{item} ");

}

