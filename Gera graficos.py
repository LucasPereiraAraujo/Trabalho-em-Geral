import matplotlib.pyplot as plt
import numpy as np
import locale

# Configura formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Para Windows use 'Portuguese_Brazil.1252'

# =====================
# Dados
# =====================
# J&T
jt_custo = 58041.69
jt_receita = 51574.12
jt_frete_tabelado = 55714.27

jt_amazon_custo = 6637.74
jt_amazon_receita = 8610.90
jt_amazon_frete_tabelado = 6235.52

jt_outros_custo = jt_custo - jt_amazon_custo
jt_outros_receita = jt_receita - jt_amazon_receita
jt_outros_frete_tabelado = jt_frete_tabelado - jt_amazon_frete_tabelado

# TEX
tex_custo = 24731.9
tex_receita = 25693.19
tex_frete_tabelado = 33852.27

tex_outros_custo = tex_custo
tex_outros_receita = tex_receita
tex_outros_frete_tabelado = tex_frete_tabelado

# =====================
# Paleta sofisticada Data Storytelling
# =====================
colors = {
    "custo": "#E4572E",    # vermelho
    "receita": "#1F77B4",  # azul
    "resultado": "#2CA02C",# verde
    "frete": "#FF7F0E"     # laranja
}

# Função para formatar valor em R$ brasileiro
def format_brl(value):
    return f"R$ {locale.format_string('%.2f', value, grouping=True)}"

# =====================
# Função de anotação sofisticada
# =====================
def annotate_bars(bars, offset_factor=0.02):
    for bar in bars:
        yval = bar.get_height()
        if yval >=0:
            va = "bottom"
            offset = max_val * offset_factor
        else:
            va = "top"
            offset = -max_val * offset_factor
        plt.text(bar.get_x() + bar.get_width()/2, yval + offset, format_brl(yval),
                 ha="center", va=va, fontweight="bold", fontsize=10)

# =====================
# 1 - Visão Financeira Geral
# =====================
labels = ["J&T", "TEX"]
custos = [jt_custo, tex_custo]
receitas = [jt_receita, tex_receita]
resultados = [jt_receita - jt_custo, tex_receita - tex_custo]

x = np.arange(len(labels))
width = 0.2

plt.figure(figsize=(10,6))
bars_custo = plt.bar(x - width, custos, width, label="Custo", color=colors["custo"], edgecolor="gray", alpha=0.9)
bars_receita = plt.bar(x, receitas, width, label="Receita", color=colors["receita"], edgecolor="gray", alpha=0.9)
bars_resultado = plt.bar(x + width, resultados, width, 
                         label="Resultado", 
                         color=[colors["resultado"] if v>=0 else "#8B0000" for v in resultados],
                         edgecolor="gray", alpha=0.9)

plt.xticks(x, labels, fontsize=11)
plt.ylabel("R$ (reais)", fontsize=11)
plt.title("Visão Financeira Geral - Resultado para Baixo se Negativo", fontsize=14, fontweight="bold")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.4)

max_val = max(custos + receitas)
y_min = min(0, min(resultados)*1.2)
y_max = max(custos + receitas)*1.15
plt.ylim(y_min, y_max)

for bars in [bars_custo, bars_receita, bars_resultado]:
    annotate_bars(bars)

plt.tight_layout()
plt.savefig("visao_financeira_geral.png", dpi=300)
plt.show()

# =====================
# 2 - Visão Amazon (somente J&T)
# =====================
labels = ["J&T Amazon"]
valores_custo = [jt_amazon_custo]
valores_receita = [jt_amazon_receita]
valores_frete = [jt_amazon_frete_tabelado]

x = np.arange(len(labels))
width = 0.2
plt.figure(figsize=(7,5))
bars_custo = plt.bar(x - width, valores_custo, width, label="Custo", color=colors["custo"], edgecolor="gray", alpha=0.9)
bars_receita = plt.bar(x, valores_receita, width, label="Receita", color=colors["receita"], edgecolor="gray", alpha=0.9)
bars_frete = plt.bar(x + width, valores_frete, width, label="Frete Tabelado", color=colors["frete"], edgecolor="gray", alpha=0.9)

plt.xticks(x, labels, fontsize=11)
plt.ylabel("R$ (reais)", fontsize=11)
plt.title("Visão Amazon - J&T", fontsize=14, fontweight="bold")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.3)

max_val = max(valores_custo + valores_receita + valores_frete)
plt.ylim(0, max_val*1.15)

for bars in [bars_custo, bars_receita, bars_frete]:
    annotate_bars(bars, offset_factor=0.015)

plt.tight_layout()
plt.savefig("visao_amazon_jt.png", dpi=300)
plt.show()

# =====================
# 3 - Visão Outros Métodos de Envio
# =====================
labels = ["J&T Outros", "TEX Outros"]
custos = [jt_outros_custo, tex_outros_custo]
receitas = [jt_outros_receita, tex_outros_receita]
frete = [jt_outros_frete_tabelado, tex_outros_frete_tabelado]

x = np.arange(len(labels))
width = 0.2
plt.figure(figsize=(10,6))
bars_custo = plt.bar(x - width, custos, width, label="Custo", color=colors["custo"], edgecolor="gray", alpha=0.9)
bars_receita = plt.bar(x, receitas, width, label="Receita", color=colors["receita"], edgecolor="gray", alpha=0.9)
bars_frete = plt.bar(x + width, frete, width, label="Frete Tabelado", color=colors["frete"], edgecolor="gray", alpha=0.9)

plt.xticks(x, labels, fontsize=11)
plt.ylabel("R$ (reais)", fontsize=11)
plt.title("Visão Outros Métodos de Envio - J&T e TEX", fontsize=14, fontweight="bold")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.3)

max_val = max(custos + receitas + frete)
plt.ylim(0, max_val*1.15)

for bars in [bars_custo, bars_receita, bars_frete]:
    annotate_bars(bars, offset_factor=0.02)

plt.tight_layout()
plt.savefig("visao_outros_metodos.png", dpi=300)
plt.show()

   # =====================
# 4 - Visão J&T - Filial 901 (Ecommerce BH)
# =====================
# <<< Substitua os valores abaixo pelos reais da filial 901 >>>
jt_901_custo = 1264.28
jt_901_receita = 735.33
jt_901_frete_tabelado = 1230.01 # coloque o valor correto se tiver, senão pode deixar 0 ou remover

labels = ["J&T 901 - Ecommerce BH"]
valores_custo = [jt_901_custo]
valores_receita = [jt_901_receita]
valores_frete = [jt_901_frete_tabelado]

x = np.arange(len(labels))
width = 0.25
plt.figure(figsize=(7,5))

bars_custo = plt.bar(x - width, valores_custo, width, label="Custo", 
                     color=colors["custo"], edgecolor="gray", alpha=0.9)
bars_receita = plt.bar(x, valores_receita, width, label="Receita", 
                       color=colors["receita"], edgecolor="gray", alpha=0.9)
bars_frete = plt.bar(x + width, valores_frete, width, label="Frete Tabelado", 
                     color=colors["frete"], edgecolor="gray", alpha=0.9)

plt.xticks(x, labels, fontsize=11)
plt.ylabel("R$ (reais)", fontsize=11)
plt.title("Visão Filial 901 - J&T Ecommerce BH", fontsize=14, fontweight="bold")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.3)

max_val = max(valores_custo + valores_receita + valores_frete)
plt.ylim(0, max_val*1.15)

for bars in [bars_custo, bars_receita, bars_frete]:
    annotate_bars(bars, offset_factor=0.02)

plt.tight_layout()
plt.savefig("visao_jt_901.png", dpi=300)
plt.show()
