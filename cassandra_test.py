from cassandra.cluster import Cluster

cluster = Cluster(['localhost'])
session = cluster.connect()

session.execute("CREATE KEYSPACE stocks WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}")

session.set_keyspace('stocks')
session.execute("""
                  CREATE TABLE company (
                      company_id text,
                      name_latest text,
                      name_previous text,
                      PRIMARY KEY (company_id)
                   )
                """)

session.execute("""
                  CREATE TABLE indicator_by_company (
                      company_id text,
                      indicator_id text,
                      yr_2010 bigint,
                      yr_2011 bigint,
                      yr_2012 bigint,
                      yr_2013 bigint,
                      yr_2014 bigint,
                      yr_2015 bigint,
                      yr_2016 bigint,
                      PRIMARY KEY (company_id, indicator_id)
                   )
                """)

import json

with open('companies.json') as f_in:
	companies = json.load(f_in)

for company in companies:
    try:
        session.execute(
                           """
                           INSERT INTO company (company_id, name_latest, name_previous)
                           VALUES (%s, %s, %s)
                           """,
                           (company['company_id'],company['name_latest'], company['names_previous']))
    except:
        pass

result_set = session.execute("SELECT * FROM company")

print(result_set.current_rows)