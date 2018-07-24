#-*- coding: utf-8 -*-

import re


BlankCharSet = set([' ', '\n', '\t'])
CommaNumberPattern = re.compile(u'\d{1,3}([,，]\d\d\d)+')
CommaCharInNumberSet = set([',', '，'])
NumberSet = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'])


def clean_text(text):
    """
    如果一段文本中含有数字，把中文与数字分开，保存为列表，返回
    :param text:
    :return:
    """
    return clean_number_in_text(remove_blank_chars(text))


def clean_number_in_text(text):
    comma_numbers = CommaNumberPattern.finditer(text)  # 匹配出文本中的数字
    new_text, start = [], 0
    for comma_number in comma_numbers:
        # comma_number.start() 数字的开始索引
        new_text.append(text[start:comma_number.start()])
        start = comma_number.end()  # 数字的结束索引
        new_text.append(remove_comma_in_number(comma_number.group()))
    new_text.append(text[start:])
    return ''.join(new_text)


def remove_blank_chars(text):
    new_text = []
    if text is not None:
        for ch in text:
            if ch not in BlankCharSet:
                new_text.append(ch)
    return ''.join(new_text)


def remove_comma_in_number(text):
    """
    去除数字中的逗号
    :param text:
    :return:
    """
    new_text = []
    if text is not None:
        for ch in text:
            if ch not in CommaCharInNumberSet:
                new_text.append(ch)
    return ''.join(new_text)

def extract_number(text):
    new_text = []
    for ch in text:
        if ch in NumberSet:
            new_text.append(ch)
    return ''.join(new_text)

if __name__ == "__main__":
    text = "总股 2,000,000 总价 300,000,000,000 元"
    print(text)
    print(clean_number_in_text(text))
