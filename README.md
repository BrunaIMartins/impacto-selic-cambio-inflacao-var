# impacto-selic-cambio-inflacao-var
Este projeto analisa a relação dinâmica entre a taxa de juros, a taxa de câmbio e a inflação no Brasil, utilizando técnicas de séries temporais e econometria aplicada.

🎯 Objetivo

O objetivo deste estudo é avaliar como variações na taxa de juros (Selic) impactam o comportamento da inflação (IPCA) e da taxa de câmbio (R$/US$) ao longo do tempo.

Busca-se:

Analisar os efeitos de choques na taxa de juros
Investigar relações de longo prazo entre variáveis macroeconômicas
Compreender os mecanismos de transmissão da política monetária
📊 Dados

Foram utilizadas séries temporais mensais:

Taxa de câmbio (R$/US$ – média mensal)
Inflação (IPCA – variação mensal)
Taxa de juros (Selic – acumulada no mês)

Fontes:

Banco Central do Brasil (BCB)
IPEA Data

🧠 Metodologia

O projeto segue um pipeline econométrico padrão:

1. Transformação dos dados por logaritmização das variáveis
2. Análise exploratória
- Visualização das séries temporais
- Identificação de tendências e volatilidade
3. Busca por quebras estruturais por Teste de Bai-Perron (via biblioteca ruptures)
4. Teste de raiz unitária por Dickey-Fuller Aumentado (ADF)
5. Teste de cointegração por Teste de Johansen
7. Modelagem econométrica pelo modelo de Vetores Autorregressivos (VAR)
Análise da dinâmica entre as variáveis

🛠️ Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels
- Ruptures
