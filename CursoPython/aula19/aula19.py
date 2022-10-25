import random
from typing import List

# pegar pokemon aleatorio
indice: List[int] = []

for i in range(1):
    indice.append(random.randint(1, 150))

pokemon = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran","Nidorina","Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]

pokemonAleatorio = pokemon[indice[0]-1].lower()

digitado = [] # lista de digitos que o usuario digitou

chance = 5

while True:

# chances de acertar o pokemon
    if chance > 0:
        print(f'######################Você tem {chance} chances######################')
    else:
        print(f'o pokemon era {pokemonAleatorio}')
        print('Game Over')
        break


    letraDigitada = input(f'Digite uma letra: ').lower()

    if len(letraDigitada) > 1: # se o usuário digitou mais de uma letra
        print("Só pode digitar uma letra")
        continue


    pokemonAleatorioTemporario = '' # string que vai receber as letras que o usuario digitou

    digitado.append(letraDigitada)  # adiciona a letra digitada na lista digitado, se por ela dentro do if vc n consegue tirar no else

    if letraDigitada in pokemonAleatorio: # se a letra digitada estiver no pokemon aleatorio
        print(f'Acertou a letra "{letraDigitada}"')

    else:
        print(f'Errou, nao tem a letra "{letraDigitada}"')
        chance -= 1
        digitado.pop()


    for letraSecreta in pokemonAleatorio: # percorre o pokemon aleatorio
        if letraSecreta in digitado: # se a letra digitada estiver no pokemon aleatorio
            pokemonAleatorioTemporario += letraSecreta # adiciona a letra digitada na string pokemonAleatorioTemporario

        else:
            pokemonAleatorioTemporario += '*' # se nao tiver, adiciona um * na string pokemonAleatorioTemporario

    print(pokemonAleatorioTemporario)