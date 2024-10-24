import pandas as pd
import matplotlib.pyplot as plt

# Classe VendasEcommerce para manipulação dos dados de vendas
class VendasEcommerce:
    def __init__(self):
        self.dados = None
    
    # Método para carregar os dados do CSV
    def carregar_dados(self, caminho):
        self.dados = pd.read_csv(caminho, encoding='latin1')  # Usando 'latin1' para evitar problemas de codificação
    
    # Método para limpar os dados, removendo nulos e colunas que não são necessárias
    def limpar_dados(self):
        self.dados.drop(columns=['InvoiceNo', 'StockCode', 'CustomerID'], inplace=True, errors='ignore')
        self.dados.dropna(subset=['Description', 'UnitPrice'], inplace=True)
        self.dados = self.dados[self.dados['UnitPrice'] > 0]
    
    # Método para calcular o valor total por pedido
    def calcular_total_por_pedido(self):
        self.dados['TotalValue'] = self.dados['Quantity'] * self.dados['UnitPrice']

    # Método para calcular o lucro (usando um custo fictício)
    def calcular_lucro(self):
        custo_por_item = self.dados['UnitPrice'] * 0.7  # Supondo que o custo é 70% do preço unitário
        self.dados['Lucro'] = self.dados['TotalValue'] - (custo_por_item * self.dados['Quantity'])

    # Método para exibir as primeiras linhas dos dados
    def mostrar_dados(self):
        return self.dados

    # Método para gerar gráficos
    def gerar_graficos(self):
        # Gráfico 1: Total de vendas e lucro por produto
        vendas_e_lucro_por_produto = self.dados.groupby('Description').agg({'TotalValue': 'sum', 'Lucro': 'sum'}).sort_values(by='TotalValue', ascending=False).head(10)
        
        # Criando um gráfico de barras
        fig, ax1 = plt.subplots(figsize=(10, 5))

        vendas_e_lucro_por_produto['TotalValue'].plot(kind='bar', color='skyblue', ax=ax1, position=0, width=0.4, label='Total de Vendas')
        vendas_e_lucro_por_produto['Lucro'].plot(kind='bar', color='lightgreen', ax=ax1, position=1, width=0.4, label='Lucro')

        plt.title('Total de Vendas e Lucro por Produto (Top 10)')
        plt.xlabel('Produtos')
        plt.ylabel('Valores (R$)')
        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.tight_layout()
        plt.show()

        # Gráfico 2: Relação entre Preço Unitário e Quantidade Vendida
        plt.figure(figsize=(10, 5))
        plt.scatter(self.dados['UnitPrice'], self.dados['Quantity'], alpha=0.5, color='orange')
        plt.title('Relação entre Preço Unitário e Quantidade Vendida')
        plt.xlabel('Preço Unitário')
        plt.ylabel('Quantidade Vendida')
        plt.xlim(0, self.dados['UnitPrice'].max() + 5)
        plt.ylim(0, self.dados['Quantity'].max() + 5)
        plt.grid()
        plt.show()

# Instanciando a classe
vendas = VendasEcommerce()

# Carregando o dataset 'Online Retail.csv'
vendas.carregar_dados("online_retail.csv")

# Limpando os dados
vendas.limpar_dados()

# Calculando o valor total por pedido
vendas.calcular_total_por_pedido()

# Calculando o lucro
vendas.calcular_lucro()

# Exibindo as primeiras 100 linhas das colunas disponíveis
dados_filtrados = vendas.mostrar_dados()
print(dados_filtrados[['Description', 'UnitPrice', 'Quantity', 'TotalValue', 'Lucro']].head(100).to_string())

# Gerando gráficos
vendas.gerar_graficos()
