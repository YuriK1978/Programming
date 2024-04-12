String[] string_array1 = new String[10] {"Monday", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday", "12", "-1", "terminator"};

Console.WriteLine(String.Join(", ", string_array1));

Console.WriteLine("");

string[] string_array2 = new string[string_array1.Length];

var counter = 0;    

for (int i = 0; i < string_array1.Length; i++)                  
{   
    if (string_array1[i].Length < 4)
    {
        string_array2[counter++] = string_array1[i];
        Console.Write($"{string_array1[i]}" + ", ");
        
    }   
}