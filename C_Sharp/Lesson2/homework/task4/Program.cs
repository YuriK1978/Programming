// На вход принимаем натуральное число N. На выходе показываем все его цифры через запятую.

Console.Write ("Введите число N: ");
    int N = Convert.ToInt32 (Console.ReadLine ());

    int num = N;
    int numDigit = 0;
    int decPow = 1;
    string str = "";

    while (num > 0)
    {
      numDigit++;
      num = num / 10;

      if (num > 0)
      {
        decPow = decPow * 10;
      }
    }
    
    for (int i = numDigit; i > 0; i--)
    {
      if(i != 1) {
        str += ((N / decPow) + ",");
      } else {
        str += N / decPow;
      }

      N = N % decPow;
      decPow = decPow / 10;
    }

    Console.WriteLine(str);
