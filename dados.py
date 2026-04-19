# Arquivo contendo os dados utilizados como valores de referência pelo programa  

# Dicionário que guarda outros dicionários 'homem' e 'mulher' que contêm os intervalos de referências
## Intervalos de referência específicos por sexo (valores mínimo, máximo) 
VALORES_REF_SEXO = {
    "homem": {
        "RBC": (4.5, 6.5),    # Contagem de eritrócitos (em milhões/uL)
        "HGB": (13.5, 17.5),  # Hemoglobina (em g/dL)
        "HT": (40, 52)        # Hematócrito (em %)
    },
    "mulher": {
        "RBC": (3.9, 5.6),    # Contagem de eritrócitos (em milhões/uL)
        "HGB": (11.5, 15.5),  # Hemoglobina (em g/dL)
        "HT": (36, 48)        # Hematócrito (em %)
    }
}

# Dicionário que guarda os intervalos de referência gerais tanto para homem quanto mulheres (valores mínimos, máximo)
VALORES_REF_GERAIS = {
    "VCM": (80, 95),    # Volume Corpuscular Médio (em fL)
    "HCM": (27, 34),    # Hemoglobina Corpuscular Média (em pg)
    "CHCM": (30, 35),   # Concentração de Hemoglobina Corpuscular Média (em g/dL)
    "RETIC": (0.5, 2),  # Contagem de reticulócitos (em %)
    "FERRO": (60, 160), # Ferro sérico (ug/dL)
    "B12": (160, 925),  # Vitamina B12 (ng/dL)
    "FOLATO": (3, 15)   # Folato (ug/dL)
}

# Limites mínimos para critério de anemia 
CRITERIOS_ANEMIA = {
    "homem": {
        "HGB_min": 13.5,  # Valor de hemoglobina mínimo para homens (em g/dL)
        "HT_min": 40,     # Valor de hematócrito mínimo para homens (em %)
        "RBC_min": 4.5    # Valor de eritrócitos mínimo para homens (em milhões/uL)
    },
    "mulher": {
        "HGB_min": 11.5,  # Valor de hemoglobina mínimo para mulheres (em g/dL)
        "HT_min": 36,     # Valor de hematócrito mínimo para mulheres (em %)
        "RBC_min": 3.9    # Valor de eritrócitos mínimo para mulheres (em milhões/uL)
    }
}
