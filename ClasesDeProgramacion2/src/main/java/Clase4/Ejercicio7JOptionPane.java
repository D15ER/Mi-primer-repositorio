/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */
package Clase4;

import javax.swing.JOptionPane;


public class Ejercicio7JOptionPane {

    public static void main(String args[]) {
        int contador = 0 , total = 0, numero , resultado;
        
        JOptionPane.showMessageDialog(null, "Indicar numeros positivos para sacar la media y un numero negativo para terminar el programa.");
        numero = Integer.parseInt(JOptionPane.showInputDialog("\nDigite un numero"));
        
        while(numero > 0){   
                total = numero + total;
                contador++;
                numero = Integer.parseInt(JOptionPane.showInputDialog("\nDigite un numero"));

            
            
        }
            resultado = total / contador;
            JOptionPane.showMessageDialog(null, "La media es: "+resultado);
    }
}
    

