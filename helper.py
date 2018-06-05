def isIsbnOrKey(word):
    '''
    判断是isbn还是普通关键字
    :param word: 要判断的字符串
    :return:返回isbn或者key
    '''
    is_inbn_or_key='key'
    if len(word)==13 and word.isdigit():
        is_inbn_or_key='isbn'
    sort_word=word.replace('-','')
    if '-' in word and len(sort_word)==10 and sort_word.isdigit():
        is_inbn_or_key = 'isbn'
    return is_inbn_or_key