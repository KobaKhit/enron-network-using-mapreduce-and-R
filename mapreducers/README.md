# Instructions on using mapreducers

**Commands executed in current directory.**

## Mapreduce 1

### mapper1.py

Output:

`rank<TAB>sender1<TAB>sender2<TAB>origin<TAB>recievers`

Example:
```
9999999	john arnold john arnold	arnold-j	slafontaine@globalp.com @ enron
```

### reducer1.py

Output: 

`sender1<TAB>recievers` or `sender1<TAB>number of recievers`

Example:

```
community  	1077
gorte, david 	795
clyatt, julie 	795
dl-technology 	795
dottie kerr 	795
energy insight editor @enron	795
```

## Mapreduce 2

### mapper2.py

Output:

`date<TAB>sender<TAB>receivers<TAB>subject<TAB>id`

Example:
```
2000-12-06 04:41:00	 phillip k allen	brenda stone <bs_stone@yahoo.com> @ enron    re: court ordered notice to customers and registered users of	1
```

### reducer2.py

Output: 

`sender<TAB>date<TAB>receiver<TAB>subject<TAB>id`

Example:

```
stephanie piwetz	1998-10-30 07:43:00	kate symes	39005
elizabeth sager sara shackleton	1998-10-30 07:56:00	mark - ect legal taylor	39502
alison smythe 	1998-10-30 08:02:00	mark - ect legal taylor	39587

```

## Usage

### Hadoop

```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input enron-sent \
-output conns-sent -file mapper1.py -file reducer1.py \
-mapper mapper1.py -reducer reducer1.py

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input enron-inbox \
-output conns-inbox mapper1.py -file reducer1.py \
-mapper mapper1.py -reducer reducer1.py

# download results
hadoop
```

Edit the `reducer1.py` file. Comment out lines 37 and 43. Uncomment lines  38 and 44.

For below commands I just changed the output filename to `n-conns-inbox.txt`.

```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input enron-sent \
-output n-conns-sent -file mapper1.py -file reducer1.py \
-mapper mapper1.py -reducer reducer1.py

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input enron-inbox \
-output n-conns-inbox mapper1.py -file reducer1.py \
-mapper mapper1.py -reducer reducer1.py
```

### Shell

```bash
find ../data/enron-emails-inbox/* -name '*.' -exec cat {} \; | python mapper1.py | sort | python reducer1.py > ../data/conns-inbox.txt

find ../data/enron-emails-sent/* -name '*.' -exec cat {} \; | python mapper1.py | sort | python reducer1.py > ../data/conns-inbox.txt
```

Same as for the hadoop usage.

```bash
find ../data/enron-emails-inbox/* -name '*.' -exec cat {} \; | python mapper1.py | sort | python reducer1.py > ../data/n-conns-inbox.txt

find ../data/enron-emails-sent/* -name '*.' -exec cat {} \; | python mapper1.py | sort | python reducer1.py > ../data/n-conns-inbox.txt
```


