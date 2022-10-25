/* for (let i = 0; i <= 5; i++) {
    console.log(`Linha $ {i}`);
}
 */

const elementos = [
    { tag: 'p', texto: 'Frase 1' },
    { tag: 'div', texto: 'Frase 2' },
    { tag: 'footer', texto: 'Frase 3' },
    { tag: 'section', texto: 'Frase 4' },
];

const container = document.querySelector('.container');
const div = document.createElement('div');
const h1 = document.createElement('h1');

for (let i = 0; i < elementos.length; i++) {
    let { tag, texto } = elementos[i];
    let tagCriada = document.createElement(tag);
    tagCriada.innerText = texto;
    div.appendChild(tagCriada);    
}

container.appendChild(h1);
container.appendChild(div);

