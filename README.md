# 🛠 Rinha de Dados - Desafio de Engenharia de Dados

## 🎯 Objetivo

**Criar um pipeline de dados completo para rastreamento e análise de pedidos de e-commerce em tempo real e/ou em batch, com foco em eficiência, escalabilidade e capacidade analítica.**

---

## 🏃‍♂️ Desafio Proposto

Desenvolver um sistema capaz de:

* Ingerir eventos de pedidos (bach e/ou streaming)
* Realizar transformações e agregações
* Armazenar dados otimizados para consulta
* Disponibilizar uma interface de consulta SQL ou dashboard
* Exibir métricas de performance e uso de recursos

---

## 📦 Entradas de Dados

### 1. Stream de Eventos de Pedidos (`order_events.jsonl`)

Arquivo no formato JSON Lines com eventos como:

* `ORDER_CREATED`
* `PAYMENT_CONFIRMED`
* `ORDER_PACKED`
* `ORDER_SHIPPED`
* `ORDER_DELIVERED` (X% com `is_delayed = true`)
* `ORDER_RETURNED` (X% com `is_returned = true`)

### 2. Catálogo de Produtos (CSV)
```python
# Schema do arquivo
product_id,
product_name,
category,
price
```

---

## ✅ Requisitos Funcionais

1. **Ingestão de dados**

   * Streaming (ferramentas livres)
   * Batch com leitura de arquivos estáticos (ferramentas livres)

2. **Transformações e Agregações**

   * Total de pedidos por região e categoria
   * Tempo médio do ciclo de vida do pedido (criação até entrega)
   * Percentual de devoluções por categoria e região
   * Percentual de entregas com atraso de entrega categoria e região
   * Peso em percentual das vendas por região

3. **Armazenamento**

   * Formato columnar (ferramentas livres)
   * Suporte a consultas analíticas SQL/OLAP

4. **Consulta e Visualização**

   * Engine/Interface SQL (ferramentas livres)
   * Dashboard ou notebook (ferramentas livres)

---

## 📂 Entrega Esperada

* `docker-compose.yml` com os serviços necessários
* Scripts de setup e execução
* Código do pipeline (ETL/ELT)
* Documentação:

  * Arquitetura da solução
  * Instruções de execução
  * Métricas de performance (tempo de ingestão, transformação e consulta)
* Exemplo de consultas ou dashboard

---

## 🛠️ Ferramentas Livres, cabe a você coloca-las em seus

Kafka, Spark Structured Streaming, Delta Lake, Airbyte, Nifi,
Spark, dbt, Flink, Python, Flink, Apache Iceberg, Postgres,
DuckDB, BigQuery, Redshift, Athena, Synapse Analytics, Dataform,
Trino, Superset, Metabase, DuckDB, Notebooks, Airflow, S3,
Glue, Step Functions, Azure Data Factory, Synapse Pipelines,
MinIO, Docker, Pub/Sub, Dataflow, Kinesis, Lambda, Event Hubs,
Stream Analytics, Glue Catalog, Hive.

---

## 🔢 Critérios de Avaliação

| Critério                                                              | Peso  |
| --------------------------------------------------------------------- | ----- |
| **Escalabilidade** (capacidade de lidar com grandes volumes de dados) | ⭐⭐⭐⭐☆ |
| Eficiência do pipeline (latência, throughput)                         | ⭐⭐⭐⭐☆ |
| Clareza da arquitetura e do código                                    | ⭐⭐⭐⭐☆ |
| Qualidade das transformações / métricas                               | ⭐⭐⭐☆☆ |
| Armazenamento otimizado para OLAP                                     | ⭐⭐⭐☆☆ |
| Facilidade de consulta / visualização                                 | ⭐⭐☆☆☆ |
| Criatividade e boas práticas                                          | ⭐⭐☆☆☆ |


---

Vamos ver quem constrói o pipeline mais inteligente, performático e elegante. 🚀🚀

**Boa sorte, e que vença o melhor pipeline!**
