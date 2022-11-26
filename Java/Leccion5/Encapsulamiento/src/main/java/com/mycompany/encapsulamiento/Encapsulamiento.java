/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.encapsulamiento;

import dominio.Persona;

public class Encapsulamiento {

    public static void main(String[] args) {
        
        // Importamos y Generamos nuestro encapsulamiento y pasamos los parametros
        Persona persona1 = new Persona("matias" , 100000 , false);
        System.out.println("Persona1 su nombre es : "+persona1.getNombre());
        // Modificar a traves de los metodos
        persona1.setNombre("Jose");
        System.out.println("Actualizacion del nombre de persona1: "+persona1.getNombre());
        // Tarea: Crear otro objeto de tipo persona, asignar los valores de manera inicial
        //y imprimir, luego modificar sus valores y volver a imprimir
        
        Persona persona2 = new Persona("Rocio Belen Greco" , 200000, false);
        
        System.out.println("Indicamos los valores de persona2: \n"+persona2.getNombre()+ "\n" + persona2.getSueldo() + "\n" + persona2.isEliminado() );
        persona2.setNombre("Matias diaz de Otazu");
        persona2.setSueldo(10);
        persona2.setEliminado(true);
        
        System.out.println("Indicamos los  nuevos valores de persona2: \n"+persona2.getNombre()+ "\n" + persona2.getSueldo() + "\n" + persona2.isEliminado() );
        System.out.println("persona1: " + persona1.toString()); // Mostramos el metodo toString
        System.out.println("persona2: " + persona2); // No es un necesario mostrarlo para que ejecute
    }
}
