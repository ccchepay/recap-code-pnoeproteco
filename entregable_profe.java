import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    //FUNCIONES
    static void imprimirCualidades(List<String> cualidades) {
        for (String cualidad : cualidades) {
            System.out.println(cualidad);
        }
    }

    static void agregarCualidades(List<String> cualidades) {
        boolean flag = true;
        Scanner scanner = new Scanner(System.in);
        while (flag) {
            System.out.println("Deseas agregar más condiciones?(Y/N)");
            if (scanner.nextLine().equals("Y")) {
                System.out.println("Escribe la propiedad: ");
                cualidades.add(scanner.nextLine());
            } else {
                flag = false;
            }
        }
    }

    static int cuestionarCualidades(List<String> cualidades) {
        int score = 0;
        Scanner scanner = new Scanner(System.in);
        for (String cualidad : cualidades) {
            System.out.println("Es " + cualidad + "? (Y/N)");
            if (!scanner.nextLine().equals("N")) {
                score++;
            }
        }
        return score;
    }

    static void calcularScore(int score, int len) {
        double ratio = (double) score / len;
        if (ratio == 1) {
            System.out.println("Es perfecto");
        } else if (ratio >= 0.8) {
            System.out.println("Apliquese o se lo ganan");
        } else if (ratio >= 0.6) {
            System.out.println("Momeno");
        } else if (ratio >= 0.4) {
            System.out.println("No te lo recomiendo");
        } else if (ratio <= 0.2) {
            System.out.println("Corre y no mires atrás");
        }
    }

    public static void main(String[] args) {
        //VARIABLES
        List<String> qualities = new ArrayList<>();
        qualities.add("alto");
        qualities.add("bronceado");
        qualities.add("guapo");
        qualities.add("rico");
        qualities.add("sexy");
        qualities.add("tierno");
        qualities.add("rudo");

        //PROGRAMA
        System.out.println("Vamos a ver si la persona que piensas te conviene");
        System.out.println("Estas son las cualidades que actualmente validamos");
        imprimirCualidades(qualities);
        agregarCualidades(qualities);
        System.out.println("Vamos a comenzar");

        int score = cuestionarCualidades(qualities);
        calcularScore(score, qualities.size());
    }
}
