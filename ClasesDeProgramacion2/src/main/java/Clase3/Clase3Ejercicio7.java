/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Clase3;

import javax.swing.JOptionPane;


public class Clase3Ejercicio7 {
       public static void main(String[]args){
           int numero=0 , contador=0 ;
           numero = Integer.parseInt(JOptionPane.showInputDialog(null,"Indicar un numero:"));
           JOptionPane.showMessageDialog(null,"Si desea salir indicar un numero negativo.");
           
           while(numero > 0 ){
               contador++;
               numero = Integer.parseInt(JOptionPane.showInputDialog(null,"Indicar otro numero:"));
               
           }
           JOptionPane.showMessageDialog(null,"La cantidad de numeros instroducidos son "+contador);
       }
}
