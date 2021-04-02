import PySimpleGUI as sg
import frontend.setup


def popup_error_101(values):
    sg.popup('Já existe um contato com esse nome.\n'
             'Altere o nome do contato para que possa ser adicionado!',
             font=(frontend.setup.font, frontend.setup.font_size_text),
             background_color=frontend.setup.color_medium,
             title='[101] Erro ao adicionar contato',
             button_color=frontend.setup.color_hard)


def popup_error_102(values):
    sg.popup('Não é permitido adicionar um contato sem nome.\n'
             'Altere o nome do contato para que possa ser adicionado!',
             font=(frontend.setup.font, frontend.setup.font_size_text),
             background_color=frontend.setup.color_medium,
             title='[102] Erro ao adicionar contato',
             button_color=frontend.setup.color_hard)


def popup_to_do(values):
    sg.popup('Feature não implementada.\n'
             'Essa feature será implementado em versões futuras',
             font=(frontend.setup.font, frontend.setup.font_size_text),
             background_color=frontend.setup.color_medium,
             title='NÃO IMPLEMENTADO',
             button_color=frontend.setup.color_hard)
