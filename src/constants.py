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
    'Nos últimos 6 MESES, você teve problemas (como formigamento, dor ou dormência) em alguma parte do corpo: ': {
        'Se SIM, em qual região?': None,  # campo aberto, não ordinal
        'Sim': 2,
        'Não': 1,
        'às vezes ': 1.5  # você pode ajustar esse valor conforme desejar tratá-lo
    },
    'Nos últimos 6 MESES, você foi impedido de realizar suas atividades normais (trabalho, atividades domésticas e de lazer) por causa desses problemas?': {
        'Sim': 2,
        'Não': 1
    },
    'Nos últimos 6 MESES, você consultou algum profissional da área da saúde (médico, fisioterapeuta) por causa dessa condição?': {
        'Não': 1,
        'Sim': 2
    },
    'Nos últimos 7 DIAS, você teve/tem algum problema/sintoma musculoesquelético?': {
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
    # 'Nos últimos 6 MESES, você foi impedido de realizar suas atividades normais (trabalho, atividades domésticas e de lazer) por causa desses problemas?': {
    #     'Não': 0,
    #     'Sim': 1
    # },
    # 'Nos últimos 6 MESES, você consultou algum profissional da área da saúde (médico, fisioterapeuta) por causa dessa condição?': {
    #     'Não': 0,
    #     'Sim': 1
    # }
}

ordinal_inverse_mappings = {}

for col, mapping in ordinal_mappings.items():
    # Ignora categorias com valor None
    reverse_mapping = {v: k for k, v in mapping.items() if v is not None}
    ordinal_inverse_mappings[col] = reverse_mapping

