import PySimpleGUI as sg
from frontend.popups.popup_errors import popup_error_101, popup_error_102, popup_to_do
from frontend.popups.popup_success import popup_success_add_contact
from frontend.window_main import main_layout
from frontend.window_book_list import window_add_contact
from backend.files import write_file, load_file, read_file, get_contact_list_info, check_contact, strip_string


def main():

    # Criar as janelas inicias
    w_main, w_add_contact, popup_101 = main_layout(), None, None

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
                popup_to_do(values)
            elif event == 'btn_reset':
                popup_to_do(values)
            elif event == 'btn_add':
                w_add_contact = window_add_contact()
                w_main.disable()
            elif event == 'btn_edit':
                popup_to_do(values)
            elif event == 'btn_delete':
                popup_to_do(values)
            elif event == 'btn_delete_all':
                popup_to_do(values)
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
                    name = values['contact_name']

                    validation = check_contact(name)

                    if validation == 200:
                        # print("Entrada válida")

                        # Tratamento dos inputs
                        name = strip_string(values['contact_name'])
                        telephone = strip_string(values['contact_phone'])
                        celphone = strip_string(values['contact_celphone'])
                        address = strip_string(values['contact_address'])
                        address_number = strip_string(values['contact_address_number'])
                        address_quarter = strip_string(values['contact_address_quarter'])
                        city = strip_string(values['contact_city'])
                        state = strip_string(values['contact_state'])
                        if values['sex_male']:
                            sex = 'Masculino'
                        else:
                            sex = 'Feminino'

                        # print(values)

                        write_file(load_file(), name, telephone, celphone, sex, address, address_number, address_quarter, city, state)
                        w_main.FindElement('li_values').Update(read_file(load_file()))
                        popup_success_add_contact(values)
                        w_add_contact.close()
                        w_main.enable()
                        w_main.bring_to_front()
                    elif validation == 101:
                        print('[ERRO 101] Já tem um contato com esse nome')
                        popup_error_101(values)
                    elif validation == 102:
                        print("[ERRO 202] Contato não pode ser vazio")
                        popup_error_102(values)
                elif event == 'btn_return':
                    w_add_contact.close()
                    w_main.enable()
                    w_main.bring_to_front()


if __name__ == '__main__':
    main()
