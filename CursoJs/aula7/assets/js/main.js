function meuEscopo(){
    const form = document.querySelector('.form'); // seleciona o formulário
    const erro = document.querySelector('.erro'); // seleciona o resultado
    const resposta = document.querySelector('.resposta'); // seleciona a resposta
    const refazer = document.querySelector('.refazer'); // seleciona o botão de refazer
    const enviar = document.querySelector('.enviar'); // seleciona o botão de enviar

    // oculta botão de refazer
    refazer.style.display = 'none';
    resposta.style.display = 'none';
    erro.style.display = 'none';
    
    function recebeEventoForm(event){
        event.preventDefault();
        let ladoA = form.querySelector('.ladoA').value; // seleciona o campo lado1
        let ladoB = form.querySelector('.ladoB').value; // seleciona o campo lado2
        let ladoC = form.querySelector('.ladoC').value; // seleciona o campo lado3

        let ladoAfloat = parseFloat(ladoA);  //.ladoA como float
        //.ladoB como float
        let ladoBfloat = parseFloat(ladoB);
        //.ladoC como float
        let ladoCfloat = parseFloat(ladoC);

        if (!ladoAfloat || !ladoBfloat || !ladoCfloat){ // verifica se sao numeros
            erro.style.display = 'block';
            resposta.style.display = 'none';
            refazer.style.display = 'none';
           return erro.innerHTML = 'Digite um número válido';
        }
        

        let array_ordenado = [ladoAfloat, ladoBfloat, ladoCfloat]; // ordena os valores em ordem crescente

        array_ordenado.sort(function(a, b){return a-b});     //ordernar os valores em ordem crescente 
        console.log(array_ordenado);
        
        let maior = array_ordenado[2]; // seleciona o maior valor
        let menor = array_ordenado[0] + array_ordenado[1]; // seleciona o menor valor

        if(menor >= maior) { // verifica se o primeiro valor somado com o segundo é maior que o terceiro
            if (ladoA === ladoB && ladoB === ladoC) {
                // adiciona o resultado no pagrafo resultado
                resposta.style.display = 'block';
                resposta.innerHTML = `<p>O triângulo é Equilátero</p>`;
            }
            else if (ladoA === ladoB || ladoA === ladoC || ladoB === ladoC) {
                resposta.style.display = 'block';
                resposta.innerHTML = `<p>O triângulo é Isosceles</p>`;
            }
            else {
                let paragrafo = document.createElement('p');
                resposta.style.display = 'block';
                resposta.innerHTML = `<p>O triângulo é Escaleno</p>`;
            }
        } else {
            erro.style.display = 'block';
            erro.innerHTML = `<p>Não é um triangulo</p>`;
        }

        form.querySelector('.ladoA').disabled = true; // desabilita o campo lado1
        form.querySelector('.ladoB').disabled = true; // desabilita o campo lado2
        form.querySelector('.ladoC').disabled = true; // desabilita o campo lado3
        
        enviar.style.display = 'none'; // oculta botão de enviar
        refazer.style.display = 'block'; // mostra botão de refazer  
        //elimna o erro
        erro.style.display = 'none';
    }
 
    form.addEventListener('submit', recebeEventoForm); // quando o form for submetido, chama a função recebeEventoForm

    refazer.addEventListener('click', function(){
        //previne o comportamento padrão do botão
        event.preventDefault();
        erro.innerHTML = '';
        resposta.innerHTML = '';

        form.querySelector('.ladoA').disabled = false;
        form.querySelector('.ladoB').disabled = false;
        form.querySelector('.ladoC').disabled = false;
        form.querySelector('.enviar').disabled = false;
        form.reset(); // reseta o formulário
        refazer.style.display = 'none';
        resposta.style.display = 'none';
        erro.style.display = 'none';
        enviar.style.display = 'block';
    })
}

meuEscopo(); // chama a função meuEscopo()


// abrir link no navegador
