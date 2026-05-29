console.log("Camisa");
console.log("Termo");
console.log("Recogedor");
console.log("Soporte");

// Lista de metodos, se llaman arrays
const pedidos = ["Camisa", "Termo", "Recogedor" , "Soporte"];

// instruccion que recorre la lista y que hace algo con cada elemento

for (const metodo of pedidos) {
    console.log(metodo);
}

console.log("Fin del programa")


// ejemplo de bucle pedidos en el dia

const pedidosDelDia = [2, 1, 2, 1, 2];
let totalPedidos = 0;

for (const cantidad of pedidosDelDia) {
    totalPedidos = totalPedidos + cantidad;
 }

 // ejemplo de un for que corre pero no hace lo que queremos

  for (const cantidad of pedidosDelDia) {
   totalPedidos = cantidad;
  }

console.log(totalPedidos)

