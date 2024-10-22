import pandas as pd

# Classe VendasEcommerce para manipulação dos dados de vendas
class VendasEcommerce:
    def __init__(self):
        self.dados = None
    
    # Método para carregar os dados do CSV
    def carregar_dados(self, caminho):
        self.dados = pd.read_csv(caminho)
    
    # Método para limpar os dados, removendo nulos e ajustando tipos
    def limpar_dados(self):
        self.dados.dropna(inplace=True)
        # Ajuste tipos para colunas específicas, se necessário
        if 'preco_venda' in self.dados.columns and 'custo' in self.dados.columns:
            self.dados['preco_venda'] = pd.to_numeric(self.dados['preco_venda'], errors='coerce')
            self.dados['custo'] = pd.to_numeric(self.dados['custo'], errors='coerce')

    # Método para filtrar os dados por categoria de produto
    def filtrar_categoria(self, categoria):
        return self.dados[self.dados['categoria'] == categoria]
    
    # Método para filtrar os dados por região
    def filtrar_regiao(self, regiao):
        return self.dados[self.dados['regiao'] == regiao]
    
    # Método para calcular o lucro por pedido
    def calcular_lucro(self):
        if 'preco_venda' in self.dados.columns and 'custo' in self.dados.columns:
            self.dados['lucro'] = self.dados['preco_venda'] - self.dados['custo']
    
    # Método para exibir as primeiras linhas dos dados
    def mostrar_dados(self):
        return self.dados.head()

# Instanciando a classe
vendas = VendasEcommerce()

# Carregando o dataset 'amazon.csv' (ajuste o caminho conforme necessário)
vendas.carregar_dados("amazon.csv")

# Limpando os dados
vendas.limpar_dados()

# Calculando o lucro
vendas.calcular_lucro()

# Exemplo: Filtrando por categoria 'eletrônicos'
dados_filtrados_categoria = vendas.filtrar_categoria("eletrônicos")

# Exemplo: Filtrando por região 'sul'
dados_filtrados_regiao = vendas.filtrar_regiao("sul")

# Exibindo os dados filtrados
print(vendas.mostrar_dados())
