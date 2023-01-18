# Databricks notebook source
# MAGIC %run ./Settings

# COMMAND ----------

sql = (f"USE CATALOG {catalog}")
spark.sql(sql)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE bronze.customer(
# MAGIC Name STRING,
# MAGIC Address STRING,
# MAGIC Age INT
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into bronze.customer(name,address,age) values 
# MAGIC ("John Doe","1 Main Street",25),
# MAGIC ("Jane Doe", "2 Market Street",55)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from bronze.customer

# COMMAND ----------

print("This is production")

# COMMAND ----------

print(catalog)
