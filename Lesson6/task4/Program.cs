// На основе символов строки (тип string) сформировать массив символов (тип char[]). Вывести массив на экран.
// Указание: метод строки ToCharArray() не использовать.

string str1 = "hello";
char[] str2 = new char[str1.Length];
for (int i = 0; i < str1.Length; i++)
{

    str2[i] = str1[i];

}
foreach (char item in str2)
{

    Console.WriteLine(item);
}
