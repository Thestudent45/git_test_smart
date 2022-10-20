names = []

while True:
    a = input('digite 1 para escrever 2 para ver e 0 para sair: ')
    if a == '1':
        x = input(':')
        names.append(x)
    elif a == '2':
        for i in names:
            print('\n',i,'\n')
    elif a == '0':
        break
