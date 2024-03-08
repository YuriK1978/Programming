 // Дан двумерный массив 3*4 надо поменять местами первую и последнюю строчку массива.
 
 var array = new int[3, 4]
            { { 1, 2, 3, 4 },
              { 0, 0, 0, 0 },
              { 5, 6, 7, 8 },
            };
            for(int i = 0; i < array.GetLength(1); i++)
            {
                var tmp = array[2, i];
                array[2, i] = array[0, i];
                array[0, i] = tmp;
            }
            for(int i = 0; i < array.GetLength(0); i++)
            {
                for(int j = 0; j < array.GetLength(1); j++)
                {
                    Console.Write(array[i,j] + " ");
                }
                Console.WriteLine();
            }
            Console.ReadKey(true);

// Дан двумерный массив 4*4 надо поменять местами первую и последнюю строчку массива.
//  var array = new int[4, 4]
//             { { 1, 2, 3, 4 }, 
//               { 0, 0, 0, 0 },
//               { 0, 0, 0, 0 },
//               { 5, 6, 7, 8 }
//             };
//             for(int i = 0; i < array.GetLength(1); i++)
//             {
//                 var tmp = array[3, i];
//                 array[3, i] = array[0, i];
//                 array[0, i] = tmp;
//             }
//             for(int i = 0; i < array.GetLength(0); i++)
//             {
//                 for(int j = 0; j < array.GetLength(1); j++)
//                 {
//                     Console.Write(array[i,j] + " ");
//                 }
//                 Console.WriteLine();
//             }
//             Console.ReadKey(true);
