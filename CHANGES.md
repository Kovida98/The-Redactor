#CHANGES

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

    
