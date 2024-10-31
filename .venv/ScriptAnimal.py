import json

try:
    # Abre e carrega os dados do primeiro JSON
    with open("package.json", encoding='ISO-8859-1') as meu_json:
        dados = json.load(meu_json)

        # Coleta os nomes dos animais da primeira lista ("INSPECOES") para a comparação final
        animais_primeira_lista = set()

        # Contador para cada seção
        contador_rgns = 0
        contador_completo = 0
        contador_rgds = 0
        contador_rgd = 0
        contador_desclassificados = 0
        print(
            '---------------------------------------------** RGN **---------------------------------------------------')
        for inspecao in dados.get("INSPECOES", []):
            if inspecao.get('pkTipoInspecao') == 'RGN':
                print('Animal:', inspecao.get('nomeAnimal'), ' | ', 'Brinco:', inspecao.get('cgnAnimal'), ' | ',
                      inspecao.get('idParametro'), ' | ', inspecao.get('idStatus'))
                contador_rgns += 1  # Incrementa o contador
            nome_animal = inspecao.get("nomeAnimal")
            if nome_animal:
                animais_primeira_lista.add(nome_animal)
        print(f"Total de animais em RGNS: {contador_rgns}")
        print("")
        print('---------------------------------------------** Completos **---------------------------------------------------')
        for inspecao in dados.get("INSPECOES", []):
            if inspecao.get('pkTipoInspecao') == 'CGNmaisCGD_Femea' or inspecao.get('pkTipoInspecao') == 'RGNmaisRGD_Femea' :
                print('Animal:', inspecao.get('nomeAnimal'), ' | ', 'Brinco:', inspecao.get('cgnAnimal'), ' | ',
                      inspecao.get('idParametro'), ' | ', inspecao.get('idStatus'))
                contador_completo += 1  # Incrementa o contador
            nome_animal = inspecao.get("nomeAnimal")
            if nome_animal:
                animais_primeira_lista.add(nome_animal)
        print(f"--------------------#Total de animais em Completos: {contador_completo}", "#--------------------------------")
        print("")
        print('---------------------------------------------*** RGDS ***----------------------------------------------------')
        for inspecao in dados.get("INSPECOES", []):
            if inspecao.get('pkTipoInspecao') == 'RGDGD':
                print('Animal:', inspecao.get('nomeAnimal'), ' | ', 'Brinco:', inspecao.get('cgdAnimal'), ' | ',
                      inspecao.get('idParametro'), ' | ', inspecao.get('idStatus'))
                contador_rgds += 1  # Incrementa o contador
            nome_animal = inspecao.get("nomeAnimal")
            if nome_animal:
                animais_primeira_lista.add(nome_animal)
        print(f"Total de animais em RGDS: {contador_rgds}")

        print('-----------------------------------------**** RGD ****---------------------------------------')
        for inspecao in dados.get("INSPECOES", []):
            if inspecao.get('pkTipoInspecao') == 'RGDFEMEA':
                print('Animal:', inspecao.get('nomeAnimal'), ' | ', 'Brinco:', inspecao.get('cgdAnimal'), ' | ',
                      inspecao.get('idParametro'), ' | ', inspecao.get('idStatus'))
                contador_rgd += 1  # Incrementa o contador
            nome_animal = inspecao.get("nomeAnimal")
            if nome_animal:
                animais_primeira_lista.add(nome_animal)
        print(f"Total de animais em RGD: {contador_rgd}")

        print('-----------------------------------------**** Desclassificados ****---------------------------------------')
        for inspecao in dados.get("INSPECOES", []):
            if inspecao.get('idStatus') == 'AD':
                print('Animal:', inspecao.get('nomeAnimal'), ' | ', 'Brinco:', inspecao.get('cgdAnimal'), ' | ',
                      inspecao.get('idParametro'), ' | ', inspecao.get('idStatus'))
                contador_desclassificados += 1  # Incrementa o contador
            nome_animal = inspecao.get("nomeAnimal")
            if nome_animal:
                animais_primeira_lista.add(nome_animal)
        print(f"Total de animais Desclassificados: {contador_desclassificados}")

    # Abre e carrega os dados do segundo JSON
    with open("lista.json", encoding='ISO-8859-1') as animais_json:
        animais = json.load(animais_json)

        # Define a chave específica para acessar a lista de animais
        query_key = "SELECT  \r\na.nomeAnimal \r\nFROM Inspecao i \r\nINNER JOIN Animal a ON a.id = i.idAnimal \r\nWHERE i.idAtendimento = 2"

        # Coleta os nomes dos animais da segunda lista
        animais_segunda_lista = set()
        for animal in animais.get(query_key, []):
            nome_animal = animal.get("nomeAnimal")
            if nome_animal:
                animais_segunda_lista.add(nome_animal)

    # Calcula a diferença: animais na primeira lista, mas não na segunda
    diferenca_animais = animais_primeira_lista - animais_segunda_lista

    # Exibe os resultados da comparação
    print(
        '-----------------------------------------**** Animais da primeira lista que não estão na segunda ****---------------------------------------')
    if diferenca_animais:
        print('-----------------------------------------------------Animais Completos---------------------------------------------------')
        for animal in diferenca_animais:
            if inspecao.get('pkTipoInspecao') == 'CGNmaisCGD_Femea' or inspecao.get(
                    'pkTipoInspecao') == 'RGNmaisRGD_Femea':
                print('Animal:', inspecao.get('nomeAnimal'), ' | ', 'Brinco:', inspecao.get('cgnAnimal'), ' | ',
                      inspecao.get('idParametro'), ' | ', inspecao.get('idStatus'))



except FileNotFoundError:
    print("Erro: Um dos arquivos JSON não foi encontrado.")
except json.JSONDecodeError:
    print("Erro: Um dos arquivos JSON não é válido.")
except UnicodeDecodeError:
    print("Erro: Não foi possível decodificar um dos arquivos JSON.")
