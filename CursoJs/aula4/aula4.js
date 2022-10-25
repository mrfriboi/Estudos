function criaPessoa (nome, sobrenome, idade) {
    return {
        // nome: nome,
        // sobrenome: sobrenome,
        // idade: idade

        nome, sobrenome, idade
    };
}

const pessoa1 = criaPessoa("Lucas", "Santos", 23);
const pessoa2 = criaPessoa("João", "Silva", 25);
const pessoa3 = criaPessoa("Maria", "Souza", 20);

console.log(pessoa1);
console.log(pessoa2);
console.log(pessoa3);


