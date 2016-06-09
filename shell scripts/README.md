# Instructions on using shell scripts

**Commands executed in current directory.**

### count-emails.sh
Gets the count of emails in a folder (sent, or inbox) from the original dataset.

**Usage**: `sh count-emails.sh`

**Example**: Assuming the `enron-emails` folder is in the `data` folder.

```bash
sh count-emails.sh ../data/enron-emails sent > ../data/n-conns-sent.txt
```

### emails-rename.sh
Rename email files in each persons account to be uniquely named in contrast to being just numbered.

**Usage**: `sh emails-rename.sh SOURCE FOLDER DEST_FOLDER`

**Example**:

```
mkdir ../data/enron-emails-sent
sh emails-rename.sh ../data/enron-emails sent ../data/enron-emails-sent
```