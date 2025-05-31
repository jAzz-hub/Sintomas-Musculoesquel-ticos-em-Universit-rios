ordinal_mappings = {
    'Quanto você se preocupou com a sua dor ou com o desconforto físico?  ': {
        'Mais ou menos': 3,
        'Muito pouco': 2,
        'Bastante': 4,
        'Nada': 1,
        'Extremamente': 5
    },
    'Quanto você se preocupou com a sua saúde?  ': {
        'Mais ou menos': 3,
        'Bastante': 4,
        'Extremamente': 5,
        'Muito pouco': 2,
        'Nada': 1
    },
    'Em que medida você acha que a sua dor (física) te impede de fazer o que precisa?  ': {
        'Bastante': 4,
        'Muito pouco': 2,
        'Mais ou menos': 3,
        'Nada': 1,
        'Extremamente': 5
    },
    'Você tem alguma dificuldade para dormir ou dificuldade com o sono?   ': {
        'Mais ou menos': 3,
        'Extremamente': 5,
        'Muito pouco': 2,
        'Bastante': 4,
        'Nada': 1
    },
    'Em que medida você tem dificuldade para exercer suas atividades diárias?  ': {
        'Mais ou menos': 3,
        'Nada': 1,
        'Bastante': 4,
        'Muito pouco': 2,
        'Extremamente': 5
    },
    'Qual a sua frequência de atividades físicas semanais?  ': {
        'Nada': 1,
        '5 a 6 dias': 4,
        '1 a 2 dias': 2,
        'Todos os dias': 5,
        '3 a 4 dias': 3
    },
    'Com que frequência você utiliza dispositivos eletrônicos?   ': {
        'Extremamente': 5,
        'Bastante': 4,
        'Nada': 1,
        'Mais ou menos': 3,
        'Muito pouco': 2
    },
    'Você fica sentado estudando em média quantas horas por dia? ': {
        '3 horas': 2,
        '4 horas': 3,
        '1 a 2 horas': 1,
        '6 horas ou mais': 5,
        '5 horas': 4
    },
    'As suas atividades acadêmicas/estágios influenciam nas dores que sente? ': {
        'Muito pouco': 2,
        'Bastante': 4,
        'Mais ou menos': 3,
        'Nada': 1,
        'Extremamente': 5
    },
    'Você se sente muito estressado/ansioso? ': {
        'Bastante': 4,
        'Extremamente': 5,
        'Muito pouco': 2,
        'Mais ou menos': 3,
        'Nada': 1
    },
    'Afirmação de dormência ou formigamento sentidos nos últimos 6 mêses': {
        'Se SIM, em qual região?': None,  # campo aberto, não ordinal
        'Sim': 2,
        'Não': 1,
        'às vezes ': 1.5  # você pode ajustar esse valor conforme desejar tratá-lo
    },
    'Não realização de lazer, atividades domésticas ou trabalho por formigamento ou dormência sentidos nos últimos 6 mêses': {
        'Sim': 2,
        'Não': 1
    },
    'Afirmação de consulta com profissionais da saúde por causa das condições de dormência ou formigamento': {
        'Não': 1,
        'Sim': 2
    },
    'Afirmação de sintoma musculoesquelético nos últimos 7 dias': {
        'Sim': 2,
        'Não sei ': 1.5,
        'Não': 1
    }

    # ----------------------------------------------------------
    # Colunas Binárias e Especiais
    # ----------------------------------------------------------
    # 'SEXO': {
    #     'FEMININO': 0,
    #     'MASCULINO': 1
    # },
    # 'Não realização de lazer, atividades domésticas ou trabalho por formigamento ou dormência sentidos nos últimos 6 mêses': {
    #     'Não': 0,
    #     'Sim': 1
    # },
    # 'Afirmação de consulta com profissionais da saúde por causa das condições de dormência ou formigamento': {
    #     'Não': 0,
    #     'Sim': 1
    # }
}

ordinal_inverse_mappings = {
    'Quanto você se preocupou com a sua dor ou com o desconforto físico?  ': {
        1: 'Nada',
        2: 'Muito pouco',
        3: 'Mais ou menos',
        4: 'Bastante',
        5: 'Extremamente'
    },
    'Quanto você se preocupou com a sua saúde?  ': {
        1: 'Nada',
        2: 'Muito pouco',
        3: 'Mais ou menos',
        4: 'Bastante',
        5: 'Extremamente'
    },
    'Em que medida você acha que a sua dor (física) te impede de fazer o que precisa?  ': {
        1: 'Nada',
        2: 'Muito pouco',
        3: 'Mais ou menos',
        4: 'Bastante',
        5: 'Extremamente'
    },
    'Você tem alguma dificuldade para dormir ou dificuldade com o sono?   ': {
        1: 'Nada',
        2: 'Muito pouco',
        3: 'Mais ou menos',
        4: 'Bastante',
        5: 'Extremamente'
    },
    'Em que medida você tem dificuldade para exercer suas atividades diárias?  ': {
        1: 'Nada',
        2: 'Muito pouco',
        3: 'Mais ou menos',
        4: 'Bastante',
        5: 'Extremamente'
    },
    'Qual a sua frequência de atividades físicas semanais?  ': {
        1: 'Nada',
        2: '1 a 2 dias',
        3: '3 a 4 dias',
        4: '5 a 6 dias',
        5: 'Todos os dias'
    },
    'Com que frequência você utiliza dispositivos eletrônicos?   ': {
        1: 'Nada',
        2: 'Muito pouco',
        3: 'Mais ou menos',
        4: 'Bastante',
        5: 'Extremamente'
    },
    'Você fica sentado estudando em média quantas horas por dia? ': {
        1: '1 a 2 horas',
        2: '3 horas',
        3: '4 horas',
        4: '5 horas',
        5: '6 horas ou mais'
    },
    'As suas atividades acadêmicas/estágios influenciam nas dores que sente? ': {
        1: 'Nada',
        2: 'Muito pouco',
        3: 'Mais ou menos',
        4: 'Bastante',
        5: 'Extremamente'
    },
    'Você se sente muito estressado/ansioso? ': {
        1: 'Nada',
        2: 'Muito pouco',
        3: 'Mais ou menos',
        4: 'Bastante',
        5: 'Extremamente'
    },
    'Afirmação de dormência ou formigamento sentidos nos últimos 6 mêses': {
        1: 'Não',
        1.5: 'Às vezes',
        2: 'Sim'
    },
    'Não realização de lazer, atividades domésticas ou trabalho por formigamento ou dormência sentidos nos últimos 6 mêses': {
        1: 'Não',
        2: 'Sim'
    },
    'Afirmação de consulta com profissionais da saúde por causa das condições de dormência ou formigamento': {
        1: 'Não',
        2: 'Sim'
    },
    'Afirmação de sintoma musculoesquelético nos últimos 7 dias': {
        1: 'Não',
        1.5: 'Não sei',
        2: 'Sim'
    }
}
# for col, mapping in ordinal_mappings.items():
#     # Ignora categorias com valor None
#     reverse_mapping = {v: k for k, v in mapping.items() if v is not None}
#     ordinal_inverse_mappings[col] = reverse_mapping
