/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Clase3;
import java.lang.Math;
import java.util.Scanner;
/**
 *
 * @author MdiazOtazu
 */
public class Clase3Ejercicio8 {
    public static void main(String[]args){
        int numero, aleatorio , contador = 0;
        Scanner sc = new Scanner(System.in);
        
        aleatorio = (int)(Math.random() *100);//Esteo genera un numero aleatorio
        System.out.println("\nBienvenido!!!");
        System.out.println("\nTiene que adivinar el numero que esta entre el 0-100.");
        System.out.println("Indique el primero numero: ");
        numero = Integer.parseInt(sc.nextLine());
        
        while(numero != aleatorio){
            contador++;
            if(numero > aleatorio){
                System.out.println("\nEl numero aleatorio es mas bajo.");
                System.out.println("\nIndique  otro numero: ");
                numero = Integer.parseInt(sc.nextLine());
            }else if(numero < aleatorio){
                System.out.println("\nEl numero aleatorio es mas alto.");
                System.out.println("\nIndique  otro numero: ");
                numero = Integer.parseInt(sc.nextLine());
            }
        }
        System.out.println("\n\nFELICIDADES!");
        System.out.println("\nEl numero aleatorio era: " +aleatorio);
        System.out.println("\nLa cantidad de veces que fracaso rotundamente son: "+contador);
    }
}
