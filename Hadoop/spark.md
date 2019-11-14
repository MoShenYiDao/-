spark
1.##解压
```bash
mkdir spark
cd    spark
tar -zxvf spark-2.4.3-bin-hadoop2.7.tgz
```
2.配置环境变量
```bash
vim ~/.bashrc
export SPARK_HOME=/spark/spark-2.4.3-bin-hadoop2.7
export PATH=$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
source ~/.bashrc
```
3.配置文件
```bash
cd $SPARK_HOME/conf
cp spark-env.sh.template spark-env.sh   第一个文件
vim spark-env.sh
cp slaves.template slaves               第二个文件
vim slaves
```
4.给$SPARK_HOME/sbin文件中的start-all.sh 和stop-all.sh 把源文件移动到目标的
```bash
mv start-all.sh start-spark-all.sh
mv stop-all.sh stop-spark-all.sh
```
5.传送给slave1和slave2
```bash
首先在slave1和slave2上分别mkdir spark这样文件才可以传过去
scp -r /spark/spark-2.4.3-bin-hadoop2.7 slave1:/spark/spark-2.4.3-bin-hadoop2.7
scp -r /spark/spark-2.4.3-bin-hadoop2.7 slave2:/spark/spark-2.4.3-bin-hadoop2.7
scp ~/.bashrc slave1:~/.bashrc 
scp ~/.bashrc slave2:~/.bashrc 
```
6.ssh slave1
```bash
source ~/.bashrc
```
7.ssh slave2
```bash
source ~/.bashrc
```
8.master上启动
```bash
这是分别启动
start-master.sh 
start-slaves.sh
也可以直接启动 
start-spark-all.sh
最后jps
```
9.slave1上启动
```bash
start-master.sh 
start-slaves.sh
jps
```
10.slave2上启动
```bash
start-master.sh 
start-slaves.sh
jps
```
11.注意spark-env.sh里的配置文件
```bash
export JAVA_HOME=/java/jdk1.8.0_191
export HADOOP_CONF_DIR=/usr/local/hadoop-2.7.3/etc/hadoop
export SPARK_MASTER_HOST=master
export SPARK_MASTER_PORT=7077
export SPARK_WORKER_CORES=1
export SPARK_WORKER_MEMORY=1g
```
12.注意slaves里的文件
```bash
192.168.0.202
192.168.0.203
192.168.0.204
```
13slave1上启动的效果
```bash
8000 Jps
3653 SecondaryNameNode
7861 Worker
5833 QuorumPeerMain
一个worker
```
14.slave2
```bash
32244 Jps
3925 SecondaryNameNode
31927 Worker
30590 QuorumPeerMain
一个worker
```
15master
```bash
44853 Jps
44597 Worker
44437 Master
39673 NameNode
39034 QuorumPeerMain
40011 ResourceManager
41903 HMaster
一个master和一个worker
```
#一定要注意
```bash
1.关闭防火墙  service iptables stop
```
