import PySimpleGUI as sg
from backend import operation_system


def window_logo():

    root_dir = operation_system.get_root_path()
    # Image Directory
    file_name = root_dir + '\\images\\phone_book_image.png'

    layout = [
        [sg.Image(file_name,
                  key="imageContainer",
                  pad=((1, 1), (1, 1))),
         ],
    ]

    return layout

