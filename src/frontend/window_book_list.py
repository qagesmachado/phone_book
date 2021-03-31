import PySimpleGUI as sg
import frontend.setup


def window_book_list(values):
    layout = [
        [sg.Input('',
                  font=(frontend.setup.font, frontend.setup.font_size_text),
                  pad=((5, 1), (1, 5)),
                  background_color=frontend.setup.color_medium,
                  key='in_search',
                  size=(40, 1)),
         sg.Button('Procurar',
                   font=(frontend.setup.font, frontend.setup.font_size_text),
                   pad=((7, 3), (1, 5)),
                   button_color=frontend.setup.color_hard,
                   key='btn_search'),
         sg.Button('Resetar',
                   font=(frontend.setup.font, frontend.setup.font_size_text),
                   pad=((5, 1), (1, 5)),
                   button_color=frontend.setup.color_hard,
                   key='btn_reset'),
         ],
        [sg.Listbox(values=values,
                    size=(56, 23),
                    key='li_values',
                    font=(frontend.setup.font, frontend.setup.font_size_text),
                    pad=((5, 5), (1, 1)),
                    text_color='black',
                    background_color=frontend.setup.color_light,
                    change_submits=True)
         ],
        [sg.Button('Adicionar Contatos',
                   font=(frontend.setup.font, frontend.setup.font_size_text),
                   pad=((5, 1), (5, 5)),
                   button_color=frontend.setup.color_hard,
                   key='btn_add'),
         sg.Button('Apagar Contato',
                   font=(frontend.setup.font, frontend.setup.font_size_text),
                   pad=((5, 1), (5, 5)),
                   button_color=frontend.setup.color_hard,
                   key='btn_delete'),
         sg.Button('Apagar Todos',
                   font=(frontend.setup.font, frontend.setup.font_size_text),
                   pad=((5, 1), (5, 5)),
                   button_color=frontend.setup.color_hard,
                   key='btn_delete_all')
         ]
    ]

    return layout


def window_add_contact():
    sg.theme(frontend.setup.window_theme)

    layout = [
        # Linha 1 - Titulo
        [sg.Text('Informe os dados do novo contato',
                 justification='center',
                 size=(40, 1),
                 background_color=frontend.setup.color_light,
                 pad=((2, 2), (2, 2)),
                 font=(frontend.setup.font, frontend.setup.font_size_title))],
        # Linha 2 - Nome
        [sg.Text('Nome  ',
                 font=(frontend.setup.font, frontend.setup.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.setup.color_light),
         sg.Input('',
                  font=(frontend.setup.font, frontend.setup.font_size_text),
                  pad=((1, 1), (1, 2)),
                  background_color=frontend.setup.color_hard,
                  key='contact_name',
                  size=(25, 1),
                  text_color=frontend.setup.text_color)
         ],
        # Linha 3 - Telefone e celular
        [sg.Text('Telefone  ',
                 font=(frontend.setup.font, frontend.setup.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.setup.color_light),
         sg.Input('',
                  font=(frontend.setup.font, frontend.setup.font_size_text),
                  pad=((1, 1), (1, 2)),
                  background_color=frontend.setup.color_hard,
                  key='contact_phone',
                  size=(15, 1),
                  text_color=frontend.setup.text_color),
         sg.Text('Celular  ',
                 font=(frontend.setup.font, frontend.setup.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.setup.color_light),
         sg.Input('', font=(frontend.setup.font, frontend.setup.font_size_text),
                  pad=((1, 1), (1, 2)),
                  background_color=frontend.setup.color_hard,
                  key='contact_celphone',
                  size=(15, 1),
                  text_color=frontend.setup.text_color)

         ],
        # Linha 4 - Sexo
        [sg.Text('Sexo  ',
                 font=(frontend.setup.font, frontend.setup.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.setup.color_light),
         sg.Input('', font=(frontend.setup.font, frontend.setup.font_size_text),
                  pad=((1, 1), (1, 2)),
                  background_color=frontend.setup.color_hard,
                  key='contact_sex',
                  size=(25, 1),
                  text_color=frontend.setup.text_color)

         ],
        # Linha 5 - Endereço e numero
        [sg.Text('Logradouro  ',
                 font=(frontend.setup.font, frontend.setup.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.setup.color_light),
         sg.Input('', font=(frontend.setup.font, frontend.setup.font_size_text),
                  pad=((1, 1), (1, 2)),
                  background_color=frontend.setup.color_hard,
                  key='contact_address',
                  size=(24, 1),
                  text_color=frontend.setup.text_color),
         sg.Text('Número  ',
                 font=(frontend.setup.font, frontend.setup.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.setup.color_light),
         sg.Input('', font=(frontend.setup.font, frontend.setup.font_size_text),
                  pad=((1, 1), (1, 2)),
                  background_color=frontend.setup.color_hard,
                  key='contact_address_number',
                  size=(4, 1),
                  text_color=frontend.setup.text_color)

         ],
        # Linha 6 - Bairro
        [sg.Text('Bairro  ',
                 font=(frontend.setup.font, frontend.setup.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.setup.color_light),
         sg.Input('', font=(frontend.setup.font, frontend.setup.font_size_text),
                  pad=((1, 1), (1, 2)),
                  background_color=frontend.setup.color_hard,
                  key='contact_address_quarter',
                  size=(25, 1),
                  text_color=frontend.setup.text_color)
         ],
        # Linha 7 - Cidade e estado
        [sg.Text('Cidade  ',
                 font=(frontend.setup.font, frontend.setup.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.setup.color_light),
         sg.Input('',
                  font=(frontend.setup.font, frontend.setup.font_size_text),
                  pad=((1, 1), (1, 2)),
                  background_color=frontend.setup.color_hard,
                  key='contact_city',
                  size=(17, 1),
                  text_color=frontend.setup.text_color),
         sg.Text('Estado  ',
                 font=(frontend.setup.font, frontend.setup.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.setup.color_light),
         sg.Input('',
                  font=(frontend.setup.font, frontend.setup.font_size_text),
                  pad=((1, 1), (1, 2)),
                  background_color=frontend.setup.color_hard,
                  key='contact_state',
                  size=(16, 1),
                  text_color=frontend.setup.text_color)
         ],
        [sg.Button('Adicionar',
                   font=(frontend.setup.font, frontend.setup.font_size_text),
                   pad=((5, 5), (1, 5)),
                   button_color=frontend.setup.color_hard,
                   key='btn_add'),
         sg.Button('Voltar',
                   font=(frontend.setup.font, frontend.setup.font_size_text),
                   pad=((5, 5), (1, 5)),
                   button_color=frontend.setup.color_hard,
                   key='btn_return')
         ]
    ]

    return sg.Window('Adicionar Contato', layout=layout, finalize=True,
                     background_color=frontend.setup.color_light).Finalize()