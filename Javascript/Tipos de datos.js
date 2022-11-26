// Comentarios de una linea

/* Comentarios de varias lineas*/

var nombre = "Ariel"; // STRING
console.log(nombre);

// Podemos ejecutar el codigo con control + shift + p
// Seleccionamos la opcion QUOKKA.js (Start/Stop)
// Sin necesidad de crear un archivo HTML

var numero = 3000; // INT
console.log(typeof numero); // Nos indica el tipo de dato que es(typeof)
nombre = 7;
console.log( typeof nombre)

var objeto = { // OBJETO
    nombre : "Ariel",
    edad : "20",
    telefono : " 1321321" 
}

console.log(typeof objeto);

// Tipos de datos Booleanos(Banderas)

var bandera = true;
console.log(typeof bandera)

// Tipo de dato funcion

function miFuncion(){}
console.log(miFuncion);

// Tipo de dato symbol

var simbolo = Symbol("JoseMariaListorti");
console.log(simbolo);

// Tipo de datos clases
class Persona{  // Clase = funcion
    constructor(nombre,apellido){
        this.nomre = nombre; // this hace referencia a los atributos de la clase
        this.apellido = apellido;
    }
}
console.log(Persona);