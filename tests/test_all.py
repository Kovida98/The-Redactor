
from project1 import project1
import pytest
import glob

lis=glob.glob('test.txt')
input_list=[]
#print(lis)
for i in lis:
    with open(i) as f:
        text=f.read()
        input_list.append(text)

def test_name_redaction():
    for i in input_list:
        lines,names_count=project1.name_redaction(i)
        assert lines is not None
        assert names_count > 0

def test_gender_redaction():
    for i in input_list:
        lines,gender_count=project1.gender_redaction(i)
        assert lines is not None
        assert gender_count >0

def test_date_redaction():
    for i in input_list:
        lines,date_count=project1.date_redaction(i)
        assert lines is not None
        assert date_count >0

def test_phonenumbers_redaction():
    for i in input_list:
        lines,phone_count=project1.phonenumbers_redaction(i)
        assert lines is not None
        assert phone_count >0

def test_address_redaction():
    for i in input_list:
        lines,address_count=project1.address_redaction(i)
        assert lines is not None
        assert address_count >0

def test_concept():
    for i in input_list:
        lines = project1.concept_redaction(i,"good")
        assert lines is not None










