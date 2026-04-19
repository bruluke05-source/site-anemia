from dados import VALORES_REF_SEXO, VALORES_REF_GERAIS, CRITERIOS_ANEMIA

# Arquivo contendo as funções que o programa possui 
# Cada função será uma verificação dos valores do usuário para testar o tipo de anemia


# Função 1: verifica se há anemia ou não 
def verificar_presenca_anemia(sexo, valores):
    rbc = valores["RBC"]
    hgb = valores["HGB"]
    ht = valores["HT"]

    criterios = CRITERIOS_ANEMIA.get(sexo.lower())
    if not criterios:
        return False, "Erro: Sexo inválido. Use 'homem ou 'mulher'."

    tem_anemia_clinica = (hgb < criterios["HGB_min"]) or (ht < criterios["HT_min"])
    tem_rbc_baixo = (rbc < criterios["RBC_min"])

    msg = "" 
    
    ## Situação 1: normalidade, sem anemia 
    if not tem_anemia_clinica and not tem_rbc_baixo:
        msg = ("\nDIAGNÓSTICO: Todos os parâmetros hematimétricos (HGB, HT, RBC) estão acima dos valores mínimos da faixa de normalidade. O paciente NÃO apresenta anemia. Caso VCM, HCM ou reticulócitos alterados, sugere repetir exame de sangue em 1 mês e solicitar perfil hepático (investigar presença de sintomas clínicos). Sugere suplementação caso ferro, B12 ou folato (B9) estiverem baixos. ")
        return False, msg 

    ## Situação 2: Apenas RBC baixo
    if (not tem_anemia_clinica) and tem_rbc_baixo:
        msg = ("\nATENÇÃO: Valores de HGB e HT estão dentro da normalidade, mas o número de eritrócitos (RBC) está baixo. ")
        msg += ("\nNão será feita a classificação de anemia. Sugere-se investigar possíveis causas adjacentes, como talassemia menor ou deficiência de ferro inicial. Sugere investigar possíveis deficiências nutricionais. ")
        return False, msg 

    ## Situação 3: Anemia confirmada
    return True, "\nDIAGNÓSTICO: Anemia clínica (HGB e/ou HT abaixo do limite mínimo da normalidade).\n"


# Função 2: se houver anemia, classifica o tipo de anemia de acordo com o volume corpuscular médio dos eritrócitos  
def classificar_por_vcm(vcm):
    vcm_min, vcm_max = VALORES_REF_GERAIS["VCM"]

    if vcm < vcm_min:          ## Se VCM < 80, anemia microcítica
        return "Microcitica"
    elif vcm > vcm_max:        ## Se VCM > 95, anemia macrocítica
        return "Macrocitica"
    else:                      ## Se há anemia com HT e HGB baixos mas VCM normal, anemia normocítica
        return "Normocitica"

        
# Função 3: se houver anemia, analisa a causa da anemia 
def investigar_causa_anemia(tipo_anemia, valores):
    resultado = ""

    ## 3.1 Anemia normocítica e normocrômica, VCM entre 80 e 95fL
    ### Próximo passo: análise do número de reticulócitos  
    if tipo_anemia == "Normocitica":
        retic = valores["RETIC"]
        resultado += "\nTipo: Anemia Normocítica e Normocrômica\n"
        resultado += "\nInterpretação com base no número de reticulócitos: "
        
        if retic < 0.5:
            resultado += "Reticulócitos baixos → Medula óssea hipoproliferativa (baixa eritropoetina - possível problema renal).\n"
            resultado += "Investigar: aplasias, infiltrações ou insuficiências medulares.\n"
            
        elif 0.5 <= retic <= 2:
            resultado += "Reticulócitos normais → Sugere hemorragia ou perda sanguínea.\n"
            resultado += "Investigar: sangramentos internos.\n"
            
        else:
            resultado += "Reticulócitos altos → Anemia hemolítica.\n"
            resultado += "Investigar: teste de Coombs, dosagem de bilirrubinas e haptoglobina.\n"

    ## 3.2 Anemia microcítica e hipocrômica, VCM abaixo de 80fL
    ### Próximo passo: dosar ferro e ferritina séricos para confirmação de anemia ferropriva, se não há alterações, pesquisar mutações moleculares 
    elif tipo_anemia == "Microcitica":
        ferro = valores["FERRO"]
        resultado += "\nTipo: Anemia Microcítica e Hipocrômica\n"
        resultado += "Avaliação do ferro sérico: "
        
        if ferro < 60:
            resultado += "Ferro baixo → Anemia ferropriva.\n"
            resultado += "Ação: dosar ferritina sérica e suplementar ferro.\n"
            
        elif 60 <= ferro <= 160:
            resultado += "Ferro normal → Hemoglobinopatias genéticas.\n"
            resultado += "Investigar: talassemias alfa/beta, anemia falciforme.\n"

        else:
            resultado += "Ferro alto → Anemia sideroblástica.\n"
            resultado += "Investigar: mutações na ALA sintetase e presença de sideroblastos em anel em esfregaço de medula óssea.\n"
            
    ## 3.3 Anemia macrocítica 
    ### Próximo passo: dosar vitamina B12 e folato séricos para confirmação de anemia megaloblástica, se não há alterações, pesquisar problemas medulares ou hepáticos
    elif tipo_anemia == "Macrocitica":
        b12 = valores["B12"]
        folato = valores["FOLATO"]
        resultado += "\nTipo: Anemia Macrocítica\n"
        resultado += "Avaliação de B12 ou folato: "
        
        if b12 < 160 or folato < 3:
           resultado += "Deficiência de B12 ou folato → Anemia megaloblástica.\n"
           resultado += "Ação: pesquisa de neutrófilos hipersegmentados em esfregaço sanguíneo, suplementação de B12 e folato, e pesquisa de anticorpos anti-fator intrínseco.\n"
            
        else:
            resultado += "B12/folato normais.\n"
            resultado += "Ação: avaliar esfregaço para reticulocitose e policromatofilia, presença de codócitos.\n"
            resultado += "Investigar: doenças hepáticas com alterações lipídicas ou mielodisplasias medulares.\n"

    return resultado + "\n"


# Função 4: analisa o tipo e causa, organiza as outras três funções e retorna ao menu
def analisar_anemia(sexo, valores):
    
    # 4.1 Chama a função 1 (verificar_presenca_anemia)
    tem_doenca, mensagem_inicial = verificar_presenca_anemia(sexo, valores)
    
    ## Se a triagem disse que não há anemia (False), retorna o laudo e encerra 
    if not tem_doenca:
        return mensagem_inicial

    ## Se tem anemia, ela guarda a primeira parte da mensagem e continua 
    laudo_final = mensagem_inicial
    
    # 4.2 Chama a função 2 (classificar_por_vcm)
    tipo_anemia = classificar_por_vcm(valores["VCM"])
    
    # 4.3 Chama a função 3 (investigar_causa_anemia)
    detalhes_causa = investigar_causa_anemia(tipo_anemia, valores)
    
    ## Junta as respostas e entrega para o menu
    laudo_final += detalhes_causa

    detalhes_formatado = detalhes_causa

    detalhes_formatado = detalhes_formatado.replace("Tipo:", "<br><b>Tipo:</b><br>")
    detalhes_formatado = detalhes_formatado.replace("Avaliação do ferro sérico:", "<br><b>Avaliação do ferro:</b><br>")
    detalhes_formatado = detalhes_formatado.replace("Ação:", "<br><b>Ação:</b><br>")

    laudo_final = f"""
<div style='text-align:left;'>

<h5 style='color:#0d6efd;'>🧾 Diagnóstico</h5>
<p>{mensagem_inicial}</p>

<h5 style='color:#198754;'>🧬 Tipo</h5>
<p>{tipo_anemia}</p>

<h5 style='color:#dc3545;'>🔬 Avaliação</h5>
<p>{detalhes_formatado}</p>

</div>
"""

    return laudo_final
