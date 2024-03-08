// Считать строку с консоли, содержащую латинские буквы. Вывести на экран согласные буквы этой строки.
// Указание: использовать рекурсию. Не использовать цикл.

// Пример:

// “hello” => h l l
// “World” => W r l d
// “Hello world!” => H l l w r l d

//if (char.IsAsciiLetter(s[0]) && !vovels.Contains(char.ToLower(s[0])))

void ShowLetters (string s)
{
    if (s.Length == 0)
        return;
    string vovels = "aeoyiu";
    if (char.IsLetter(s[0]) && !vovels.Contains(char.ToLower(s[0]))){
        Console.Write($"{s[0]} ");
    }
    ShowLetters(s.Substring(1));
}

ShowLetters("Cat");