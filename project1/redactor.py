import argparse
import project1
import glob

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required= True,nargs='*',action="append",help= 'used for input text files to be redacted')
    parser.add_argument('--names',action="store_true",required=False,help= 'used for redacting names in text file')
    parser.add_argument('--dates',action="store_true", required=False,help= 'used for redacting dates in text file')
    parser.add_argument('--phones',action="store_true",required=False, help= 'used for redacting phone numbers in text file')
    parser.add_argument('--genders',action="store_true",required=False, help= 'used for redacting gender in text file')
    parser.add_argument('--address',action="store_true",required=False ,help= 'used for redacting address in text file')
    parser.add_argument('--concept',type=str,required=False,action="append", help= 'used for redacting kids related text in input file')
    parser.add_argument('--output',type=str,required=False, help= 'To keep the redacted files in to the particular folder')
    parser.add_argument('--stats',required=False, help='To keep the stats of redacted words in to a folder')
    args= parser.parse_args()
    lis=glob.glob(args.input[0][0])
    input_list=[]
#    print(lis)
    for i in lis:
            if i[-4:]==".txt":
                with open(i) as f:
                    lines = f.read()
                    input_list.append(lines)
            else:
                print("Input file is not txt file and cannot be read:"+ i)

    outputList = []
    for i in input_list:
        stats_list = []
        namesCount=0
        genderCount=0
        datesCount=0
        phoneCount=0
        addressCount=0
        if args.names:
            i,namesCount = project1.name_redaction(i)
#            print(namesCount)
        if args.genders:
            i,genderCount = project1.gender_redaction(i)
        if args.dates:
            i,datesCount = project1.date_redaction(i)
        if args.phones:
            i,phoneCount = project1.phonenumbers_redaction(i)
        if args.address:
            i,addressCount = project1.address_redaction(i)
        if args.concept:
            for j in args.concept:
                i = project1.concept_redaction(i,j)
        outputList.append(i)
        stats_dict={}

        stats_dict['name']=str(namesCount)
        stats_dict['gender']=str(genderCount)
        stats_dict['dates']=str(datesCount)
        stats_dict['phonenumbers']=str(phoneCount)
        stats_dict['address']=str(addressCount)
        stats_list.append(stats_dict)
#        print(stats_list)
        if args.stats:
            for j in stats_list:
                #print(j)
                project1.stats_files(j,args.stats)



    map=zip(lis,outputList)
    map_list=list(map)
    if args.output:
        for j in map_list:
            i = project1.output(j[1],j[0],args.output)
        #print(i)

''''

#    print(outputList[2])

            # outputList.append(doc)
            # print(outputList[0])
'''




