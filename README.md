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
