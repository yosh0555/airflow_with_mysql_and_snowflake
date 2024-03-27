#   Installation    #

1. Run the installer.sh file

```bash
sh installer.sh
```

2. Now extract the spark tar file

```bash
tar -xvf spark-3.3.0-bin-hadoop3.tgz
```

3. Move the spark directory to /usr/bin/

```bash
sudo mv spark-3.3.0-bin-hadoop3 /usr/bin/
```

4. setup enviroment variables for spark in .bashrc file

```bash
vi ~/.bashrc
```

5. type the following commands in the .bashrc file

```bash
export SPARK_HOME=/usr/bin/spark-3.3.0-bin-hadoop3
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
```

6. use this command to apply the changes in .bashrc file

```bash
source ~/.bashrc
```


#   Setting pyspark python version to 3.8   #

1. Use the following command to check which python version being used by pyspark

```bash
pyspark
```

2. If the version is not 3.8, open the .bashrc file with an editor

```bash
vi ~/.bashrc
```

3. Type in the following command to setup environment variable for python used by pyspark

```
export PYSPARK_PYTHON=/usr/bin/python3.8
export PYSPARK_DRIVER_PYTHON=/usr/bin/python3.8
```

4. Use the following command to apply the changes in .bashrc file

```bash
source ~/.bashrc
```


#   Starting the airflow server and logging into the webUI    #

1. Use the following command to start the airflow server
```bash
airflow standalone
```

2. Copy the password that is generated in the terminal
