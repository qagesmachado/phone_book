# encoding: utf-8
import PySimpleGUI as sg

from backend.contact_statistics import collect_statistics
from frontend.popups.popup_errors import popup_error_101, popup_error_102, popup_to_do, popup_error_103
from frontend.popups.popup_question import popup_question_delete_contact
from frontend.popups.popup_success import popup_success_add_contact
from frontend.window_main import main_layout
from frontend.window_book_list import window_add_contact
from backend.files import write_file, path_file, get_name_in_file, get_contact_list_info, check_contact, strip_string, \
    delete_one_element_list, read_lines


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
                if len(values['in_search']) == 0:
                    w_main.FindElement('li_values').Update(get_name_in_file(path_file()))
                else:
                    popup_to_do(values)
            elif event == 'btn_reset':
                popup_to_do(values)
            elif event == 'btn_add':
                w_add_contact = window_add_contact()
                w_main.disable()
            elif event == 'btn_edit':
                # popup_to_do(values)
                read_lines()
            elif event == 'btn_delete':
                try:
                    element_list = values['li_values'][0]
                    pop_up_result = popup_question_delete_contact(element_list)
                    if pop_up_result == 'Yes':

                        # Remove
                        delete_one_element_list(element_list)

                        # # UPDATE APP

                        # # Update contact info
                        w_main.FindElement('contact_name').Update('')
                        w_main.FindElement('contact_phone').Update('')
                        w_main.FindElement('contact_celphone').Update('')
                        w_main.FindElement('contact_sex').Update('')
                        w_main.FindElement('contact_address').Update('')
                        w_main.FindElement('contact_address_number').Update('')
                        w_main.FindElement('contact_address_quarter').Update('')
                        w_main.FindElement('contact_city').Update('')
                        w_main.FindElement('contact_state').Update('')

                        # # Update listbox
                        w_main.FindElement('li_values').Update(get_name_in_file(path_file()))

                        # update statistics
                        list_len, m, f, n, m_percent, f_percent, n_percent = collect_statistics()
                        w_main.FindElement('qtd_total').Update(list_len)
                        w_main.FindElement('qtd_men').Update(m)
                        w_main.FindElement('qtd_women').Update(f)
                        w_main.FindElement('qtd_none').Update(n)
                        w_main.FindElement('qtd_men_pct').Update(m_percent)
                        w_main.FindElement('qtd_women_pct').Update(f_percent)
                        w_main.FindElement('qtd_none_pct').Update(n_percent)

                except IndexError:
                    'list index out of range'
                    popup_error_103(values)

            elif event == 'btn_delete_all':
                popup_to_do(values)
            elif event == 'li_values':
                if len(get_name_in_file(path_file())) > 0:
                    element_list = values['li_values'][0]
                    name, telephone, celphone, sex, address, address_number, address_quarter, city, state = get_contact_list_info(
                        element_list)

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
                        elif values['sex_female']:
                            sex = 'Feminino'
                        elif values['sex_none']:
                            sex = 'Não definido'

                        # print(values)

                        write_file(path_file(), name, telephone, celphone, sex, address, address_number,
                                   address_quarter, city, state)
                        w_main.FindElement('li_values').Update(get_name_in_file(path_file()))

                        # update statistics
                        list_len, m, f, n, m_percent, f_percent, n_percent = collect_statistics()
                        w_main.FindElement('qtd_total').Update(list_len)
                        w_main.FindElement('qtd_men').Update(m)
                        w_main.FindElement('qtd_women').Update(f)
                        w_main.FindElement('qtd_none').Update(n)
                        w_main.FindElement('qtd_men_pct').Update(m_percent)
                        w_main.FindElement('qtd_women_pct').Update(f_percent)
                        w_main.FindElement('qtd_none_pct').Update(n_percent)

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
