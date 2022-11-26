/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */
package Clase4;

/**
 *
 * @author MdiazOtazu
 */
public class PruebaPersona {
    public static void main(String args[]) {
        
        // Creamos el objeto 
         
        Persona persona1 = new Persona(); //llamamos al constructor
        
        persona1.nombre = "Jose miguel";
        persona1.apellido = "Santoro";
        
        // LLamamos al metodo
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        persona2.nombre = "Rocio Belen";
        persona2.apellido = "Greco";
        persona2.obtenerInformacion();
    }
}
