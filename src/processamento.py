# src/processamento.py
import re

def extrair_ano_historico(data_str):
    data_str = str(data_str).lower().strip()

    # século (ex: século VI a.C. ou século V d.C.)
    match_seculo = re.search(r"século\s+([ivxlcdm]+)\s*(a\.c\.|d\.c\.)", data_str)
    if match_seculo:
        romanos = {
            'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5, 'vi': 6,
            'vii': 7, 'viii': 8, 'ix': 9, 'x': 10
        }
        valor = romanos.get(match_seculo[1])
        if valor:
            ano = valor * 100 - 50
            return -ano if "a.c" in match_seculo[2] else ano

    # intervalo de anos com a.C. ou d.C. (ex: 570–495 a.C.)
    match_intervalo = re.search(r"(\d{1,4})\s*[-–—]\s*(\d{1,4})\s*(a\.c\.|d\.c\.)", data_str)
    if match_intervalo:
        ano = int(match_intervalo[1])
        return -ano if "a.c" in match_intervalo[3] else ano

    # único ano com a.C. ou d.C. (ex: 27 a.C.)
    match_acdc = re.search(r"(\d{1,4})\s*(a\.c\.|d\.c\.)", data_str)
    if match_acdc:
        ano = int(match_acdc[1])
        return -ano if "a.c" in match_acdc[2] else ano

    # data solta tipo "em 212" ou "por 54"
    match_solto = re.search(r"(?:em|por|no|ano)?\s*(\d{1,4})", data_str)
    if match_solto:
        return int(match_solto[1])

    return None
