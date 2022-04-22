# CHANGES

**TREE STRUCTURE:**
```
├── CHANGES.md
├── COLLABORATORS
├── LICENSE
├── README.md
├── docs
│    ├── 1.txt
│    ├── 107
│    └── 2.txt
├── files
│    ├── 1.txt.redacted
│    ├── 107.redacted
│    └── 2.txt.redacted
├── project1
│    └── project1.py
├── redactor.py
├── requirements.txt
├── setup.cfg
├── setup.py
├── stats.txt
└── tests
    ├── test.txt
    └── test_all.py
```
* Output files not stored in respective folder :
    
    I kept the input files in "docs" folder and changed the glob function code in such
    a way that it takes all files. I placed redactor.py file outside the project 1 folder that is i placed that in the 
    line of README.md file. After running the code, i can see my output folder is creating
    with the name which i gave in output flag in the README.md line.In that folder, i can see the redacted files got created.


* File names not reassigned correctly:

    I changed my code for the redacted text file names.It will take the redacted file names by just 
    adding ".redacted" at the end.

    For example, 
    
    if you give the "1.txt" as input file name. The output file name will changes to
    "1.txt.redacted".
     
    If you give "1" as input file name, the output file name will changes to 
    "1.redacted"


* Missing Stats:

    I changed my code in such a way that,if i give "stdout" in the stats flag, it will print
    the statistics of the redacted name,gender,date,phonenumbers,address in console.
    If you give "stderr", it will print the errors if i have any in console.
    If you give anything else other than stderr or stdout, my code will create a file
    with the name which i have given in the stats flag and it contains the count of all
    redacted names,genders,dates,phonenumbers,address.

* Missing names,gender,phone number,concept,dates,addresses: 
 
    I can see names, gender,phone numbers,concept,dates, addresses are redacting for me.
    It can redact those words which are recognized by the packages which i have used.
    For names, i am using hugging face package. It will redact all the names which are 
    recognized by the hugging face package.For dates, I am redacting almost all formats
    of dates by writing regex for different patterns.For gender also i am redacting almost all the words which are related to gender.
    For Addresses also i wrote the regex expression for some patterns of addresses.For concept,
    i used nltk package to redact the whole sentence which contains that concept word.


**OUTPUT:**

For OUTPUT:

```
Message-ID: <18782981.1075855378110.JavaMail.evans@thyme>
Date: Mon, ███████████ 16:39:00 -0700 (PDT)
From: phill██.███en@█████.com
To: tim.be███n@█████.com
Subject: 
Mime-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
X-From: ███████ █ █████
X-To: ██████████ <██████████/█████@██████████>
X-cc: 
X-bcc: 
X-Folder: \███████_█████_███████_1\█████, █████████.\'Sent Mail
X-Origin: █████-█
X-FileName: pallen (Non-Privileged).pst

Here is our forecast
i am████████.
```
 
For STATS:
* STATS output for stdout in console:
```
redaction for file1:

name:22 gender:1 dates:3 phonenumbers:4 address:8

redaction for file2:

name:26 gender:0 dates:3 phonenumbers:0 address:1

redaction for file3:

name:19 gender:3 dates:6 phonenumbers:0 address:3

```

