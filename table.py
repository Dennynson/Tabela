# Desenvolvedor: Dennynson Scheydt (20240010564)

# Função para criar tabela
def criar_tabela(nomes_colunas, matriz_valores):
    if not nomes_colunas or not matriz_valores:
        raise ValueError("As colunas e a matriz de valores não podem ser vazios.")

    for linha in matriz_valores:
        if len(nomes_colunas) != len(linha):
            raise ValueError("Número de colunas e valores não correspondem.")

    tabela = {}
    for i in range(len(nomes_colunas)):
        valores_coluna = []
        for linha in matriz_valores:
            valores_coluna.append(linha[i])
        tabela[nomes_colunas[i]] = valores_coluna
    return tabela

# Função para adicionar uma linha
def adicionar_linha(tabela, linha):
    if len(linha) != len(tabela):
        raise ValueError("Dimensão da linha inválida.")
    for i, key in enumerate(tabela.keys()):
        tabela[key].append(linha[i])

# Função para remover linha
def remover_linha(tabela, indice):
    if indice < 0 or any(indice >= len(coluna) for coluna in tabela.values()):
        raise IndexError("Índice fora do intervalo válido.")
    for key in tabela.keys():
        tabela[key].pop(indice)

# Função para adicionar coluna
def adicionar_coluna(tabela, nome_coluna, valores_coluna):
    if len(valores_coluna) != len(list(tabela.values())[0]):
        raise ValueError("Dimensão dos valores das colunas inválida.")
    tabela[nome_coluna] = valores_coluna

# Função para remover coluna
def remover_coluna(tabela, nome_coluna):
    if not tabela:
        raise ValueError("A tabela está vazia.")
    if nome_coluna not in tabela:
        raise KeyError("Coluna não encontrada.")
    del tabela[nome_coluna]

# Função para somas valores das colunas
def soma_colunas(tabela):
    soma = {} 
    for key, value in tabela.items():  # Percorre cada chave e lista de valores
        # Verifica se todos os elementos da lista 'value' são numéricos (int ou float)
        if all(isinstance(x, (int, float)) for x in value):
            soma[key] = sum(value)
    return soma

# Função para calcular a média dos valores da tabela
def media_colunas(tabela):
    media = {}
    for key, value in tabela.items(): 
        if all(isinstance(x, (int, float)) for x in value):
            media[key] = f"{sum(value) / len(value):.2f}"
    return media

# Função para imprimir a tabela
def exibir_tela(tabela):
    cabecalho = list(tabela.keys())  # Converte as chaves para uma lista
    print("\t".join(cabecalho))  # Imprime as chaves separadas por tabulação

    numero_de_linhas = len(next(iter(tabela.values())))  # Pega o número de elementos na primeira coluna
    for i in range(numero_de_linhas):
        linha = []  # Lista para armazenar os valores da linha
        for key in cabecalho:  # Para cada coluna (chave)
            linha.append(str(tabela[key][i]))  # Adiciona o valor da coluna na linha
        print("\t".join(linha))  # Imprime a linha, com valores separados por tabulação

# Função para abrir arquivo CSV
def nova_tabela(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    linhas = arquivo.readlines() # Lê todas as linhas do arquivo e as armazena em uma lista chamada linhas
    
    chaves = linhas[0].strip().split(",") # obtém as chaves do dicionário
    tabela = {chave: [] for chave in chaves}
    
    for i in range(1, len(linhas)):
        valores = linhas[i].strip().split(",") # obtém os valores da linha
        for j in range(len(chaves)):
            tabela[chaves[j]].append(valores[j]) # adiciona os valores à tabela
    
    return tabela

# Função que filtra a tabela
def filtrar_tabela(tabela, condicao):
    tabela_filtrada = {key: [] for key in tabela.keys()}
    for i in range(len(next(iter(tabela.values())))):
        if condicao({key: tabela[key][i] for key in tabela.keys()}):
            for key in tabela.keys():
                tabela_filtrada[key].append(tabela[key][i])
    return tabela_filtrada