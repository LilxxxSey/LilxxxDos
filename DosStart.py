# Dos

import sys

num = '0123456789'
file = open('phone.txt', 'a')
code = input('[+] Port: ')
    
for a in num:
    for b in num:
        for c in num:
            for d in num:
                for e in num:
                    for f in num:
                        for g in num:
                            for h in num:
                                number = 'Packete enviados:  ' +code+a+b+c+d+e+f+g+h
                                file.write(number+'\n')
                                print(number)
file.close()                               
