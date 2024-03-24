// Задайте массив символов (тип char []). 
// Создайте строку из символов этого массива.
// Указание: Конструктор строки вида string(char []) не использовать.

char[] array = { '1', '2', '3', '4', '5' };
string str = "";
for (int i = 0; i < array.Length; i++)
{
    str += array[i];
}
Console.Write(str);
