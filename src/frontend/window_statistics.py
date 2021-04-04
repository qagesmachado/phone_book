import PySimpleGUI as sg
import frontend.initial_setup_frontend


def window_statistics(list_len, m, f, n, m_percent, f_percent, n_percent):
    layout = [
        # Linha 1
        [sg.Text('Estatísticas dos Contatos',
                 size=(47, 1),
                 justification='center',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((5, 5), (1, 2)), background_color=frontend.initial_setup_frontend.color_light)
         ],
        # Linha 2
        [sg.Text('Quantidade de Contatos: ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((5, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text(list_len,
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='qtd_total',
                 size=(5, 1))
         ],
        # Linha 2
        [sg.Text('Quantidade de Homens: ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((5, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text(m,
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='qtd_men',
                 size=(5, 1)),
         sg.Text('Porcentagem: ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((5, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text(m_percent,
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='qtd_men_pct',
                 size=(5, 1))
         ],
        # Linha 3
        [sg.Text('Quantidade de Mulheres: ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((5, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text(f,
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='qtd_women',
                 size=(5, 1)),
         sg.Text('Porcentagem: ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((5, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text(f_percent,
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='qtd_women_pct',
                 size=(5, 1))
         ],
        # Linha 4
        [sg.Text('Quantidade não definido: ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((5, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text(n,
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='qtd_none',
                 size=(5, 1)),
         sg.Text('Porcentagem: ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((5, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text(n_percent,
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='qtd_none_pct',
                 size=(5, 1))
         ]
    ]
    return layout
