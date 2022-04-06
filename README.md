## THE REDACTOR

When sensitive material is shared with the public, it must first be 
redacted. That is, any sensitive names, locations, and other sensitive
data must be concealed. Sensitive information can be found in documents
such as police reports, court transcripts, and hospital records. 
The process of redacting this material is often costly and time-consuming.
In this project, I applied my python skills, hugging face, and NLTK 
packages to redact sensitive information from a ".txt" file.Here, we are
redacting names,genders,dates,address,phone numbers and also we need to 
redact the whole sentence for one particular concept.For output, i am
creating a folder named `files` to store the redacted file by changing
the file name.For the statistics of redacted words, i am creating a folder
named `stderr` to store the `stderr.txt` file.

## AUTHOR:

Kovida Mothukuri

Author Email: kovida.mothukuri-1@ou.edu

## TREE STRUCTURE:

```
.
├── COLLABORATORS
├── LICENSE
├── README.md
├── project1
│        ├── 1.txt
│        ├── 107.txt
│        ├── 2.txt
│        ├── files
│              ├── 1.redacted
│              ├── 107.redacted
│              └── 2.redacted
│        ├── main.py
│        ├── project1.py
│        ├── redactor.py
│        └── stderr
│            └── stderr.txt
├── requirements.txt
├── setup.cfg
├── setup.py
└── tests
    ├── test.txt
    └── test_all.py
```

## PACKAGES USED:

To run this code we need following packages:
1. glob
2. re
3. os
4. nltk
5. wordnet
6. omw-1.4
7. punkt
8. transformers
9. argparse
10. pytest
11. pytorch
12. tensorflow
13. ntpath

## FUNCTIONS:
I made a folder called project1 with two files titled `project1.py` and
`redactor.py` in it.
I've written code for eight functions in the `project1.py` file. I called
all these functions in `redactor.py` file.
### project1.py:
1. **name_redaction():**

    As an input parameter, I am sending `lines` which is a string of whole text
    of the file.In this method, I used hugging face to tokenize the sentences.
    In this method, I considered that redaction of name of the persons and organizations.
    By tokenizing the text from the file, it will give you the list of dictionary
    which contains entity group,word,start,end etc values.So by iterating through
    that list by checking the entity_group == PER or ORG, i am able to redact
    those words.Here, i am able to redact the words which are identified by
    hugging face package.
2. **gender_redaction():**

    In this method, I am redacting the genders by defining one list named
    gender_list which contains some of the words which reveal the gender of
    the person. gender_list has these words:

    `gender_list=[' father ',' mother ',' she ',' her ',' he ',' his ',' woman ',' women ',' men ',' man ',' female ',' male ',' him ',' wife ',' husband ',' Father ',' Mother ',' She ',' Her ',' He ',' His ',' Woman ',' Women ',' Men ',' Man ',' Female ',' Male ',' Him ',' Wife ',' Husband ']`
    Here it will redact the words which has space before and after the gender word.
    By iterating through that list,i am checking whether that word
    is present in that string or not.If it is present i am redacting the word
    by using the symbol '█'.
3. **date_redaction():**
    
    In this method,i am redacting the dates for the following example patterns:
    
    - 14 May 2001 : `\d{1,2}\s+[A-Za-z]*\s+\d{2,4}`
    - 22/2/2022 or 2/12/22 : `[0-9]{1,2}[/][0-9]{1,2}[/][0-9]{4}`
    - April 24 or Apr 1 or Jan2022 or Jan12 : `(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{0,1}\d{2,4}`
    
    To redact these i wrote regex for every pattern to indentify those patterns.
    This function takes input as lines and returns the redacted lines and count 
    of the redacted dates.
4. **phonenumbers_redaction():**

    In this method, i am redacting the phone numbers for the following
    example patterns:
    
    - +1-201-761-7500 or 1-201-761-7500 : `[+]?\d{1,3}[-]\d{3}[-]\d{3}[-]\d{4}`
    - +1 201 761 7500 : `[+]{1}\d{1,3}\s{0,1}\d{3}\s{0,1}\d{3}\s{0,1}\d{4}`
    - +912017617500 : `[+]{1}\d{1,3}\s{0,1}\d{3}\s{0,1}\d{3}\s{0,1}\d{4}`
 
   Here, for the extension of phone number, it can take one to three numbers 
   as the extensions are different for different countries.It takes the input
   lines and returns redacted text and count of phone numbers redacted.By using
   findall method, i am searching for the dates which matches those patterns. By using
   those dates, i am redacting those by using this character '█'.
5. **address_redaction():**

    Firstly,to redact address, i am using hugging face to tokenize the words. After tokenizing
    i am checking `entity_group=='LOC'`, then i am redacting the words which are recognized
    by that. Mostly it will redact the state and country names.

    Secondly,I wrote regex for particular address pattern.Below is the example of address pattern:

    - 795 E DRAGRAM : `\d{1,}\s(?:East|West|North|South|E|W|N|S|NE|NW|SE|SW)\s?\w{1,}`
    first more than 1 digit number and second which gives the directions like 
    North,South,E,W etc and third any word.Here i am using findall method for this 
    regex pattern and redacting with the character '█'.
6. **concept_redaction():**

   This method takes the lines as input parameter and returns the redacted text.
   In this method, i used nltk to tokenize and to get the synonyms of the
   particular word.I appended all the synonym words in to a list named `concept_words`.
   Here first, i tokenized by sentence which will return a list 
   named as `sentences` and then by word returns list named as `tok_words`.
   By iterating through both the lists i found whether the tokenized word is
   present in that concept_words list. If it is present then redact the whole sentence.
   
7. **output():**

   This method takes the lines and path of the txt file and filename as input paramaters.
   In this method, by checking the current working directory, i am creating a
   folder named `files` to store all the redacted files.Here, i am writing the redacted 
   text to the new file with the same name as input file but with extension ".redacted".
8. **stats_files():**

   In this method, I am creating a folder to store the txt file which contains
   stats of each method.Here, I am creating a folder named 
   `stderr` and in that folder i am creating the file name called `stderr.txt`.
    To that `stderr.txt`, i am pushing the redacted statistics of all methods.
### redactor.py:
In redactor.py file, i have added parser arguments for each flag. Here in this file,
by using glob function retrieving the txt files in the particular folder path.
glob function will return a list named `lis`.By iterating through that list `lis`,
open function is used to read the text in that files. If the file has .txt as extension
it will retrieve the text otherwise it will print the statement as "File cannot be read".
The read function will return a list which contains the text of each file as string named
`input_list`. By iterating through that input_list, i am calling each function which 
is present in Project1.py by writing if condition. For stats flag, i am creating a dictionary
which will contain the count of redacted name,gender,date,phonenumber,address.
By using that dictionary, I am calling `stats_file` function. For Output flag,
I am using zip to zip two lists of file name `lis` and redacted text of that file `outputlist`and again changing that 
zipped to a list named map_list. By iterating through that map_list, i am calling the 
function `output` which will create a folder named `files`.

## TEST CASES:
For test cases, i created a folder named `tests` and in that created a file
named `test_all.py`. I kept one file called `test.txt` which contains the text same as 
input files.Here i called the glob function for the file `test.txt` and by iterating
through the output of glob function, i have read the files and pushed in to a list named `input_list`.
This file contains six functions named:
- **test_name_redaction():** 

    This will test the `name_redaction()` function by iterating through the `input_list` and by calling that function will
    return the redacted text in `lines` and count in `names_count`.I tested lines 
    by writing assert is not none and names_count is greater than zero.
- **test_gender_redaction():**

    This will test the `gender_redaction()` function by iterating through the `input_list` and by calling that function will return
    redacted text in `lines` and count in `gender_count`.I tested lines by writing assert
    is not none and gender_count is greater than zero.
- **test_date_redaction():**

    This will test the `date_redaction()` function by iterating through the `input_list` and by calling that function will return
    redacted text in `lines` and count in `date_count`.I tested lines by writing assert
    is not none and date_count is greater than zero.
- **test_phonenumbers_redaction():**

    This will test the `phonenumbers_redaction()` function by iterating through the `input_list` and by calling that function will return
    redacted text in `lines` and count in `phone_count`.I tested lines by writing assert
    is not none and phone_count is greater than zero.
- **test_address_redaction():**

    This will test the `address_redaction()` function by iterating through the `input_list` and by calling that function will return
    redacted text in `lines` and count in `address_count`.I tested lines by writing assert
    is not none and address_count is greater than zero.
- **test_concept():**

    This will test the `concept_redaction()` function by iterating through the `input_list` and by calling that function will return
    redacted text in `lines`.I tested lines by writing assert is not none.



## COMMANDS TO RUN:
Here to run the file we have to use below command:
`pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones --genders --address\
                    --concept 'kids' \
                    --output 'files/' \
                    --stats stderr`

**For example:**
`python redactor.py --input "*.txt" --names 
--gender --phones --dates --address --output 'files/' --concept good 
--stats stderr
`

**Expected Output:**

To run test cases we can use any one of the following commands

`pipenv run python -m pytest`


## ASSUMPTIONS AND BUGS:

For Names redaction, It will redact those names which are recognized by hugging face package.

For gender redaction, It will redact those words which are there in the assumed list and 
it will redact those words which have space before and after the gender word.


for example: for the word 'she', it should contain space before and after the word 'she'.

For date redaction, It will redact those dates which are in particular patterns because i assumed 
most of the date formats will be in the following patterns:

- 14 May 2001 i.e, dd May yyyy
- 22/2/2022 or 2/12/22 i.e, mm/dd/yyyy or mm/dd/yy
- April 24 or Apr 1 or Jan2022 i.e, April dd or April YYYY or Aprildd or Aprilyyyy

It cannot redact other than these patterns.

For Phone numbers redaction,It cannot redact other than the following patterns:
- +1-201-761-7500 or 1-201-761-7500
- +1 201 761 7500
- +912017617500 

For address redaction, It can redact those are identified by hugging face package as
location and can redact only for one pattern of address:

- 795 E DRAGRAM 

For Stats flag, if we run the program once, we need to delete the stats file created to rerun the 
program again.



## DIRECTIONS TO INSTALL:

You can create folders and files using mkdir and touch commands.
Here in this project we will be using python 3.10.2 version. to install that use this command.

`pipenv install --python 3.10.2`

After downloading the project from github, go to that directory using cd.Install pipenv by using
command. `pip install pipenv`. After that by checking requirements.txt file, you have to install all
required packages.  you need to install pytest using this command `pipenv install pytest`.Once the installation of pytest is done, you will be able to
run the unittests using `pipenv run python -m pytest`. you can run the code using
`pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones --genders --address\
                    --concept 'kids' \
                    --output 'files/' \
                    --stats stderr`.
## EXTERNAL LINKS USED:
[https://www.pythontutorial.net/python-basics/python-read-text-file/](https://www.pythontutorial.net/python-basics/python-read-text-file/)
[https://www.computerhope.com/issues/ch001721.htm](https://www.computerhope.com/issues/ch001721.htm)
[https://stackoverflow.com/questions/63221913/named-entity-recognition-with-huggingface-transformers-mapping-back-to-complete](https://stackoverflow.com/questions/63221913/named-entity-recognition-with-huggingface-transformers-mapping-back-to-complete)
[https://docs.python.org/3/howto/regex.html](https://docs.python.org/3/howto/regex.html)
[https://www.codeunderscored.com/regular-expressions-in-python/](https://www.codeunderscored.com/regular-expressions-in-python/)
[https://www.codegrepper.com/code-examples/python/save+files+in+a+particular+folder+python](https://www.codegrepper.com/code-examples/python/save+files+in+a+particular+folder+python)
[https://www.geeksforgeeks.org/os-module-python-examples/](https://www.geeksforgeeks.org/os-module-python-examples/)
[https://stackoverflow.com/questions/11700593/creating-files-and-directories-via-python](https://stackoverflow.com/questions/11700593/creating-files-and-directories-via-python)
[https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/#:~:text=Check%20if%20a%20directory%20exists%20os.path.isdir%20%28%29%20method,a%20directory%20then%20the%20method%20will%20return%20True.](https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/#:~:text=Check%20if%20a%20directory%20exists%20os.path.isdir%20%28%29%20method,a%20directory%20then%20the%20method%20will%20return%20True.)
[https://www.geeksforgeeks.org/python-dictionary-items-method/#:~:text=In%20Python%20Dictionary%2C%20items%20%28%29%20method%20is%20used,of%20a%20given%20dictionary%E2%80%99s%20%28key%2C%20value%29%20tuple%20pair.](https://www.geeksforgeeks.org/python-dictionary-items-method/#:~:text=In%20Python%20Dictionary%2C%20items%20%28%29%20method%20is%20used,of%20a%20given%20dictionary%E2%80%99s%20%28key%2C%20value%29%20tuple%20pair.)



