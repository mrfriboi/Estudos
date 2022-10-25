const url = 'https://api.thecatapi.com/v1/images/search'; // Troque pela URL da sua API

// funcao para pegar a imgagem do gato
function getCat() {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const img = document.querySelector('img');
            img.src = data[0].url;  // pega a url da imagem
            img.alt = "Gato"; // adiciona um alt
            
        })
}

// api de frases em portugues




const botao = document.querySelector('#botao');
botao.addEventListener('click', function() {
    getCat();
    console.log('Clicou');   
})

botao.addEventListener('mouseover', function() {
    //console.log('Passou o mouse');
    //mouse pointer
    botao.style.cursor = 'pointer';
    // fonte mudar de cor
    botao.style.color = '#ffe0f9';
    // background mudar de cor
    botao.style.background = '#000';
    // borda mudar de cor
    botao.style.border = '1px solid #ffe0f9';

})

// quando o mouse sair do botão
botao.addEventListener('mouseout', function() {
    //console.log('Saiu do botão');
    botao.style.color = 'white';
    botao.style.background = 'pink';
    botao.style.border = '1px solid #000';
})


getCat(); // chama a funcao getCat