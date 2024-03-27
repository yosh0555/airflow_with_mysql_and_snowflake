#   Creating a pipeline using spark to fetch data from MySQL table, processing this data then storing this processed data into Snowflake every 5 minutes by using Apache Airflow to automate the process   #

1. First we need to create a connection to MySQL database for that hover to the "Admin" tab and select "Connections" option

![Connections](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/connections.png)

2. Now click on "+" symbol to create a new connection

![Add new connection](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/add_conn.png)

3. Enter the connection ID (It can be anything you want) then select "Spark" as the Connection Type

![Select Connection Type](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/spark_opt.png)

4. Now enter "local" or "local[*]" in Host field, "client" in Deploy mode field, "spark-submit" in Spark binary field

![Enter the information related to Spark](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/spark_details.png)

5. Now click on the "Save" button on the bottom left

![Save](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/save1.png)

6. Write a DAG program in the "~/airflow/dags/" directory to run a spark job every 5 minutes (you can find this code in the dags directory of this repository)

```bash
cd ~/airflow/dags/
vi mysqlToSnowflakeWithSparkAndAirflow.py
```

7. Now to run a spark job we need to include MySQL and Snowflake dependencies into the DAG program, so download the following dependencies in the home directory and include their paths in the DAG program

```bash
wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.11/mysql-connector-java-8.0.11.jar

wget https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/3.14.4/snowflake-jdbc-3.14.4.jar

wget https://repo1.maven.org/maven2/net/snowflake/snowflake-ingest-sdk/2.0.2/snowflake-ingest-sdk-2.0.2.jar

wget https://repo1.maven.org/maven2/net/snowflake/spark-snowflake_2.12/2.11.3-spark_3.1/spark-snowflake_2.12-2.11.3-spark_3.1.jar
```

8. Write a spark job that will fetch the data from MySQL, process that data and then store the processed data to Snowflake

```bash
cd ~
vi spark.py
```

9. After writing the DAG and spark program go to the Airflow webUI homepage and click on the "pause/unpause DAG" slider or "Trigger DAG" to run the DAG program

![Run DAG](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/run_dag1.png)

10. For more information click on the DAG name

![More Information about the DAG](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/dag_more_info1.png)

11. Click on graph to check task status

![Graph Option](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/graph_opt1.png)

12. Congrats the DAG program ran successfully, the table was created in MySQL server and the records were inserted in the table

![Run Successful](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/run_successful1.png)

![Snowflake table](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/snowflake_tab.png)

13. If more records are inserted into the MySQL table, the old records and the new records are overwritten to the Snowflake table after a regular interval of 5 minutes

![Inserting new records into MySQL](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/new_records.png)

![New records are reflected in the Snoflake table](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/new_records_snowflake.png)
