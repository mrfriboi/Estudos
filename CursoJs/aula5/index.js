 function meuEscopo () {
    const form = document.querySelector('.form'); // seleciona o formulário
    const resultado = document.querySelector('.resultado'); // seleciona o resultado
    const pessoas = []; 

    function recebeEventoForm (event) {
        event.preventDefault(); // impede que a página seja recarregada
        const nome = form.querySelector('.nome'); // seleciona o campo nome
        const sobrenome = form.querySelector('.sobrenome'); // seleciona o campo sobrenome
        const peso = form.querySelector('.peso');
        const altura = form.querySelector('.altura');

        const pessoa = { // cria um objeto pessoa
            nome: nome.value, 
            sobrenome: sobrenome.value,
            peso: peso.value,
            altura: altura.value,
        }

        //insere pessoa no array
        pessoas.push(pessoa);
        // inserir pessoas no resultado da tela
        resultado.innerHTML += `
            <p>
                <strong> Nome completo: ${pessoa.nome} ${pessoa.sobrenome}</strong>
                <span>Peso: ${pessoa.peso}</span>
                <span>Altura: ${pessoa.altura}</span>
            </p>
        `;

        // limpar os campos do formulario
        nome.value = '';
        sobrenome.value = '';
        peso.value = '';
        altura.value = '';

    }
    form.addEventListener('submit', recebeEventoForm); // quando o form for submetido, chama a função recebeEventoForm
}

meuEscopo();