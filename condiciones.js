// datos de la condicion

const pedidos = 8;
const sinPedidos = 8;

// condicional de si hay pedidos o no hay pedidos
// si el numero de pedidos es mayor que el numero de no pedidos devuelve "hay pedidos, abrir para pedir"
// si no devuelve "Sin pedidos, esperar por favor"

if (pedidos > sinPedidos) {
    console.log("Hay pedidos, abrir para pedir")
} else {
    console.log("Sin pedidos, esperar por favor")
}

//operadores de comparacion 

// mayor que
8 > 5 // true

// menor que 
3 < 10 // true

// mayor o igual 
8 >= 8 // true

// menor o igual
4 <= 9 // true

// igual a
5 === 5 // true

// distinto de 
5 !== 3 // true


const tasas = 2

if (tasas <= 2) {
    console.log("Puedes pedir")
} else {
    console.log("No puedes pedir")
}