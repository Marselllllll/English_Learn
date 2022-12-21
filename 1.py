import pymorphy2
from translate import Translator
from typing import TextIO


def read_file(name: str) -> list:
    """
    :param name: Параметр (type: str), подающий на вход путь к файлу для последующего чтения.
    :return: Значение (type: list), возвращаемое функцией в виде списка всех слов из прочитанного файла.
    """
    text: TextIO = open(name, mode='r')
    stroka0: str = text.read()
    text.close()
    stroka1: str = stroka0.replace('\n', ' ')
    i: int = 0
    strokaend: str = ''
    while i != len(stroka1):
        if 1040 <= ord(stroka1[i]) <= 1103 or ord(stroka1[i]) == 1025 or ord(stroka1[i]) == 1105:
            strokaend += stroka1[i].lower()
        elif stroka1[i] == ' ' or stroka1[i] == '-' or stroka1[i] == '_':
            if stroka1[i+1] != ' ':
                strokaend += stroka1[i]
        i += 1
    lst0: list = strokaend.split(sep=' ')
    i = 0
    lstend: list = []
    while i != len(lst0):
        lstend.append(lst0[i])
        i += 1
    return lstend


def unique(lst: list) -> list:
    """
    :param lst: Параметр (type: list), подающий на вход список всех слов.
    :return: Значение (type: list), возвращаемое функцией в виде списка всех уникальных слов.
    """
    i: int = 0
    lstend: list = []
    while i != len(lst):
        if lstend.count(lst[i]) == 0:
            lstend.append(lst[i])
        i += 1
    return lstend


def slovar(lstfull: list, lstunique: list) -> dict:
    """
    :param lstfull: Параметр (type: list), подающий на вход список всех слов.
    :param lstunique: Параметр (type: list), подающий на вход список всех уникальных слов.
    :return: Значение (type: dict), возвращаемое функцией в виде словаря всех уникальных слов и их количества.
    """
    dct: dict = {}
    for i in lstunique:
        dct.fromkeys(i, lstfull.count(i))

    sorted_values: list = sorted(dct.values())
    sorted_dct: dict = {}

    for i in sorted_values:
        for k in dct.keys():
            if dct[k] == i:
                sorted_dct[k] = dct[k]
                break
    return sorted_dct


def translating(dct: dict) -> None:
    translator: Translator = Translator(to_lang="en")
    lst: list = dct.keys()
    text: TextIO = open("End.txt", mode='w')

    translation: str = translator.translate()
    text.close()

lst: list = read_file("test.txt")
lstunique: list = unique(lst)
dct: dict = slovar(lst, lstunique)
