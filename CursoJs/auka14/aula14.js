const pessoa = {
    nome: 'João',
    sobrenome: 'da Silva',
    idade: 20,
    endereco: {
        rua: 'Av Brasil',
        numero: 320
    }
};
//const nome = `${pessoa.nome} ${pessoa.sobrenome}`;

/* const { nome = 'Não existe', sobrenome, idade } = pessoa;  // desestruturação

console.log(nome , sobrenome, idade); */

const { endereco: { rua, numero, cep = '20930-502' } } = pessoa;

console.log(rua, numero, cep);