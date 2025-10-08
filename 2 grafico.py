import matplotlib.pyplot as plt
import numpy as np

# Dados (prejuízos em valores negativos)
transportadoras = ["J&T", "TEX"]
q1 = [-5535.46, -42875.06]
q2 = [-6467.57, 961.29]

x = np.arange(len(transportadoras))
largura = 0.35

fig, ax = plt.subplots(figsize=(8,6))

# Barras negativas
b1 = ax.bar(x - largura/2, q1, largura, label="1ª Quinzena Agosto", color="#d9534f")
b2 = ax.bar(x + largura/2, q2, largura, label="1ª Quinzena Setembro", color="#f0ad4e")

# Títulos e eixos
ax.set_title("Comparação de desvio: 1Q Agosto x 1Q Setembro", fontsize=14, weight="bold")
ax.set_xticks(x)
ax.set_xticklabels(transportadoras)
ax.set_ylabel("Valor (R$)")
ax.legend()

# Linha de zero para referência
ax.axhline(0, color="black", linewidth=0.8)

# Inserir rótulos nos dados
for barras in [b1, b2]:
    for barra in barras:
        altura = barra.get_height()
        ax.annotate(f'R$ {abs(altura):,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."),
                    xy=(barra.get_x() + barra.get_width()/2, altura),
                    xytext=(0, -5),
                    textcoords="offset points",
                    ha='center', va='top', fontsize=10, color="black", weight="bold")

plt.tight_layout()

# Salvar em PNG com alta qualidade
plt.savefig("prejuizo_transportadoras.png", dpi=300, bbox_inches="tight")

plt.show()