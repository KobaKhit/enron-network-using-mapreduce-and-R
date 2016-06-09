# Network analysis of Enron emails

## Upload Enron data to hadoop

Assuming the `enron-emails` folder is in the `data` folder. You can download the Enron Email Dataset from 
[this link](http://www.cs.cmu.edu/~enron/)

For hadoop we are using [CDH 5.5 virtual machine](http://www.cloudera.com/downloads/cdh/5-5-0.html) by Cloudera.

First, you will have to run `emails-rename.sh` shell script to give the email files unique names instead of repeating numbers. Refer to [this README.md](/shell-scripts/README.md).

```
mkdir data/enron-emails-sent
sh shell-scripts/emails-rename.sh data/enron-emails sent data/enron-emails-sent
sh shell-scripts/emails-rename.sh data/enron-emails inbox data/enron-emails-inbox
```

Now, we can upload files uniquely named files to hdfs.

```bash
hadoop fs -mkdir enron-sent enron-inbox
hadoop fs -put data/enron-emails-sent/* enron-sent
hadoop fs -put data/enron-emails-inbox/* enron-inbox
```

## Mapreduce

Refer to README in `mapreducers/` to find info about the mappers and reducers. They can be executed in shell or using hadoop streaming API. Below are examples for the first mapreduce job. To execute the other one change the digit in the names of the mapper and reducer from 1 to 2.

### Hadoop

```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input enron-sent \
-output enron-sent-out -file mapper1.py -file reducer1.py \
-mapper mapper1.py -reducer reducer1.py

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input enron-inbox \
-output enron-inbox-out -file mapper1.py -file reducer1.py \
-mapper mapper1.py -reducer reducer1.py
```

### Shell

```bash
find ../data/enron-emails/*/inbox/* -name '*.' -exec cat {} \; | python mapper1.py | sort | python reducer1.py > ../data/n-conns-inbox.txt

find ../data/enron-emails/*/sent/* -name '*.' -exec cat {} \; | python mapper1.py | sort | python reducer1.py > ../data/n-conns-inbox.txt
```

## R Network Analysis

Links to R analysis [with code](https://rpubs.com/Koba/enron-network-code) and [without code](https://rpubs.com/Koba/enron-network).

Link to [github repo]().