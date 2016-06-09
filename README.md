# Network analysis of Enron emails


<div style = "text-align:center">
<h4>Enron Network over Time Based on Sent Emails<msall> | Date Range: 1998-11->2001-04</small></h4>
<a href = "https://rpubs.com/Koba/enron-network" target = "_blank"><img src="https://github.com/KobaKhit/enron-network-using-mapreduce-and-R/blob/master/R/final_files/figure-html/unnamed-chunk-7-1.png" width = "80%"/></a>
</div>
## What it is about?

We explore the social network aspect of the [Enron Email dataset](http://www.cs.cmu.edu/~enron/). We use hadoop and shell as an alternative to transform the semi-unstructured email data into something we can work with. Using this data we will be able to visualize the social network grouped by the metrics such as edge betwenness, centrality index, etc. 

The reason it is an intersting project is to see how a network of people behaved in a company that was caught doing fraud. Additionally, this project is a great way to learn about dealing with large unstructured data using the mapreduce concept and open source tools like hadoop virtual machine and R.

The most challenging part of this project was coming up with rules to extract the metrics we wanted from the emails using mapreduce. We have done this with regular expressions, python and unix shell/hadoop. Additionally, it so happened that **one worker node is much slower than shell** when executing the mapreduce jobs. We provide examples in the code section for both shell and hadoop. We ran two mapreduce jobs in shell and they completed in around 25 minutes each.

## Code
## Upload Enron data to hadoop

Assuming the `enron-emails` dataset folder is in the `data` folder. You can download the Enron Email Dataset from 
[this link](http://www.cs.cmu.edu/~enron/). **Commands are executed from current (`enron-network-using-mapreduce-and-R/`) directory.**

For hadoop we are using [CDH 5.5 virtual machine](http://www.cloudera.com/downloads/cdh/5-5-0.html) by Cloudera.

First, you will have to run `emails-rename.sh` shell script to give the email files unique names instead of repeating numbers. Refer to [this README.md](/shell-scripts/README.md) in `shell-scripts/` for more info.

```
mkdir data/enron-emails-sent
sh shell-scripts/emails-rename.sh data/enron-emails sent data/enron-emails-sent
sh shell-scripts/emails-rename.sh data/enron-emails inbox data/enron-emails-inbox
```

Now, we can upload uniquely named files to hdfs.

```bash
hadoop fs -mkdir enron-sent enron-inbox
hadoop fs -put data/enron-emails-sent/* enron-sent
hadoop fs -put data/enron-emails-inbox/* enron-inbox
```

## Mapreduce

Refer to README in `mapreducers/` to find more info about the mappers and reducers. They can be executed **in shell** or using **hadoop streaming API**. Below are examples for the first mapreduce job. To execute the other one change the digit in the names of the mapper and reducer from 1 to 2.

### Hadoop

```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input enron-sent \
-output enron-sent-out -file mapper1.py -file reducer1.py \
-mapper mapper1.py -reducer reducer1.py

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input enron-inbox \
-output enron-inbox-out -file mapper1.py -file reducer1.py \
-mapper mapper1.py -reducer reducer1.py

# download results
hadoop fs -get training/shakespeare/poems ~/shakepoems.txt
```

### Shell

```bash
find ../data/enron-emails/*/inbox/* -name '*.' -exec cat {} \; | python mapper1.py | sort | python reducer1.py > ../data/n-conns-inbox.txt

find ../data/enron-emails/*/sent/* -name '*.' -exec cat {} \; | python mapper1.py | sort | python reducer1.py > ../data/n-conns-inbox.txt
```

## R Network Analysis

Links to R analysis [with code](https://rpubs.com/Koba/enron-network-code) and [without code](https://rpubs.com/Koba/enron-network).

Link to [github repo]().