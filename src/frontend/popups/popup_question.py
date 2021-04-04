import PySimpleGUI as sg
import frontend.initial_setup_frontend


def popup_question_delete_contact(values):
    if sg.popup_yes_no(f'Deseja excluir o contato {values}?',
                       font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                       background_color=frontend.initial_setup_frontend.color_medium,
                       title='Excluir Contato!',
                       button_color=frontend.initial_setup_frontend.color_hard,
                       ) == 'Yes':
        return 'Yes'
