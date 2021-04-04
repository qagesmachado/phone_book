import PySimpleGUI as sg
import frontend.initial_setup_frontend
from backend import operation_system
from backend.contact_statistics import collect_statistics
from backend.files import path_file, get_name_in_file
from frontend.window_book_list import window_book_list
from frontend.window_info import window_info
from frontend.window_logo import window_logo
from frontend.window_show import window_show
from frontend.window_statistics import window_statistics
from frontend.window_title import window_title


def main_layout():
    # theme
    sg.theme(frontend.initial_setup_frontend.window_theme)

    # load data
    values = get_name_in_file(path_file())
    list_len, m, f, n, m_percent, f_percent, n_percent = collect_statistics()

    layout_title = window_title()
    layout_list = window_book_list(values)
    layout_logo = window_logo()
    layout_info = window_info()
    layout_show = window_show()
    layout_statistics = window_statistics(list_len, m, f, n, m_percent, f_percent, n_percent)

    col1 = [
        [sg.Column(layout_logo, background_color=frontend.initial_setup_frontend.color_light, size=(140, 140), justification='top'), sg.Column(layout_show, background_color=frontend.initial_setup_frontend.color_light, size=(300, 140))],
        [sg.Column(layout_info, size=(449, 200), background_color=frontend.initial_setup_frontend.color_light)],
        [sg.Column(layout_statistics, size=(433, 200), background_color=frontend.initial_setup_frontend.color_light, scrollable=True, vertical_scroll_only=True)]
    ]

    layout_main =[
        [sg.Column(layout_title, background_color=frontend.initial_setup_frontend.color_medium, size=(1000, 35), pad=(1, 1, 1, 1))],
        [sg.Column(col1, background_color=frontend.initial_setup_frontend.color_medium, pad=(1, 1, 1, 1)), sg.Column(layout_list, background_color=frontend.initial_setup_frontend.color_light, size=(500, 511), pad=(1, 1, 1, 1))],
    ]

    return sg.Window('Lista de Contatos', layout=layout_main, finalize=True, size=(970, 560), background_color=frontend.initial_setup_frontend.color_medium).Finalize()


if __name__ == '__main__':
    pass
