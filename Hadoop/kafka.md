1.#解压

2.##配置文件
server.properties

```bash
maste上的
cd $KAFKA_HOME/config/server.properties

broker.id=1
listeners=PLAINTEXT://192.168.0.202:9092
zookeeper.connect=192.168.0.202:2181，
192.168.0.203:2181,192.168.0.204:2181

slave1
broker.id=2
listeners=PLAINTEXT://192.168.0.203:9092
zookeeper.connect=192.168.0.202:2181，
192.168.0.203:2181,192.168.0.204:2181

slave2
broker.id=3
listeners=PLAINTEXT://192.168.0.204:9092
zookeeper.connect=192.168.0.202:2181，
192.168.0.203:2181,192.168.0.204:2181

```
#配置环境变量
```bash
export KAFKA_HOME=/simple/kafka_2.11-2.2.0
export PATH=$KAFKA_HOME/bin:$PATH
source ~/.bashrc
```
#上传
```bash
scp -r /simple/kafka_2.11-2.2.0 slave1:/simple/kafka_2.11-2.2.0
scp -r /simple/kafka_2.11-2.2.0 slave2:/simple/kafka_2.11-2.2.0
scp ~/.bashrc slave1:~/.bashrc
scp ~/.bashrc slave2:~/.bashrc
```
#启动kafka
```bash
./kafka-server-start.sh ./../config/server.properties &
```
##查看是否已经启动
```bash
ps -ef grep | kafka
```
#注意
```bash
1.主机master启动以后
ssh slave1
(1)source ~/.bashrc
(2)./kafka-server-start.sh ./../config/server.properties &
(3)ps -ef grep | kafka
2.slave2同上步
```
