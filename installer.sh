#!/bin/bash


# installing airflow and mysql libraries
sudo apt-get update
sudo apt install python3-pip -y
sudo pip install apache-airflow
sudo apt install default-libmysqlclient-dev -y
sudo apt-get install libmysqlclient-dev


# to manage library files
sudo apt-get install pkg-config
sudo apt-get install software-properties-common -y


# installers for spark
sudo apt-get install openjdk-11-jdk -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8 -y
wget https://archive.apache.org/dist/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3.tgz

# locating where python is installed on the system
ls /usr/bin/python*

# setting python 3.8 as the default python version in your system
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 3
sudo update-alternatives --config python

# installing airflow dependencies
pip install apache-airflow-providers-ssh
pip install apache-airflow-providers-mysql
pip install apache-airflow-providers-oracle
pip install apache-airflow-providers-microsoft-mssql
pip install apache-airflow-providers-amazon
pip install apache-airflow-providers-apache-spark
pip install apache-airflow-providers-snowflake
