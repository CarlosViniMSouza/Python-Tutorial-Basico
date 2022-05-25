# Classificador Naive Bayes:
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import random
import pandas as pd
import numpy as np

random.seed(42)
data = pd.read_csv('code\sessao02\example\Iris.csv', header=0)
data = data.dropna(axis='rows')

classes = np.array(pd.unique(data[data.columns[-1]]), dtype=str)

print("\nNum. Linhas & Colunas da Matriz de Atributos: ", data.shape)
# output: Num. Linhas & Colunas da Matriz de Atributos:  (150, 6)

attributes = list(data.columns)
data = data.to_numpy()
nrow, ncol = data.shape
y = data[:, -1]
X = data[:, 0:ncol-1]

# Selecionando os conjuntos de Treino e Teste:

p = 0.7
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=p, random_state=42)

# Classificacao: implementacao do Metodo:


def likelyhood(y, Z):

    def gaussian(x, mu, sig):
        return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

    prob = 1
    for j in np.arange(0, Z.shape[1]):
        m = np.mean(Z[:, j])
        s = np.std(Z[:, j])
        prob = prob*gaussian(y[j], m, s)
    return prob


# Estimacao de cada classe:

P = pd.DataFrame(data=np.zeros(
    (X_test.shape[0], len(classes))), columns=classes)

for i in np.arange(0, len(classes)):
    elements = tuple(np.where(y_train == classes[i]))
    Z = X_train[elements, :][0]
    for j in np.arange(0, X_test.shape[0]):
        x = X_test[j, :]
        pj = likelyhood(x, Z)
        P[classes[i]][j] = pj*len(elements)/X_train.shape[0]

# Para as observações no conjunto de teste, a probabilidade pertencer a cada classe:
print("\n", P.head(10))
"""
output:

      Iris-setosa  Iris-versicolor  Iris-virginica
0   2.203966e-92     4.345947e-03    8.401969e-08
1   1.479191e-04     7.322596e-20    5.675329e-35
2  3.574579e-294     6.684121e-19    2.223171e-05
3   7.304744e-96     4.012212e-03    1.424931e-06
4  1.666488e-108     8.057105e-04    1.410390e-06
5   1.405723e-03     6.169399e-17    9.013438e-32
6   8.718053e-55     2.340174e-03    4.316097e-11
7  2.564878e-183     6.862286e-14    1.482946e-03
8   9.841417e-98     7.266205e-04    6.224668e-09
9   1.520404e-62     6.288432e-03    1.024099e-08
"""

y_pred = []
for i in np.arange(0, P.shape[0]):
    c = np.argmax(np.array(P.iloc[[i]]))
    y_pred.append(P.columns[c])

y_pred = np.array(y_pred, dtype=str)
score = accuracy_score(y_pred, y_test)
print("\n", 'Acuracia apontada: ', score)
# output: Acuracia apontada:  1.0

"""
Resumo da Opera:

1 - Tratamos colunas como listas, e utilizamos métodos de listas.
2 - Usamos funções para fazer o cálculo de Naive Bayes Gaussiano.

E lembrando, os 2 códigos foram utilizados em cursos FIC, por isso é importante
aprender um pouco de listas, dicionarios e funções (cedo ou tarde, será necessário!)

Então ... Te cuida caboco(a)!!
"""
