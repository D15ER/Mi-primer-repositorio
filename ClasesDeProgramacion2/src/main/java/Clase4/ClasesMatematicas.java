/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */
package Clase4;


public class ClasesMatematicas {
    
    int contador = 0 , total = 0, numero , resultado;
     public void SumasYConteo(){
         
         if(numero > 0){
             total = numero + total;
             contador++;
         }else{
             resultado = total / contador;
             System.out.println("\n\nLa media de los numeros que puso es: " +resultado);
         }
         
    }
}

