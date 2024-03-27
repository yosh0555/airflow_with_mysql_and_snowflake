from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator
from datetime import datetime, timedelta

# Define default arguments for DAG
default_args = {
        'owner': 'yosh0555',
        'start_date': datetime(2024, 3, 27),
        'retries': 1,
        'retry_delay': timedelta(minutes=1)
}

# Define a DAG
mysqldag = DAG('mysql_poc',
        default_args = default_args,
        description = 'poc to create and store table in MySQL database',
        start_date = datetime(2024, 3, 27),
        schedule_interval = '@once',
        catchup = True
)

# Define a task to create a table in MySQL database
create_table = MySqlOperator(
        task_id = 'create_table_task',
        mysql_conn_id = 'connect_mysql',
        sql = 'create table if not exists mytab (name varchar(10), age int);',
        dag = mysqldag
)

# Define a task to insert values into the table created in MySQL database
insert_data = MySqlOperator(
        task_id = 'insert_data_task',
        mysql_conn_id = 'connect_mysql',
        sql = "insert into mytab values('Jolyne', 23), ('John', 30), ('Emily', 25), ('Michael', 40), ('Sarah', 35), ('James', 28), ('Jennifer', 33), ('David', 45), ('Emma', 22), ('Liam', 27), ('Olivia', 31), ('Benjamin', 38), ('Ava', 29), ('Matthew', 42), ('Sophia', 26), ('William', 32), ('Charlotte', 34), ('Daniel', 36), ('Mia', 23), ('Ethan', 37), ('Amelia', 24), ('Alexander', 39), ('Harper', 41), ('Jackson', 43), ('Evelyn', 30), ('Henry', 28), ('Abigail', 27), ('Sebastian', 34), ('Avery', 25), ('Joseph', 31), ('Madison', 26), ('David', 40), ('Chloe', 29), ('Samuel', 33), ('Grace', 22), ('Owen', 35), ('Scarlett', 32), ('Lucas', 36), ('Lily', 23), ('Gabriel', 38), ('Zoe', 31);",
        dag = mysqldag
)

# Specify the task execution order
create_table >> insert_data
