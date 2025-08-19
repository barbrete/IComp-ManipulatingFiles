# Controle de Itens de Frota de Veículos

## Problema

Empresas que disponibilizam veículos para seus colaboradores frequentemente enfrentam dificuldades para controlar o uso desses bens. A falta de um registro detalhado pode gerar prejuízos financeiros, uso indevido dos veículos, dificuldade no acompanhamento de custos, manutenção e depreciação. Para resolver esse problema, é fundamental criar uma base de dados que registre informações relevantes sobre cada veículo, como nome/descrição, quantidade, mês da aquisição, valor, colaborador responsável, quilometragem e datas de uso.

## Objetivo

Desenvolver uma solução que:
- Gere um arquivo CSV com os dados dos veículos da empresa.
- Carregue esses dados em uma estrutura de dados (lista ou DataFrame).
- Apresente os seguintes resultados:
  - O item mais caro (nome/descrição e valor).
  - O item mais barato (nome/descrição e valor).
  - Estatísticas dos valores dos itens: média e mediana.

## Exemplo de Estrutura da Tabela

| Descrição      | Quantidade | Mês da Aquisição | Valor    | Colaborador | Quilometragem Inicial | Quilometragem Final | Data de Retirada | Data de Devolução |
|----------------|------------|------------------|----------|-------------|----------------------|--------------------|------------------|-------------------|
| FIAT Uno       | 1          | 04/2025          | 65000.00 | João        | 12000                | 12500              | 10/08/2025       | 10/08/2025        |



## Passos do Projeto

1. **Geração do arquivo CSV:**  
   Os dados dos veículos são salvos em um arquivo chamado `ControleCarros.csv`.

2. **Leitura dos dados:**  
   O arquivo CSV é carregado em um DataFrame do pandas para facilitar a manipulação e análise.

3. **Apresentação dos resultados:**  
   - Exibição da tabela e das primeiras 5 linhas.
   - Exibição do carro mais caro e mais barato, com nome/descrição e valor.
   - Cálculo e exibição da média e mediana dos valores dos veículos.

## Resultados Esperados

- **Item mais caro:**  
  Exemplo: Honda Fit — R$ 71.000,00

- **Item mais barato:**  
  Exemplo: Ford Ka — R$ 47.000,00

- **Média dos valores:**  
  Exemplo: R$ 59.800

- **Mediana dos valores:**  
  Exemplo: R$ 60.500

## Como executar

1. Certifique-se de ter Python e as bibliotecas `pandas` e `numpy` instaladas.
2. Execute o script principal (`ManipulatingFiles.py`).
3. Veja os resultados no terminal.

---

Sinta-se à vontade para adaptar a estrutura para outros tipos de itens, como produtos de supermercado, papelaria, imóveis, etc. O importante é manter os campos principais: nome/descrição, quantidade, mês da aquisição e valor.
