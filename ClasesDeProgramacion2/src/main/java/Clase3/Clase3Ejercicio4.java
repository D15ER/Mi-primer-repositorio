
package Clase3;
import java.util.Scanner;
/**
 *
 * @author MdiazOtazu
 */
public class Clase3Ejercicio4 {
    public static void main(String[] args){
        
        Scanner sc = new Scanner(System.in);
        int numero , conteo = 0;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(sc.nextLine());
        
        while(numero >= 0){
            System.out.println("El numero " +numero+ " es POSITIVO");
            conteo++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(sc.nextLine());

        }
        System.out.println("A Ingresado" + conteo + "numeros que no son negativos.");
    }
}
