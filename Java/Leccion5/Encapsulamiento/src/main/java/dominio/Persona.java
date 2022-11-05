/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dominio;
public class Persona {
    //Atributos
    private String nombre;
    private double sueldo;
    private boolean eliminado;
    
    // Constructor
    // indicamos nuestras variables
    public Persona(String nombre, double sueldo , boolean eliminado ){
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
        
        // Click derecho ---> Insert Code ---> Getters and Setters
        // Para generarlos automaticamente
        
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    
    public String toString(){ // Convierte en una cadena cada atributo
        return "Persona [ nombre:" +this.nombre +
                ",sueldo: " + this.sueldo + " ,eliminado: "
                + this.eliminado + "]";
        
    }
    
}
