// // o mes começa em 0 e vai até 11 (12 meses)

// const sdata = new Date(2019, 3, 20, 15, 14, 27);
// console.log(sdata.toString());

// // 0 = domingo, 6 = sabado
const data = new Date('2019-04-20  20:20:59.100');
// console.log(data.toString());

console.log('Dia', data.getDate());
console.log('Mês', data.getMonth() + 1); // mês começa em 0
console.log('Ano', data.getFullYear());
console.log('Hora', data.getHours());
console.log('Min', data.getMinutes());
console.log('Seg', data.getSeconds());
console.log('ms', data.getMilliseconds());
console.log('Dia semana', data.getDay()); // 0 = domingo, 6 = sabado
