/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */
package Clase4;

import java.util.Scanner;


public class Ejercicio7Scanner {

    public static void main(String args[]) {
        
        int contador = 0 , total = 0, numero , resultado;
        Scanner sc = new Scanner(System.in);
        System.out.println("\n\nBienvenidos.");
        System.out.println("\nIndicar numeros para sumarlos e indicar la media.");
        System.out.println("\nPara terminar el programa indicar un numero negativo.");
        System.out.println("\nIndicar un numero: ");
        numero = Integer.parseInt(sc.nextLine());
        
        while(numero > 0){   
                total = numero + total;
                contador++;
                System.out.println("\nIndicar un numero: ");
                numero = Integer.parseInt(sc.nextLine());
            
            
        }
            resultado = total / contador;
            System.out.println("\n\nLa media de los numeros que puso es: " +resultado);
    }
}
