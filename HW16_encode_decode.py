# Даний рядок у байтовому вигляді:
# b'r\xc3\xa9sum\xc3\xa9'закодована в кодуванні за умовчанням utf-8.
# Декодувати її у рядковий вигляд у кодуванні за замовчуванням.
# Потім результат знову перетворити на байтовий, тільки вже в кодуванні 'Latin1'
# І на кінець результат знову декодувати у рядок
# (Результати всіх перетворень виводити на екран).


word_byte = b'r\xc3\xa9sum\xc3\xa9'
word_str = word_byte.decode()
print(word_str)

word_to_latin1 = word_str.encode('Latin1')
print(word_to_latin1)

word_Latin1_to_str = word_to_latin1.decode('Latin1')
print(word_Latin1_to_str)
