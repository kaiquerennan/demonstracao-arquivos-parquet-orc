# Comparação de Formatos de Arquivos: Parquet vs ORC

Este repositório contém o código utilizado em uma apresentação na **Universidade Federal de Ouro Preto (UFOP)**, que compara os formatos de arquivos **CSV**, **Parquet** e **ORC**, com foco em suas características de **desempenho**, **compressão** e **eficiência no armazenamento de dados**.

---

## Objetivo

- Avaliar a performance de leitura e escrita de dados em **Parquet** e **ORC**.
- Comparar a eficiência na **compressão de dados**.
- Analisar a **eficiência de armazenamento** para diferentes volumes de dados.

---

## Pré-requisitos

- Python 3.8+
- Bibliotecas Python:
  - `random`
  - `csv`
  - `time` (para medição de performance)
- Apache Spark (para manipulação de DataFrames e conversão entre formatos Parquet e ORC)
- Hadoop HDFS (para armazenamento distribuído e leitura/escrita dos arquivos)
