import frontend
import PySimpleGUI as sg


def window_title():
    layout = [
        [sg.Text('Lista de contados',
                 justification='center',
                 size=(85, 1), background_color=frontend.initial_setup_frontend.color_light,
                 pad=(2, 2, 2, 2),
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_title))]
    ]

    return layout

