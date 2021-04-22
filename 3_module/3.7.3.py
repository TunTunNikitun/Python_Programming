"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество dd известных нам слов,
после чего на dd строках указываются эти слова.
Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
"""
count=int(input())
dic=[]
text=''
for i in range(count):
    dic.append(str(input().lower()))
words=int(input())
for i in range(words):
    text+=(str(input().lower())+' ')
# text=set(text.split())
for i in set(text.split()):
    if i not in dic:
        print(i)