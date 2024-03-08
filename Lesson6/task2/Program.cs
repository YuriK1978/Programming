// создание строк

string test = null; // без любого значения. Место в памяти не резервируется.
string test1 = "";     // строка со значением и зарезервированным местом в памяти, но в ней ничего нет.
string test1_1 = string.Empty; // То же что string test1 = "";

// Проверка:
bool flag = string.IsNullOrEmpty(test);
if(string.IsNullOrEmpty(test))
{
    // Block1...
}

// Проверка:
string test1 = "\n          \t";
bool flag = string.IsNullOrWhiteSpace(test1);

...........................................................................................

string test2 = "abcd"
string test4 = new string('x', 4); // вывод: xxxx
string test5 = new string(new [] {'h', 'e', 'l', 'l', 'o'}; // вывод: hello
...........................................................................................

string test = "Hello";
string test2 = "world";
test += test2;
// или:
Console.WriteLine(string.Concat(test, test2));

...........................................................................................
// Объединение массива в одну строку

string test = string.Join(",", new int [] {1, 2, 3}); // первым аргументом идет разделитель!
Console.WriteLine(test);
// вывод: 1,2,3
......................................................
string[] test = { "Hello", "World" }; // Alternative array creation syntax 
string result = String.Join(" ", test);

...........................................................................................
// Подстроки.

string test = "                Test                ";
Console.WriteLine(test.Trim()); // минус пробелы из начала и конца строки
// Вывод: Test
// test.TrimStart() - удалит только из начала
// test.TrimEnd() - удалит только из конца

Console.WriteLine(test.Trim(' ', 't')); // вначале удалит пробел, а в конце t (включительно)
// Вывод: Tes

................................................
// Разделение

string test = "10,11,12";
foreach(string item in test.Split(","))
{
    Console.WriteLine(item);
}
// Вывод: 
//10
//11
//12
................................................
string test = "geek brains";
Console.WriteLine(test.Substring(0,4));
// Вывод: geek

string test = "geek brains";
Console.WriteLine(test.Substring(6,5)); // после 6го символа 5 символов
// Вывод: rains
Console.WriteLine(test.Substring(5)); // после 5го до конца строки
// Вывод: brains

