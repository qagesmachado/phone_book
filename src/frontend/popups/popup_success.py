import PySimpleGUI as sg
import frontend.setup


def popup_success_add_contact(values):
    sg.popup('Contato adicionado com sucesso!',
             font=(frontend.setup.font, frontend.setup.font_size_text),
             background_color=frontend.setup.color_medium,
             title='Sucesso!',
             button_color=frontend.setup.color_hard)
