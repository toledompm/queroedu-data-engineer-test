# QueroEdu Data Engineer Test

O teste consistia em:

- Resgatar dados de um endpoint
- Tratar e inserir os dados em um banco relacional

## Setup

Instale as dependencias: `make install-deps`

Suba o container do banco (O diretorio `./db/setup/` esta mapeado para o container, arquivos `.sql` serao executados na inicializacao do container): `make up`

Renomeie o arquivo `.env.example` para `.env` e preencha o campo `URL`

## Running

Primeira execucao:
`python3 main.py -f`

A flag `-f ou --fetch` enviara uma requisicao get para a url setada no `.env`. E salvara o resultado em um arquivo `resp.json`. As execucoes seguintes podem emitir a flag, o script usara o arquivo.

# Index comparissons

## Secao

```
create index on contract (secao)
```

no index:

```
de_test=# explain analyze select co.salario, ci.uf from contract co inner join cities ci on co.city_id = ci.city_id where secao = 'N';
                                                      QUERY PLAN
----------------------------------------------------------------------------------------------------------------------
 Hash Join  (cost=59.88..716.31 rows=3888 width=8) (actual time=3.260..15.238 rows=3897 loops=1)
   Hash Cond: (co.city_id = ci.city_id)
   ->  Seq Scan on contract co  (cost=0.00..646.20 rows=3888 width=8) (actual time=0.040..10.100 rows=3897 loops=1)
         Filter: (secao = 'N'::bpchar)
         Rows Removed by Filter: 18439
   ->  Hash  (cost=33.28..33.28 rows=2128 width=8) (actual time=3.086..3.088 rows=2128 loops=1)
         Buckets: 4096  Batches: 1  Memory Usage: 116kB
         ->  Seq Scan on cities ci  (cost=0.00..33.28 rows=2128 width=8) (actual time=0.036..1.369 rows=2128 loops=1)
 Planning Time: 0.885 ms
 Execution Time: 15.655 ms
(10 rows)

```

with index:

```
de_test=# explain analyze select co.salario, ci.uf from contract co inner join cities ci on co.city_id = ci.city_id where secao = 'N';
                                                               QUERY PLAN
----------------------------------------------------------------------------------------------------------------------------------------
 Hash Join  (cost=138.30..564.13 rows=3888 width=8) (actual time=4.336..8.502 rows=3897 loops=1)
   Hash Cond: (co.city_id = ci.city_id)
   ->  Bitmap Heap Scan on contract co  (cost=78.42..494.02 rows=3888 width=8) (actual time=1.114..3.038 rows=3897 loops=1)
         Recheck Cond: (secao = 'N'::bpchar)
         Heap Blocks: exact=367
         ->  Bitmap Index Scan on contract_secao_idx  (cost=0.00..77.45 rows=3888 width=0) (actual time=1.033..1.033 rows=3897 loops=1)
               Index Cond: (secao = 'N'::bpchar)
   ->  Hash  (cost=33.28..33.28 rows=2128 width=8) (actual time=3.089..3.090 rows=2128 loops=1)
         Buckets: 4096  Batches: 1  Memory Usage: 116kB
         ->  Seq Scan on cities ci  (cost=0.00..33.28 rows=2128 width=8) (actual time=0.043..1.324 rows=2128 loops=1)
 Planning Time: 0.766 ms
 Execution Time: 8.948 ms
(12 rows)
```

## Cidade

without index

```
de_test=# explain analyze select city_id from cities where municipio = 421580 and uf = 42 and regiao = 4;
                                           QUERY PLAN
-------------------------------------------------------------------------------------------------
 Seq Scan on cities  (cost=0.00..49.24 rows=1 width=4) (actual time=0.064..0.865 rows=1 loops=1)
   Filter: ((municipio = 421580) AND (uf = 42) AND (regiao = 4))
   Rows Removed by Filter: 2127
 Planning Time: 0.182 ms
 Execution Time: 0.904 ms
(5 rows)
```

with index

```
de_test=# explain analyze select city_id from cities where municipio = 330455 and uf = 33 and regiao = 3;
                                                              QUERY PLAN
---------------------------------------------------------------------------------------------------------------------------------------
 Index Scan using cities_uf_regiao_municipio_idx on cities  (cost=0.28..8.30 rows=1 width=4) (actual time=0.108..0.112 rows=1 loops=1)
   Index Cond: ((uf = 33) AND (regiao = 3) AND (municipio = 330455))
 Planning Time: 0.236 ms
 Execution Time: 0.187 ms
(4 rows)
```
