
package Clase3;

import javax.swing.JOptionPane;


public class Clase3Ejercicio5 {
    public static void main(String[]args){
            int numero, par = 0 , impar = 0; 
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            JOptionPane.showMessageDialog(null , "Poner un 0 para terminar el programa");

            while(numero != 0){
                if(numero % 2 == 0){
                par++;
                }else{
                impar++;
                }
                numero = Integer.parseInt(JOptionPane.showInputDialog("Digite  otro numero: "));

        }
            JOptionPane.showMessageDialog(null , "esta es la cantidad de numeros pares totales " + par );
            JOptionPane.showMessageDialog(null , "esta es la cantidad de numeros impares totales " + impar );
    }    
}
