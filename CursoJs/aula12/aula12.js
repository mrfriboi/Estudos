function getDayWeekText(diaSemana) {

    const semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'];

    switch (diaSemana) {
        case 0:
            diaSemanaTexto = semana[0];
            break;
        case 1:
            diaSemanaTexto = semana[1];
            break;
        case 2:
            diaSemanaTexto = semana[2];
            break;
        case 3:
            diaSemanaTexto = semana[3];
            break;
        case 4:
            diaSemanaTexto = semana[4];
            break;
        case 5:
            diaSemanaTexto = semana[5];
            break;
        case 6:
            diaSemanaTexto = semana[6];
            break;
        default:
            diaSemanaTexto = '';
            break;
    }
    return diaSemanaTexto;
}


const data = new Date();
const diaSemana = data.getDay();

// let diaSemanaTexto = getDayWeekText(diaSemana);
// ;
console.log(getDayWeekText(diaSemana), diaSemana);