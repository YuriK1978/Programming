// : Задайте двумерный массив символов (тип char [,]). Создать строку из символов этого массива. 
// Пример:
// a b c => “abcdef”
// d e f 

string[,] Tablero = new string[3, 3] {{"a","b","c"},
                                      {"d","e","f"},
                                      {"g","h","i"} };




Console.WriteLine(string.Concat(test, test1, test2));






// string input = "hello world";
// string output = new string(input.ToCharArray().Reverse().ToArray());
// Console.WriteLine(output);

// Метод Reverse (как и большинство остальных методов Linq) возвращает IEnumerable, но у класса String нет конструктора, 
// принимающего IEnumerable<char>, зато есть конструктор, принимающий массив. 
// Метод ToArray как раз и собирает массив на основе входной последовательности IEnumerable.