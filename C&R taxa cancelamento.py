import pandas as pd
import glob

# Caminho da pasta com os arquivos
pasta = r'C:\Users\lucas.araujo\Downloads\Compre E Retire\*.xlsx'

# Lista de arquivos
arquivos = glob.glob(pasta)

# Lista para armazenar os DataFrames
df_list = []

# Lê cada arquivo da pasta e adiciona na lista
for arquivo in arquivos:
    df_temp = pd.read_excel(arquivo)
    df_list.append(df_temp)

# Concatena todos os arquivos em um único DataFrame
df = pd.concat(df_list, ignore_index=True)

# Filtra os pedidos cancelados
cancelados = df[df['Status'] == 'Cancelado']

# Total de pedidos por Courrier
total_pedidos = df.groupby('Courrier')['Order'].count()

# Total de pedidos cancelados por Courrier
total_cancelados = cancelados.groupby('Courrier')['Order'].count()

# Junta as informações em um DataFrame
relatorio = pd.DataFrame({
    'Total_Pedidos': total_pedidos,
    'Cancelados': total_cancelados
})

# Substitui NaN por 0 nos cancelados
relatorio['Cancelados'] = relatorio['Cancelados'].fillna(0).astype(int)

# Calcula o percentual de cancelamento com 2 casas decimais
relatorio['Percentual_Cancelamento'] = ((relatorio['Cancelados'] / relatorio['Total_Pedidos']) * 100).round(2)

# Organiza o relatório
relatorio = relatorio.sort_values(by='Percentual_Cancelamento', ascending=False)

# Salva o resumo simples
relatorio.to_excel(r'C:\Users\lucas.araujo\Downloads\Compre E Retire\relatorio_resumo.xlsx')

# Salva o relatório completo com duas abas: Resumo + Base de dados
with pd.ExcelWriter(r'C:\Users\lucas.araujo\Downloads\Compre E Retire\relatorio_completo.xlsx') as writer:
    relatorio.to_excel(writer, sheet_name='Resumo')
    df.to_excel(writer, sheet_name='Base_Completa', index=False)

print("Relatórios gerados com sucesso.")
