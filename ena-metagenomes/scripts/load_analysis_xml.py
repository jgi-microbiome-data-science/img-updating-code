
import mysql.connector

con = mysql.connector.connect(option_files="/global/homes/s/snayfach/.my.cnf")

cur = con.cursor()

cur.execute("drop table if exists ena_analyses")

cur.execute("""
create table ena_analyses (
analysis_id varchar(255),
title varchar(255),
name varchar(255),
type varchar(255),
coverage float,
program varchar(255),
platform varchar(255),
mol_type varchar(255),
tpa varchar(255),
run_id text,
sample_id varchar(255),
study_id varchar(255),
biosample_id varchar(255),
bioproject_id varchar(255),
ftp varchar(255),
key analysis_id(analysis_id),
key sample_id(sample_id),
key study_id(study_id),
key biosample_id(biosample_id),
key bioproject_id(bioproject_id)
)""")

rows = []
for _ in open("data/tsv/analyses.tsv"):
    row = _.rstrip("\n").split("\t")
    row = [r if r != "None" else None for r in row]
    rows.append(row)
rows = rows[1:]
     
query = "insert into ena_analyses"
query += " values (%s)" % ("%s,"*len(rows[0])).rstrip(",")
cur.executemany(query, rows)

con.commit()
