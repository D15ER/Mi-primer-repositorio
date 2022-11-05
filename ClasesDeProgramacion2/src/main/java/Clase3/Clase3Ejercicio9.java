/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Clase3;

import javax.swing.JOptionPane;


public class Clase3Ejercicio9 {
    public static void main(String[]args){
        int numero , aleatorio , contador = 0;
        aleatorio = (int)(Math.random()*100);
        JOptionPane.showMessageDialog(null, "Se generera un numero aleatorio de 0 a 100.");
        numero = Integer.parseInt(JOptionPane.showInputDialog(null,"Indicar un numero"));
        
        while(numero != aleatorio){
            contador++;
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null, "El numero aleatorio es mas alto");
                numero = Integer.parseInt(JOptionPane.showInputDialog(null,"Indicar un numero"));
            }else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "El numero aleatorio es mas bajo");
                numero = Integer.parseInt(JOptionPane.showInputDialog(null,"Indicar un numero"));
            }
        }
        JOptionPane.showMessageDialog(null, "Felicidades");
        JOptionPane.showMessageDialog(null, "El numero aleatorio era: "+aleatorio);
        JOptionPane.showMessageDialog(null, "Intentos fallidos: "+contador);

    }
}
