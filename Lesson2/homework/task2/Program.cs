// На вход принимаем координаты точки и выдаем в какой четверти лежит точка с эитми координатами.

Console.WriteLine("Введите x: ");
double x = Convert.ToDouble(Console.ReadLine());
 
Console.WriteLine("Введите y: ");
double y = Convert.ToDouble(Console.ReadLine());
 
if (x > 0)
{
    if (y > 0)
        Console.WriteLine("1-я четверть");
    else if (y < 0)
        Console.WriteLine("4-я четверть");
}
else if (x < 0)
{
    if (y > 0)
        Console.WriteLine("2-я четверть");
    else if (y < 0)
        Console.WriteLine("3-я четверть");
}
 
//Console.ReadLine();
        
        