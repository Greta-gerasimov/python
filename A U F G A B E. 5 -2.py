#Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

Kate_file = open('mmarceline.txt', 'r')
content = Kate_file.read()
print(f'содержание:\n {content}')

Kate_file = open('mmarceline.txt', 'r')
content = Kate_file.readlines()
print(content)

Kate_file = open('mmarceline.txt', 'r')
content = Kate_file.readlines()
print(f'количество строк:\n  {len(content)}')

Kate_file = open('mmarceline.txt', 'r')
content = Kate_file.read()
content = content.split()
print(f'количество слов:\n  {len(content)}')


Kate_file = open('mmarceline.txt', 'r')
content = Kate_file.read()
content = len(line.split(' '))
print(f'количество слов:\n in {content} ')
#не очень понятно, как посчитать количество в каждой строке.



