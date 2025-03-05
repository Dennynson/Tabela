# Desenvolvedor: Dennynson Scheydt (20240010564)

from table import *

# Exemplo de criação de tabela
colunas = ["nome", "idade"]
valores = [["João", 25], ["Maria", 30], ["Pedro", 22]]
tabela = criar_tabela(colunas, valores)

# Exibindo a tabela inicial
print("Tabela inicial:")
exibir_tela(tabela)

# Adicionando uma linha
adicionar_linha(tabela, ["ana", 20])
print("\nTabela após adicionar uma linha:")
exibir_tela(tabela)

# Removendo uma linha
remover_linha(tabela, 2)  # Remove a segunda linha (índice 1)
print("\nTabela após remover uma linha:")
exibir_tela(tabela)

# Adicionando uma coluna
adicionar_coluna(tabela, "cidade", ["SP", "RJ", "MG"])
print("\nTabela após adicionar uma coluna:")
exibir_tela(tabela)

# Removendo uma coluna
remover_coluna(tabela, "cidade")
print("\nTabela após remover a coluna 'cidade':")
exibir_tela(tabela)

# Somando os valores das colunas
soma = soma_colunas(tabela)
print("\nSomas das colunas numéricas:", soma)

# Calculando a média das colunas
media = media_colunas(tabela)
print("\nMédias das colunas numéricas:", media)

tabela_csv = nova_tabela("exemplo.csv")
print("\nTabela carregada do CSV:")
exibir_tela(tabela_csv)

def condicao(linha):
    return linha["idade"] > 23 # Filtrando linhas onde a idade é maior que 23

filtrada = filtrar_tabela(tabela, condicao)
print("\nTabela filtrada para idades maiores que 23:")
exibir_tela(filtrada)