# encoding: utf-8
import pandas as pd
from backend.operation_system import get_root_path
import csv
from re import search
import string

encondig = "utf-8"


def write_file(file, name, telephone, celphone, sex, address, address_number, address_quarter, city, state):
    file_append = open(file, "a+")
    file_append.write(
        f'\n{name},{telephone},{celphone},{sex},{address},{address_number},{address_quarter},{city},{state}')
    file_append.close()


def path_file():
    path = get_root_path()
    file = path + "/data/phone_book_list.txt"
    # file = path + "/src/data/phone_book_list.txt"

    return file


def get_name_in_file(file):
    contact_list = []
    with open(file, mode='r', encoding=encondig) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        print(f'Names loaded:')
        for row in csv_reader:
            print(f'{row["Nome"]}')
            line_count += 1
            contact_list.append(row["Nome"])
    csv_file.close()
    print(f'Processed {line_count} lines.')
    contact_list.sort()

    return contact_list


def get_contact_list_info(element):
    file = path_file()
    if len(file) > 0:
        with open(file, mode='r', encoding=encondig) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row["Nome"] == element:
                    print(f'Contato encontrado na lista - > Será mostrado as infos --> {row["Nome"]}')
                    name = row["Nome"]
                    telephone = row["Telefone"]
                    celphone = row["Celular"]
                    sex = row["Sexo"]
                    address = row["Logradouro"]
                    address_number = row["Numero"]
                    address_quarter = row["Bairro"]
                    city = row["Cidade"]
                    state = row["Estado"]
        csv_file.close()
        return name, telephone, celphone, sex, address, address_number, address_quarter, city, state


def get_all_contact_list_info():
    name_list = []
    phone_list = []
    celphone_list = []
    sex_list = []
    address_list = []
    address_number_list = []
    address_quarter_list = []
    city_list = []
    state_list = []

    file = path_file()
    if len(file) > 0:
        with open(file, mode='r', encoding=encondig) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                name_list.append(row["Nome"])
                phone_list.append(row["Telefone"])
                celphone_list.append(row["Celular"])
                sex_list.append(row["Sexo"])
                address_list.append(row["Logradouro"])
                address_number_list.append(row["Numero"])
                address_quarter_list.append(row["Bairro"])
                city_list.append(row["Cidade"])
                state_list.append(row["Estado"])

        csv_file.close()
        return name_list, phone_list, celphone_list, sex_list, address_list, address_number_list, address_quarter_list, city_list, state_list


def check_contact(name):
    print(name)
    name = strip_string(name)
    file = path_file()
    with open(file, mode='r', encoding=encondig) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row["Nome"] == name:
                print("Contato encontrado na lista -> Não será adicionado")
                return 101
        if name == '':
            return 102
    csv_file.close()
    return 200


def strip_string(x):
    control = True
    while control:
        if search("  ", x):
            x = x.replace("  ", " ")
            print(x)
        else:
            control = False
        x = x.strip()
    return x


if __name__ == '__main__':
    write_file(path_file(), 'Giovani', 123645)
