
import duckdb

con = duckdb.connect()

print("\n🟡 Consulta 1: Top 10 parlamentares")
q1 = """
SELECT txnomeparlamentar, vlrdocumento AS total_gasto
FROM 'data/gold/gastos_por_parlamentar.parquet'
ORDER BY total_gasto DESC
LIMIT 10
"""
print(con.execute(q1).fetchdf())

print("\n🔵 Consulta 2: Gastos por partido (2015–2023)")
q2 = """
SELECT sgpartido, ano, SUM(vlrdocumento) AS total
FROM 'data/gold/gastos_por_partido_ano.parquet'
WHERE ano BETWEEN 2015 AND 2023
GROUP BY sgpartido, ano
ORDER BY ano, total DESC
"""
print(con.execute(q2).fetchdf())

print("\n🟢 Consulta 3: Média de gastos por parlamentar")
q3 = """
SELECT AVG(vlrdocumento) AS media_gastos
FROM 'data/gold/gastos_por_parlamentar.parquet'
"""
print(con.execute(q3).fetchdf())
