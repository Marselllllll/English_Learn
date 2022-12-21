from translate import Translator
from typing import TextIO


def read_file(name: str) -> list:
    """
    :param name: Параметр (type: str), подающий на вход путь к файлу для последующего чтения.
    :return: Значение (type: list), возвращаемое функцией в виде списка всех слов из прочитанного файла.
    """
    text: TextIO = open(name, encoding="utf-8")
    stroka0: str = text.read()
    text.close()
    stroka1: str = stroka0.replace('\n', ' ')
    i: int = 0
    strokaend: str = ''
    while i != len(stroka1):
        if 65 <= ord(stroka1[i]) <= 90 or 97 <= ord(stroka1[i]) <= 122:
            strokaend += stroka1[i].lower()
        elif stroka1[i] == ' ':
            if 65 <= ord(stroka1[i+1]) <= 90 or 97 <= ord(stroka1[i+1]) <= 122:
                strokaend += stroka1[i]
        i += 1
    lst0: list = strokaend.split(sep=' ')
    return lst0


def slovar(lstfull: list) -> dict:
    """
    :param lstfull: Параметр (type: list), подающий на вход список всех слов.
    :return: Значение (type: dict), возвращаемое функцией в виде словаря всех уникальных слов и их количества.
    """
    dct: dict = {}
    for i in lstfull:
        dct[i] = lstfull.count(i)

    lst_keys: list = list(dct.keys())

    sorted_values: list = sorted(list(dct.values()))

    dct_value: dict = dict.fromkeys(sorted_values)
    sorted_values = sorted(list(dct_value.keys()), reverse=True)

    sorted_dct: dict = {}

    for i in sorted_values:
        for k in lst_keys:
            if dct[k] == i:
                sorted_dct[k] = i

    return sorted_dct


def translating(dct: dict) -> None:
    """
    :param dct: Параметр (type: list), подающий на вход словарь.
    :return: None.
    """
    translator: Translator = Translator(to_lang="ru", from_lang="en")
    lst_word: list = list(dct.keys())
    lst_count: list = list(dct.values())
    lst_trans: list = []

    for i in lst_word:
        lst_trans.append(translator.translate(i))
    print(lst_word)
    print(lst_count)
    print(lst_trans)
    text: TextIO = open("End.txt", mode='w')
    for i in range(0, len(lst_word)):
        text.write(f"{lst_word[i]} {lst_trans[i]} {lst_count[i]}\n")
    text.close()


lst: list = read_file("test.txt")

dct: dict = slovar(lst)

translating(dct)
