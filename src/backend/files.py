import pandas as pd
from backend.operation_system import get_root_path
import csv


def write_file(file, name, telephone, celphone, sex, address, address_number, address_quarter, city, state):
    file_append = open(file, "a+")
    file_append.write(
        f'\n{name},{telephone},{celphone},{sex},{address},{address_number},{address_quarter},{city},{state}')
    file_append.close()


def load_file():
    path = get_root_path()
    file = path + "/data/phone_book_list.txt"
    # file = path + "/src/data/phone_book_list.txt"

    return file


def read_file(file):
    contact_list = []
    telephone_list = []

    with open(file, mode='r', encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            # print(f'\t{row["Nome"]} - {row["Telefone"]}')
            line_count += 1
            contact_list.append(row["Nome"])
            telephone_list.append(row["Telefone"])

        # print(f'Processed {line_count} lines.')
        contact_list.sort()
        return contact_list

def get_contact_list_info(element):
    file = load_file()
    if len(file) > 0:
        with open(file, mode='r', encoding='utf8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row["Nome"] == element:
                    print("Contato na lista")
                    name = row["Nome"]
                    telephone = row["Telefone"]
                    celphone = row["Celular"]
                    sex = row["Sexo"]
                    address = row["Logradouro"]
                    address_number = row["Número"]
                    address_quarter = row["Bairro"]
                    city = row["Cidade"]
                    state = row["Estado"]
            return name, telephone, celphone, sex, address, address_number, address_quarter, city, state




if __name__ == '__main__':
    write_file(load_file(), 'Giovani', 123645)