
#? No terminal:
#? pip install matplotlib numpy --user    (Sem o '--user' não funcionou no vscode)

#! Exemplo de importação de uma biblioteca externa

import matplotlib.pyplot as plt
import numpy as np

#* Gera valores para x
x = np.linspace(-10, 10, 400)

#* Calcula y = x^2 para cada valor de x
y = x**2

#* Cria o gráfico
plt.plot(x, y, label='y = x^2')
plt.title('Gráfico de y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

#* Mostra o gráfico
plt.show()