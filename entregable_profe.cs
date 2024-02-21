using System;
using System.Collections.Generic;
					
public class Program
{
	
	static void ImprimirCualidades(List<string> cualidades)
    {
        foreach (var cualidad in cualidades)
        {
            Console.WriteLine(cualidad);
        }
    }

    static void AgregarCualidades(List<string> cualidades)
    {
        bool flag = true;
        while (flag)
        {
            Console.WriteLine("Deseas agregar más condiciones?(Y/N)");
            if (Console.ReadLine() == "Y")
            {
                Console.WriteLine("Escribe la propiedad: ");
                cualidades.Add(Console.ReadLine());
            }
            else
            {
                flag = false;
            }
        }
    }

    static int CuestionarCualidades(List<string> cualidades)
    {
        int score = 0;
        foreach (var cualidad in cualidades)
        {
            Console.WriteLine("Es {0}? (Y/N)",cualidad);
            if (Console.ReadLine() != "N")
            {
                score++;
            }
        }
        return score;
    }

    static void CalcularScore(int score, int len)
    {
        double ratio = (double)score / len;
        if (ratio == 1)
        {
            Console.WriteLine("Es perfecto");
        }
        else if (ratio >= 0.8)
        {
            Console.WriteLine("Apliquese o se lo ganan");
        }
        else if (ratio >= 0.6)
        {
            Console.WriteLine("Momeno");
        }
        else if (ratio >= 0.4)
        {
            Console.WriteLine("No te lo recomiendo");
        }
        else if (ratio <= 0.2)
        {
            Console.WriteLine("Corre y no mires atrás");
        }
    }
	
	public static void Main()
	{
		
		List<string> qualities = new List<string> { "alto", "bronceado", "guapo", "rico", "sexy", "tierno", "rudo" };

        //PROGRAMA
        Console.WriteLine("Vamos a ver si la persona que piensas te conviene");
        Console.WriteLine("Estas son las cualidades que actualmente validamos");
        ImprimirCualidades(qualities);
        AgregarCualidades(qualities);
        Console.WriteLine("Vamos a comenzar");

        int score = CuestionarCualidades(qualities);
        CalcularScore(score, qualities.Count);
	}
}