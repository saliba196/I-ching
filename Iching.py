import random
hexagramas = {
    1: 'Hexagrama 1: O Criativo (Qian) - Ação forte e liderança.',
    2: 'Hexagrama 2: O Receptivo (Kun) - Energia receptiva e adaptável.',
    3: 'Hexagrama 3: A Dificuldade Inicial (Zhun) - Desafios e obstáculos no começo.',
    4: 'Hexagrama 4: A Insensatez Juvenil (Meng) - Aprendizado e crescimento com erros.',
    5: 'Hexagrama 5: A Espera (Xu) - A paciência é necessária antes de agir.',
    6: 'Hexagrama 6: O Conflito (Song) - Desacordos ou disputas.',
    7: 'Hexagrama 7: O Exército (Shi) - Organização e disciplina são necessárias.',
    8: 'Hexagrama 8: Manter-se Unido (Bi) - União e solidariedade.',
    9: 'Hexagrama 9: A Força Domesticadora do Pequeno (Xiao Chu) - Progresso gradual com pequenos esforços.',
    10: 'Hexagrama 10: O Comportamento (Lu) - Cautela em situações difíceis.',
    11: 'Hexagrama 11: A Paz (Tai) - Harmonia e equilíbrio.',
    12: 'Hexagrama 12: O Estancamento (Pi) - Estagnação e falta de progresso.',
    13: 'Hexagrama 13: A Comunidade (Tong Ren) - Cooperação com os outros.',
    14: 'Hexagrama 14: Grande Possessão (Da You) - Abundância e prosperidade.',
    15: 'Hexagrama 15: A Modéstia (Qian) - Humildade leva ao sucesso.',
    16: 'Hexagrama 16: O Entusiasmo (Yu) - Energia e otimismo impulsionam o progresso.',
    17: 'Hexagrama 17: O Seguimento (Sui) - Adaptação e aceitação das mudanças.',
    18: 'Hexagrama 18: Trabalho no que foi Corrompido (Gu) - Corrigir erros do passado.',
    19: 'Hexagrama 19: A Aproximação (Lin) - Oportunidade à vista.',
    20: 'Hexagrama 20: A Contemplação (Guan) - Reflexão e observação.',
    21: 'Hexagrama 21: Mordendo (Shi He) - Resolver conflitos de forma decisiva.',
    22: 'Hexagrama 22: A Graça (Bi) - Elegância e aparência importam.',
    23: 'Hexagrama 23: O Despedaçamento (Bo) - Deterioração e declínio.',
    24: 'Hexagrama 24: O Retorno (Fu) - Ciclos de renovação e retorno.',
    25: 'Hexagrama 25: A Inocência (Wu Wang) - Agir com intenções puras.',
    26: 'Hexagrama 26: A Força Domesticadora do Grande (Da Chu) - Autodisciplina e contenção.',
    27: 'Hexagrama 27: O Canto da Boca (Yi) - Nutrição e cuidado.',
    28: 'Hexagrama 28: A Preponderância do Grande (Da Guo) - Grande responsabilidade ou peso.',
    29: 'Hexagrama 29: O Abismal (Kan) - Perigo e desafios pela frente.',
    30: 'Hexagrama 30: O Aderir (Li) - Clareza e iluminação.',
    31: 'Hexagrama 31: A Influência (Xian) - Atração e influência sutil.',
    32: 'Hexagrama 32: A Durabilidade (Heng) - Perseverança e compromisso a longo prazo.',
    33: 'Hexagrama 33: A Retirada (Dun) - Retirada diante da adversidade.',
    34: 'Hexagrama 34: O Poder do Grande (Da Zhuang) - Ação forte e assertiva.',
    35: 'Hexagrama 35: O Progresso (Jin) - Avanço constante.',
    36: 'Hexagrama 36: O Escurecimento da Luz (Ming Yi) - Ocultar a própria luz em tempos difíceis.',
    37: 'Hexagrama 37: A Família (Jia Ren) - Harmonia e ordem doméstica.',
    38: 'Hexagrama 38: A Oposição (Kui) - Divergência e desacordos.',
    39: 'Hexagrama 39: O Impedimento (Jian) - Obstáculos bloqueiam o caminho.',
    40: 'Hexagrama 40: A Libertação (Jie) - Um caminho para sair das dificuldades.',
    41: 'Hexagrama 41: A Diminuição (Sun) - Redução ou sacrifício voluntário.',
    42: 'Hexagrama 42: O Aumento (Yi) - Crescimento e expansão.',
    43: 'Hexagrama 43: O Rompimento (Guai) - Ação decisiva é necessária.',
    44: 'Hexagrama 44: O Encontrar (Gou) - Uma força poderosa se aproxima.',
    45: 'Hexagrama 45: A Reunião (Cui) - Esforço coletivo e unidade.',
    46: 'Hexagrama 46: Subida (Sheng) - Progresso e avanço constante.',
    47: 'Hexagrama 47: A Opressão (Kun) - Dificuldade e exaustão.',
    48: 'Hexagrama 48: O Poço (Jing) - Nutrição e revitalização.',
    49: 'Hexagrama 49: A Revolução (Ge) - Transformação e mudança.',
    50: 'Hexagrama 50: O Caldeirão (Ding) - Cultivo espiritual e nutrição.',
    51: 'Hexagrama 51: O Despertar (Zhen) - Choque e mudança repentina.',
    52: 'Hexagrama 52: A Quietude (Gen) - Estabilidade e meditação.',
    53: 'Hexagrama 53: O Desenvolvimento (Jian) - Progresso gradual e evolução.',
    54: 'Hexagrama 54: A Jovem que se Casa (Gui Mei) - Inexperiência e novos começos.',
    55: 'Hexagrama 55: A Abundância (Feng) - Grande abundância e plenitude.',
    56: 'Hexagrama 56: O Andarilho (Lu) - Transitoriedade e exploração.',
    57: 'Hexagrama 57: A Suavidade (Sun) - Influência gradual e sutil.',
    58: 'Hexagrama 58: A Alegria (Dui) - Alegria e prazer.',
    59: 'Hexagrama 59: A Dispersão (Huan) - Dissolução de obstáculos.',
    60: 'Hexagrama 60: A Limitação (Jie) - Autocontrole e limites.',
    61: 'Hexagrama 61: A Verdade Interior (Zhong Fu) - Sinceridade e honestidade interior.',
    62: 'Hexagrama 62: A Preponderância do Pequeno (Xiao Guo) - Atenção aos detalhes.',
    63: 'Hexagrama 63: Depois da Conclusão (Ji Ji) - A tarefa está quase completa.',
    64: 'Hexagrama 64: Antes da Conclusão (Wei Ji) - Estágios finais de transição.',
}

def lancar_linha():
    resultado = random.randint(6, 9) 
    return resultado

def gerar_hexagrama():
    hexagrama = []
    linhas_mutaveis = []
    for i in range(6):
        linha = lancar_linha()
        hexagrama.append(linha)
        if linha == 6 or linha == 9:
            linhas_mutaveis.append(6 - i) 
    

    return hexagrama, linhas_mutaveis


def hexagrama_para_binario(hexagrama):
    binario = ''
    for linha in hexagrama:
        if linha == 6 or linha == 8:  # Linhas Yin (quebradas)
            binario += '0'
        else:  # Linhas Yang (sólidas)
            binario += '1'
    return binario


def buscar_hexagrama(binario_hex):
    num = int(binario_hex, 2) + 1  
    return hexagramas.get(num, "Hexagrama Desconhecido")


def leitura_iching():
    hexagrama, linhas_mutaveis = gerar_hexagrama()
    
    print("Hexagrama Gerado:")
    print(hexagrama)
    binario_primario = hexagrama_para_binario(hexagrama)
    print(f"Hexagrama Primário (binário): {binario_primario}")
    print(f"Hexagrama Primário: {buscar_hexagrama(binario_primario)}")
    
    if linhas_mutaveis:
        hexagrama_transformado = [(7 if linha == 9 else 8) if (linha == 6 or linha == 9) else linha for linha in hexagrama]
        binario_transformado = hexagrama_para_binario(hexagrama_transformado)
        print("\nLinhas Mutáveis:", linhas_mutaveis)
        print(f"Hexagrama Transformado (binário): {binario_transformado}")
        print(f"Hexagrama Transformado: {buscar_hexagrama(binario_transformado)}")
    else:
        print("Sem linhas mutáveis.")


leitura_iching()
