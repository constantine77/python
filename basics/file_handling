#Python File Handling: Create, Open, Append, Read, Write

import csv
import os

def open_csv(csv_file):
    file_pointer = open(csv_file)
    return file_pointer


#open the csv file, read csv file and
#return file content
def read_csv(csv_file):
    file_pointer = open(csv_file, 'rt')
    contents = file_pointer.read()
    return contents

#open the csv file, read csv file line by line
def read_csv_by_line(csv_file):
    file_pointer = open(csv_file, 'rt')
    fl = file_pointer.readlines()
    for line in fl:
        print(line)

#create a text file:
def create_file():
    file_pointer = open("sample.txt","w+")
    file_pointer.write("This is first line")
    file_pointer.close()

#Write a python list into list.csv file:
def write_list_into_file():
    os.remove('list.csv')
    companies_list = [['Copmany_name','Zip_Code'],['Apple','6000'],['Goole','7000'],['IBM','8000']]
    file_pointer = open('list.csv','w')
    writer = csv.writer(file_pointer)
    writer.writerows(companies_list)
    file_pointer.close()




#Write a python dict into dict.csv file:
def write_dict_into_file():
    companies_dict = [{'Company_name':'Apple', 'Zip_Code':'6000'},{'Company_name':'Google', 'Zip_Code':'7000'},
                      {'Company_name': 'IBM', 'Zip_Code': '8000'}]
    os.remove('dict.csv')
    file_pointer = open('dict.csv','w')
    fields = ['Company_name', 'Zip_Code']
    writer = csv.DictWriter(file_pointer, fieldnames = fields)
    writer.writeheader()
    writer.writerows(companies_dict)

#Write from CSV file into list
#use the ‘rb’ method meaning “read binary”
def write_csv_into_dict():
    companies_dict = []
    file_pointer = open('dict.csv','r')
    reader = csv.DictReader(file_pointer)
    for line in reader:
        companies_dict.append(line)
    print(len(companies_dict))
    print(companies_dict)

#Get data from log file
def get_data_from_log_file():
    file_pointer = open('log.dat','r')
    lines = file_pointer.readlines()
    log_data = dict()
    for ln in lines:
            if 'Status' in ln:
                log_data['status'] = ln[10:].strip()
            elif 'Job' in ln:
                log_data['job'] = ln[7:].strip()
    return log_data


#Write dic with log data into csv
def write_log_dict_into_csv():
    try:
        log_data = get_data_from_log_file()
        os.remove('log_out.csv')
        file_pointer = open('log_out.csv','w')
        writer = csv.DictWriter(file_pointer, fieldnames = ['status', 'job'])
        writer.writeheader()
        writer.writerow(log_data)
        #file_pointer.close()
    except IOError as io:
        print("I/O error: ", io)




def main():
    write_log_dict_into_csv()

if __name__ == "__main__":
    main()
