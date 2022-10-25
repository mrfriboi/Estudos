const nome = "Lucas";
const idade = 23;
const peso = 69;
const altura = 1.75;

let imc = peso / (altura**2);

let nascimento = 2022 - idade;

console.log(`${nome} tem ${idade} anos e pesa ${peso}Kg.`);
console.log(`tem ${altura}m de altura. Seu IMC é ${imc}`);
console.log(`${nome} nasceu em ${nascimento}.`);

if (imc < 18.5) {
    console.log(`${nome} está abaixo do peso.`);
}   
else if (imc >= 18.5 && imc < 25) {
    console.log(`${nome} está no peso ideal.`);
}
else if (imc >= 25 && imc < 30) {
    console.log(`${nome} está com sobrepeso.`);
}
else if (imc >= 30 && imc < 40) {
    console.log(`${nome} está com obesidade.`);
}
else {
    console.log(`${nome} está com obesidade mórbida.`);
}
