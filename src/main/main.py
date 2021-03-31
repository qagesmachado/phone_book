import PySimpleGUI as sg
from frontend.window_main import main_layout
from frontend.window_book_list import window_add_contact
from backend.files import write_file, load_file, read_file, get_contact_list_info


def main():

    # Criar as janelas inicias
    w_main, w_add_contact = main_layout(), None

    while True:
        window, event, values = sg.read_all_windows()

        # # Fechar tela
        if window == w_main and event == sg.WIN_CLOSED:
            break
        elif window == w_add_contact and event == sg.WIN_CLOSED:
            w_add_contact.close()
            w_main.enable()
            w_main.bring_to_front()

        if window == w_main:
            if event == 'btn_search':
                pass
            elif event == 'btn_reset':
                pass
            elif event == 'btn_add':
                w_add_contact = window_add_contact()
                w_main.disable()
            elif event == 'btn_delete':
                pass
            elif event == 'btn_delete_all':
                pass
            elif event == 'li_values':
                if len(read_file(load_file())) > 0:
                    element_list = values['li_values'][0]
                    name, telephone, celphone, sex, address, address_number, address_quarter, city, state = get_contact_list_info(element_list)

                    w_main.FindElement('contact_name').Update(name)
                    w_main.FindElement('contact_phone').Update(telephone)
                    w_main.FindElement('contact_celphone').Update(celphone)
                    w_main.FindElement('contact_sex').Update(sex)
                    w_main.FindElement('contact_address').Update(address)
                    w_main.FindElement('contact_address_number').Update(address_number)
                    w_main.FindElement('contact_address_quarter').Update(address_quarter)
                    w_main.FindElement('contact_city').Update(city)
                    w_main.FindElement('contact_state').Update(state)
        if window == w_add_contact:
            if window == w_add_contact:
                if event == 'btn_add':
                    w_add_contact.close()
                    w_main.enable()
                    w_main.bring_to_front()

                    print(values)

                    name = values['contact_name']
                    telephone = values['contact_phone']
                    celphone = values['contact_celphone']
                    sex = values['contact_sex']
                    address = values['contact_address']
                    address_number = values['contact_address_number']
                    address_quarter = values['contact_address_quarter']
                    city = values['contact_city']
                    state = values['contact_state']
                    print(name, telephone, celphone, sex, address, address_number, address_quarter, city, state)
                    write_file(load_file(), name, telephone, celphone, sex, address, address_number, address_quarter, city, state)

                    w_main.FindElement('li_values').Update(read_file(load_file()))

                elif event == 'btn_return':
                    w_add_contact.close()
                    w_main.enable()
                    w_main.bring_to_front()


        # # w_phone_statistics
        # if window == w_phone_statistics:
        #     if event == 'Voltar':
        #         w_phone_statistics.hide()
        #         w_phone_book_initial = window_phone_book_initial()

        # # w_add_contact
        # if window == w_add_contact:
        #     if event == 'Adicionar':
        #         w_add_contact.close()
        #
        #         name = values[0]
        #         telephone = values[1]
        #         print(name, telephone)
        #         write_file(load_file(), name, telephone)
        #
        #         w_phone_list.FindElement('values_list').Update(read_file(load_file()))
        #
        #     elif event == 'Voltar':
        #         w_phone_book_initial.hide()
        #         w_phone_list = window_phone_list()
        #

if __name__ == '__main__':
    # name = 'Gustavo Eduardo Silva Machado'
    # phone = '34991077043'
    # sex = 'Masculino'
    # address = 'Rua Pádua e Castro, 166'
    # city = 'Campinas'
    # state = 'São Paulo'
    main()
