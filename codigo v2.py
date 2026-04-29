import pandas as pd   ##aqui começa a logaritimização
import numpy as np

# carregando arquivo Excel
df = pd.read_excel("dados.xlsx")

# log do câmbio (np.log por ser valor em reais)
df["log_cambio"] = np.log(df["cambio"])

# log das taxas (np.log1p oir ser em %)
df["log_ipca"] = np.log1p(df["ipca"] / 100)
df["log_selic"] = np.log1p(df["selic"] / 100)

print(df.head())

############################################################################################

import pandas as pd

# selecionar colunas
tabela = df[["log_cambio", "log_ipca", "log_selic"]]

# salvar como Excel
tabela.to_excel("tabela_log.xlsx", index=False)

########################################################################################

import matplotlib.pyplot as plt  #aqui começam os gráficos

# Log câmbio
plt.figure()
plt.plot(df["log_cambio"])
plt.title("Log Câmbio")
plt.show()

# Log IPCA
plt.figure()
plt.plot(df["log_ipca"])
plt.title("Log IPCA")
plt.show()

# Log Selic
plt.figure()
plt.plot(df["log_selic"])
plt.title("Log Selic")
plt.show()

#################################################################################################
import matplotlib.pyplot as plt  #aqui começa o Bai Perron para cambio
import ruptures as rpt

# escolha da série (ex: log_cambio)
serie = df["log_cambio"].values

# modelo (l2 = mudanças na média)
model = "l2"

# aplicar algoritmo
algo = rpt.Binseg(model=model).fit(serie)

# definir número de quebras (ajuste conforme necessário)
n_quebras = 5
# detectar quebras
breaks = algo.predict(n_bkps=n_quebras)

print("Pontos de quebra:", breaks)

# gráfico
rpt.display(serie, breaks)
plt.title("Quebras Estruturais no Câmbio - Bai-Perron")
plt.show()

#################################################################################################
import matplotlib.pyplot as plt  #aqui começa o Bai Perron para ipca
import ruptures as rpt

# escolha da série (ex: log_ipca)
serie = df["log_ipca"].values

# modelo (l2 = mudanças na média)
model = "l2"

# aplicar algoritmo
algo = rpt.Binseg(model=model).fit(serie)

# definir número de quebras (ajuste conforme necessário)
n_quebras = 5
# detectar quebras
breaks = algo.predict(n_bkps=n_quebras)

print("Pontos de quebra:", breaks)

# gráfico
rpt.display(serie, breaks)
plt.title("Quebras Estruturais no IPCA - Bai-Perron")
plt.show()

#################################################################################################
import matplotlib.pyplot as plt  #aqui começa o Bai Perron para selic
import ruptures as rpt

# escolha da série (ex: log_selic)
serie = df["log_selic"].values

# modelo (l2 = mudanças na média)
model = "l2"

# aplicar algoritmo
algo = rpt.Binseg(model=model).fit(serie)

# definir número de quebras (ajuste conforme necessário)
n_quebras = 5
# detectar quebras
breaks = algo.predict(n_bkps=n_quebras)

print("Pontos de quebra:", breaks)

# gráfico
rpt.display(serie, breaks)
plt.title("Quebras Estruturais na Selic - Bai-Perron")
plt.show()

###################################################################

from statsmodels.tsa.stattools import adfuller ###raiz unitária

# lista de variáveis
variaveis = ["log_cambio", "log_ipca", "log_selic"]

for var in variaveis:
    serie = df[var].dropna()
    
    resultado = adfuller(serie)
    
    print(f"\n=== {var} ===")
    print(f"Estatística ADF: {resultado[0]:.4f}")
    print(f"p-valor: {resultado[1]:.4f}")
    print("Valores críticos:")
    
    for chave, valor in resultado[4].items():
        print(f"   {chave}: {valor:.4f}")
    
    # interpretação automática
    if resultado[1] < 0.05:
        print("→ Série estacionária (rejeita H0)")
    else:
        print("→ Série não estacionária (não rejeita H0)")
        
    ###########################################################################
    from statsmodels.tsa.vector_ar.vecm import coint_johansen

# selecionar variáveis
dados = df[["log_cambio", "log_ipca", "log_selic"]].dropna()

# aplicar teste de Johansen
resultado = coint_johansen(dados, det_order=0, k_ar_diff=1)

# estatísticas trace
print("Estatística Trace:")
print(resultado.lr1)

# valores críticos
print("\nValores críticos (90%, 95%, 99%):")
print(resultado.cvt)

# interpretação automática
for i in range(len(resultado.lr1)):
    stat = resultado.lr1[i]
    crit_5 = resultado.cvt[i, 1]
    
    print(f"\nH0: r <= {i}")
    print(f"Estatística: {stat:.2f}")
    print(f"Crítico 5%: {crit_5}")
    
    if stat > crit_5:
        print("→ Rejeita H0 → há cointegração")
    else:
        print("→ Não rejeita H0")