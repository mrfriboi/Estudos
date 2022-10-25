const ladoA = prompt("Digite o primeiro lado do triangulo: ");
const ladoB = prompt("Digite o segundo lado do triangulo: ");
const ladoC = prompt("Digite o terceio lado do triangulo: ");

if (ladoA === ladoB && ladoB === ladoC) {
    document.body.innerHTML += `O Triangulo é Equilatero<br/>`;
    alert("O Triangulo é Equilatero");
}
else if (ladoA === ladoB || ladoA === ladoC || ladoB === ladoC) {
    document.body.innerHTML += `O Triangulo é Icosceles<br/>`;
    alert("O Triangulo é Icosceles");
}
else {
    document.body.innerHTML += `O Triangulo é Escaleno<br/>`;;
    alert("O Triangulo é Escaleno");
}



// document.body.innerHTML += `O seu nome é ${nome}<br/>`;
// document.body.innerHTML += `A segundo letra do seu nome é: ${nome.length} caracteres<br/>`;
// document.body.innerHTML += `A segunda letra do seu nome é: ${nome.charAt(1)}<br/>`;
// document.body.innerHTML += `Indice primeiro A: ${nome.indexOf("a")}<br/>`;
// document.body.innerHTML += `Indice do ultimo A: ${nome.lastIndexOf("a")}<br/>`;
// document.body.innerHTML += `As ultimas três letras são: ${nome.substr(-3)}<br/>`;
// document.body.innerHTML += `As palavras do seu nome são: ${nome.split(" ")}<br/>`;
// document.body.innerHTML += `Seu nome com letras maiusculas: ${nome.toUpperCase()}<br/>`;
// document.body.innerHTML += `Seu nome com letras maiusculas: ${nome.toLowerCase()}<br/>`;

