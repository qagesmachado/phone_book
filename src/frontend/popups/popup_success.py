import PySimpleGUI as sg
import frontend.initial_setup_frontend


def popup_success_add_contact(values):
    sg.popup('Contato adicionado com sucesso!',
             font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
             background_color=frontend.initial_setup_frontend.color_medium,
             title='Sucesso!',
             button_color=frontend.initial_setup_frontend.color_hard)
