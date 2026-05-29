function calcularPrecio(precioUnitario, cantidad) {
    const total = precioUnitario * cantidad;
    return total;
}

console.log(calcularPrecio(5, 2));
console.log(calcularPrecio(3, 4));
console.log(calcularPrecio(7, 1));


// una funcion que decide
function puedePedir(cantidad) { 
  if (cantidad <= 50) {
    return true;
  } else {
    return false;
  } 
}
 
if (puedePedir(50)) {
    console.log("Pedido confirmado");
} else {
    console.log("Lo siento, maximo 50 pedidos por persona");
}
 // una funcion parecida, generada por AI

 function puedePedir(cantidad) {
    return cantidad <= 50;
 }
