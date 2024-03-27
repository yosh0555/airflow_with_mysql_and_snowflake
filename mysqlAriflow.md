#   Creating a table in MySQL database and inserting values into this table #

1. First we need to create a connection to MySQL database for that hover to the "Admin" tab and select "Connections" option

![Connections](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/connections.png)

2. Now click on "+" symbol to create a new connection

![Add new connection](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/add_conn.png)

3. Enter the connection ID (It can be anything you want) then select "MySQL" as the Connection Type

![Select Connection Type](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/mysql_opt.png)

4. Now enter the MySQL endpoint in "Host" field, database name in "Schema" field, username in "Login" field, password in "Password" field and post number as 3306

![Enter the information related to MySQL database](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/mysqldb_creds_details.png)

5. Now click on the "Save" button on the bottom left

![Save](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/save.png)

6. Open a new terminal window and go to the airflow directory which is created in the home directory after the installation, in that directory create another directory named "dags"

```bash
cd ~/airflow/
mkdir dags
```

7. Now write a DAG program to create a table in MySQL database and inserting values in to that table (you can find this code in the dags directory of this repository)

```bash
vi mysqlAirFlow.py
```

8. After you are done writing the DAG program head over to the webUI, go to the "DAGs" tab (Airflow home page), there click on the "pause/unpause DAG" slider or "Trigger DAG" to run the DAG program

![Run DAG](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/run_dag.png)

9. For more information click on the DAG name

![More Information about the DAG](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/dag_more_info.png)

10. Click on graph to check task status

![Graph Option](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/graph_opt.png)

11. Congrats the DAG program ran successfully, the table was created in MySQL server and the records were inserted in the table

![Run Successful](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/run_successful.png)

![MySQL table](https://github.com/yosh0555/airflow_with_mysql_and_snowflake/blob/master/images/mysql_tab.png)
