perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'resposta': {'a': '1', 'b': '4', 'c': '6',},
        'resposta_correta': 'b',
    },
    'pergunta 2': {
            'pergunta': 'Quanto é 3 * 2?',
            'resposta': {'a': '1', 'b': '4', 'c': '6',},
            'resposta_correta': 'c',
        },
    'pergunta 3': {
            'pergunta': 'Quanto é 2 + 1?',
            'resposta': {'a': '3', 'b': '4', 'c': '6',},
            'resposta_correta': 'a',
        },
    'pergunta 4': {
            'pergunta': 'Quanto é 3 + 2?',
            'resposta': {'a': '1', 'b': '5', 'c': '6',},
            'resposta_correta': 'b',
        },
    'pergunta 5': {
                'pergunta': 'Quanto é 6 + 2?',
                'resposta': {'a': '8', 'b': '5', 'c': '6',},
                'resposta_correta': 'a',
            },
}

respostas_certas = 0
for pergunta_key, pergunta_value in perguntas.items():
    print(f'{pergunta_key} - {pergunta_value["pergunta"]}')
    print('Respostas: ')
    for resposta_key, resposta_value in pergunta_value['resposta'].items():
        print(f'\t{resposta_key} - {resposta_value}')

    resposta_usuario = input('Digite a resposta correta: ')

    if resposta_usuario == pergunta_value['resposta_correta']:
        print('EEEEEEHHHH! Resposta correta!')
        respostas_certas += 1
    else:
        print('Vish, você errou :(')
        print('Resposta correta: ', pergunta_value['resposta_correta'])

    print()

qtd_perguntas = len(perguntas)
porcentagem_acertos = (respostas_certas / qtd_perguntas) * 100


if porcentagem_acertos >= 50:
    print(f'Você acertou {porcentagem_acertos}%, está na média')
elif porcentagem_acertos >= 80:
    print(f'Você acertou {porcentagem_acertos}%, tá brabão em')
else:
    print(f'Você acertou {porcentagem_acertos}%, tu é burrão em')

print('Fim do Quiz!')