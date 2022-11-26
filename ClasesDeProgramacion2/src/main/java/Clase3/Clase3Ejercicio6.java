/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Clase3;

import java.util.Scanner;


public class Clase3Ejercicio6 {
    public static void main(String[]args){
        
        int numero = 0 , contador = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("\nIndicar un numero:");
        numero = Integer.parseInt(sc.nextLine());
        System.out.println("\nSi desea terminar el programa marcar un numero negativo.");
        
        while(numero > 0){
            contador++;
            System.out.println("\nIndicar otro numero:");
            numero = Integer.parseInt(sc.nextLine());
        }
        System.out.println("\n\nSe han introducido "+contador+" numeros positivos.");
    }
}
