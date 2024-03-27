from pyspark.sql import *
from pyspark.sql.functions import *

spark = SparkSession.builder.master("local[*]").appName("sparkpoc").getOrCreate()

myconf = {
        "url": "jdbc:mysql://EndPoint/DatabaseName?useSSL=false",
        "user": "",
        "password": "",
        "driver": "com.mysql.cj.jdbc.Driver"
}

mysfconf = {
        "sfURL": "AccountID.snowflakecomputing.com",
        "sfUser": "",
        "sfPassword": "",
        "sfDatabase": "",
        "sfSchema": "",
        "dfWarehouse": "",
}

df = spark.read.format("jdbc").options(**myconf).option("dbtable", "dept").load()

ndf = df.withColumn("ts", current_timestamp())

ndf.write.mode("overwrite").format("net.snowflake.spark.snowflake").options(**mysfconf).option("dbtable", "newdept").save()
