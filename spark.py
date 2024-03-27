from pyspark.sql import *
from pyspark.sql.functions import *

# Creating a spark session
spark = SparkSession.builder.master("local[*]").appName("sparkpoc").getOrCreate()

# MySQL configuration
myconf = {
        "url": "jdbc:mysql://EndPoint/DatabaseName?useSSL=false",
        "user": "",
        "password": "",
        "driver": "com.mysql.cj.jdbc.Driver"
}

# Snowflake Configuration (Repalce the "AccountID" below with your own account id for ex: deezpxr-nt69055)
mysfconf = {
        "sfURL": "AccountID.snowflakecomputing.com",
        "sfUser": "",
        "sfPassword": "",
        "sfDatabase": "",
        "sfSchema": "",
        "dfWarehouse": "",
}

# Creating a dataframe "df" by fetching data from dept table in MySQL database
df = spark.read.format("jdbc").options(**myconf).option("dbtable", "dept").load()

# Transforming the dataframe "df"
ndf = df.withColumn("ts", current_timestamp())

# Storing the transformed/modified dataframe "ndf" to Snowflake as "newdept" table
ndf.write.mode("overwrite").format("net.snowflake.spark.snowflake").options(**mysfconf).option("dbtable", "newdept").save()
