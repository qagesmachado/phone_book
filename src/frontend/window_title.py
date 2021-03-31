import frontend
import PySimpleGUI as sg


def window_title():
    layout = [
        [sg.Text('Lista de contados',
                 justification='center',
                 size=(85, 1), background_color=frontend.setup.color_light,
                 pad=(2, 2, 2, 2),
                 font=(frontend.setup.font, frontend.setup.font_size_title))]
    ]

    return layout

