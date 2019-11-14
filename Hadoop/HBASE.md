#hbase
1.解压文件
2.配置环境变量
```bash
 vim ~/.bashrc
 export HBASE_HOME=/simple/hbase-1.2.12
 export PATH=$PATH:$HBASE_HOME/bin
 source ~/.bashrc
```
###配置文件
```bash
cd $HBASE_HOME/conf/
vim hbase-site.xml
<property>
<name>hbase.rootdir</name>
<value>file:///simple/hbase-1.2.12/hbase</value>
</property>

<property>    簇      分布的，分散的
<name>hbase.cluster.distributed</name>
<value>true</value>
</property>

<property>             法定人数
<name>hbase.zookeeper.quorum</name>
<value>192.168.0.202,192.168.0.203,192.168.0.204<value>
</property>

<property>
<name>hbase.tmp.dir</name>
<value>/tmp/hbase</value>
</property>

<property>
<name>hbase.master</name>
<value>hdfs://192.168.0.202:60000</value>
</property>

<property>
<name>hbase.zookeeper.property.dataDir</name>
<value>/tmp/zookeeper</value>
</property>
mkdir /tmp/hbase

###考到slave1和slave2上
 scp -r $HBASE_HOME slave1:/simple/hbase-1.2.12
 scp -r $HBASE_HOME slave2:/simple/hbase-1.2.12
 scp -r ~/.bashrc slave1:~/.bashrc 
 scp -r ~/.bashrc slave2:~/.bashrc 
```
###ssh slave1
```bash
source ~/.bashrc
mkdir /tmp/hbase
```
###ssh slave2
```bash
source ~/.bashrc
mkdir /tmp/hbase
```
###exit 回到master上
```bash
start-hbase.sh 
jps
```
###注意
1. gedit hbase-site.xml 这个命令可以直接进行编辑
