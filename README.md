# Network analysis of Enron emails

Assuming the `enron-emails` folder is in the `data` folder.

##Upload data to hadoop

```
sh scripts/emails-rename.sh
hadoop fs -mkdir enron-sent
hadoop fs -put data/enron-emails-sent/* enron-sent

```

Refer to README in `mapreducers/` to get the data.

Links to R analysis [with code](https://rpubs.com/Koba/enron-network-code) and [without code](https://rpubs.com/Koba/enron-network).

Link to [github repo]().