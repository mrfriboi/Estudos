function meuEscopo(){
    const form = document.querySelector('.form'); // seleciona o formulário
    const resultado = document.querySelector('.resultado'); // seleciona o resultado
    
    function recebeEventoForm(event){
        event.preventDefault();
        let ladoA = form.querySelector('.ladoA').value; // seleciona o campo lado1
        let ladoB = form.querySelector('.ladoB').value; // seleciona o campo lado2
        let ladoC = form.querySelector('.ladoC').value; // seleciona o campo lado3

        //.ladoA como float
        let ladoAfloat = parseFloat(ladoA);
        //.ladoB como float
        let ladoBfloat = parseFloat(ladoB);
        //.ladoC como float
        let ladoCfloat = parseFloat(ladoC);

        let array_ordenado = [ladoAfloat, ladoBfloat, ladoCfloat]; // ordena os valores em ordem crescente

        //ordernar os valores em ordem crescente 
        array_ordenado.sort(function(a, b){return a-b});
        console.log(array_ordenado);
        
        let maior = array_ordenado[2]; // seleciona o maior valor
        let menor = array_ordenado[0] + array_ordenado[1]; // seleciona o menor valor

        if(menor >= maior) { // verifica se o primeiro valor somado com o segundo é maior que o terceiro
            if (ladoA === ladoB && ladoB === ladoC) {
                // adiciocar em resultado
                resultado.innerHTML += `O Triangulo é Equilatero<br/>`;            
            }
            else if (ladoA === ladoB || ladoA === ladoC || ladoB === ladoC) {
                resultado.innerHTML += `O Triangulo é Icosceles<br/>`;  
            }
            else {
                resultado.innerHTML += `O Triangulo é Escaleno<br/>`;
            }
        } else {
            resultado.innerHTML += `Não é um triangulo<br/>`;
        }
        form.querySelector('.ladoA').disabled = true; // desabilita o campo lado1
        form.querySelector('.ladoB').disabled = true; // desabilita o campo lado2
        form.querySelector('.ladoC').disabled = true; // desabilita o campo lado3
        form.querySelector('.enviar').disabled = true; // desabilita o botão enviar
    }

    form.addEventListener('submit', recebeEventoForm); // quando o form for submetido, chama a função recebeEventoForm

    // RESETA RESULTADO ao apertar o botão refazer
    const refazer = document.querySelector('.refazer');

    refazer.addEventListener('click', function(){
        resultado.innerHTML = '';
        form.querySelector('.ladoA').disabled = false;
        form.querySelector('.ladoB').disabled = false;
        form.querySelector('.ladoC').disabled = false;
        form.querySelector('.enviar').disabled = false;
        form.reset(); // reseta o formulário
    })
}
meuEscopo(); // chama a função meuEscopo()

