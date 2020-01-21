import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('a5_ENERGIA.csv')

lista = df[0:10]
lista1 = df[131:142]
lista2 = df[0:30]

plt.subplot(2,2,3)
df.boxplot()
plt.title('Diagrama de caixa dos dados')
plt.ylabel('Energia consumida')
plt.grid(True)

plt.subplot(2,2,1)
plt.plot(lista.Ano, lista.Energia, 'y')
plt.xticks(lista.Ano, lista.Ano, rotation = 'vertical')
plt.title('Gráfico das 10 primeiras medidas')
plt.xlabel('Datas')
plt.ylabel('Energia consumida')
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(lista1.Ano, lista1.Energia, 'r--')
plt.xticks(lista1.Ano, lista1.Ano, rotation = 'vertical')
plt.title('Gráfico das 10 ultimas medidas')
plt.xlabel('Datas')
plt.ylabel('Energia consumida')
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(lista2.Ano, lista2.Energia, 'g')
plt.xticks(lista2.Ano, lista2.Ano, rotation = 'vertical')
plt.title('Gráfico das 30 primeiras medidas')
plt.xlabel('Datas')
plt.ylabel('Energia consumida')
plt.grid(True)

plt.subplots_adjust(wspace=0.3, hspace=0.8, top=0.95, bottom=0.2)

plt.show()