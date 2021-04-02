from backend.files import get_all_contact_list_info


def collect_statistics():
    name, telephone, celphone, sex, address, address_number, address_quarter, city, state = get_all_contact_list_info()
    # print(name)
    # print(telephone)
    # print(celphone)
    # print(sex)
    # print(address)
    # print(address_number)
    # print(address_quarter)
    # print(city)
    # print(state)

    list_len = len(name)

    f = 0
    m = 0
    n = 0
    for i in sex:
        if i == 'Feminino':
            f = f + 1
        elif i == 'Masculino':
            m = m + 1
        elif i == 'Nao definido':
            n = n + 1
    return list_len, m, f, n


if __name__ == '__main__':
    collect_statistics()