import re
def search(word, text):
    list_search = []
    text = re.split(r'[.|!|?|]', text)
    if len(word) < 1:
        return []
    for i in text:
        word_list = re.split('[ |,|;|:|)|(|"|«|»|-]', i.lower())
        if word.lower() in word_list:
            if i not in list_search:
                list_search.append(i)
    if len(list_search) > 0:
        return list_search
    else:
        return []