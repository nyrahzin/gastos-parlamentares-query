# 🧠 ETL - Gastos Parlamentares com DuckDB

Projeto acadêmico da disciplina de Business Intelligence — **LIBERTAS Faculdades Integradas**

---

## 🎯 Objetivo

Construir um pipeline ETL completo utilizando dados públicos de gastos dos deputados federais, organizando-os em camadas Bronze, Silver e Gold, e realizando consultas analíticas com **DuckDB**.

---

## 🔗 Link do notebook no Google Colab

📎 [Clique aqui para visualizar o ETL no Colab](https://colab.research.google.com/drive/11XTp1dWpWW1SkONgZX1TLANOAwIoA4oh?usp=sharing)

---

## 🧱 Camadas do ETL

- **Bronze**: dados brutos do Brasil.io (.parquet)
- **Silver**: dados limpos, normalizados e padronizados
- **Gold**: dados agregados por parlamentar e partido

---

## 📊 Consultas com DuckDB

As consultas estão no script [`consultas_duckdb.py`](./consultas_duckdb.py), com análises como:

1. Top 10 parlamentares que mais gastaram
2. Gastos por partido entre 2015 e 2023
3. Média de gastos por parlamentar

---

## ⚠️ Observação

Os arquivos `.parquet` das camadas Bronze, Silver e Gold **não foram incluídos** neste repositório devido ao limite de 100 MB por arquivo do GitHub.

📌 Todos esses arquivos podem ser **regenerados automaticamente** executando o notebook [`etl_pipeline.ipynb`](./etl_pipeline.ipynb) no Colab.

---

## 📁 Estrutura do projeto

projeto_etl_duckdb/
├── data/
│ ├── bronze/ ← arquivos brutos (.parquet)
│ ├── silver/ ← dados tratados
│ └── gold/ ← dados agregados para análise
├── consultas_duckdb.py
├── etl_pipeline.ipynb
└── README.md

yaml
Copiar
Editar

---

## 🎥 Apresentação

📹 Link para o vídeo explicando o projeto (YouTube):  
👉 _[colar aqui o link do vídeo]_
