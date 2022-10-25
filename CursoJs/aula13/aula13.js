/* let a = 'A'; // B
let b = 'B'; // C
let c = 'C'; // A

const letras = [b, c, a]; // [B, C, A]

[a, b, c] = letras;  // Atribuição via desestruturação

console.log(a, b, c);  // B C A */
/* 
const array = [100, 200, 300, 400, 500, 600, 700, 800, 900];

const [primeiroElemento, segundoElemento, terceiroElemento, ...resto] = array;

console.log(`Primeiro elemento: ${primeiroElemento}, Segundo elemento: ${segundoElemento}, Terceiro elemento ${terceiroElemento} , Resto: ${resto}`); */

// const numeros = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

// console.log();

// conerter mmhg para atm

// recebeber input do usuário de mmhg e converter para atm e console.log

// const mmhg = prompt('Digite o valor em mmhg: ');

// const atm = mmhg / 760;

// console.log(`O valor em atm é: ${atm}`);



// criar um grafico de pizza com 5 valores aleatorios e inserir na div com id myChart

const valores = [Math.random() * 100, Math.random() * 100, Math.random() * 100, Math.random() * 100, Math.random() * 100];

const ctx = document.getElementById('myChart').getContext('2d');

const myChart = new Chart(ctx, {

    type: 'scatter',

    data: {
            datasets: [{
              label: 'Scatter Dataset',
              data: [{
                x: -10,
                y: 0
              }, {
                x: 30,
                y: 10
              }, {
                x: 10,
                y: 5
              }, {
                x: 4.5,
                y: 5.5
              }],
              backgroundColor: 'rgb(255, 99, 132)'
            }],
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// div com id myChart ter 500px de largura e 500px de altura e ter um background-color green

const grafico = document.getElementById('myChart');

grafico.style.width = '500px';
grafico.style.height = '500px';
