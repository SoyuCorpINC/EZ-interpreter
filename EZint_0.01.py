fret = 1
x = ''
y = ''
z = ''
a = ''
b = ''
c = ''
h = 10
m = 9
w = 8
w2 = 9
d1 = ''
while fret > 0:
    import os
    import random
    import time
    import linecache
    print('')
    x1 = input('enter the filename with .txt at the end or enter quit to quit: ')
    if x1 == 'quit' or x1 == 'QUIT':
        fret -= 19919919
        input('quitted')
    else:
        print('')
    import os
    os.system('cls')
    fail = 0
    import webbrowser
    s = 0
    for line in open(x1,'r'):
        s += 1
        f = str(line)
        if f[0:8] == 'com.say:':
            if f[8:11] == '|x|':
                print(x)
            elif f[8:11] == '|a|':
                print(a)
            elif f[8:11] == '|b|':
                print(b)
            elif f[8:11] == '|c|':
                print(c)
            elif f[8:11] == '|y|':
                print(y)
            elif f[8:11] == '|z|':
                print(z)
            else:
                print(f[8:])
                
        elif f[0:4] == 'DSUM':
            drst = random.randint(1,5)
            if drst == 1:
                print('(^0x0^)')
            elif drst == 2:
                print('(^-x-^)')
            elif drst == 3:
                print('(D^oxo^)D')
            elif drst == 4:
                print('(^$x$^)')
            elif drst == 5:
                print('(^IxI^)')
            else:
                print('(^0X0^)')
        elif f[0:5] == 'cut()':
            exit()
        elif f[0:8] == 'clearall':
            os.system('cls')
        elif f[0:5] == 'halt:':
            time.sleep(eval(f[5:]))            
        elif f[0:8] == 'usr.say:' and f[8:9] != '[':
            input(f[8:])
        elif f[0:9] == 'usr.say:[':
            eval(input(f[10:]))
        elif f[0:4] == 'x = ':
            if f[4:12] == 'usr.say:' and f[12:13] != '[':
                x = input(f[12:])
            elif f[4:13] == 'usr.say:[':
                x = eval(input(f[13:]))
        elif f[0:4] == 'y = ':
            if f[4:12] == 'usr.say:' and f[12:13] != '[':
                y = input(f[12:])
            elif f[4:13] == 'usr.say:[':
                y = eval(input(f[13:]))
        elif f[0:4] == 'z = ':
            if f[4:12] == 'usr.say:' and f[12:13] != '[':
                z = input(f[12:])
            elif f[4:13] == 'usr.say:[':
                z = eval(input(f[13:]))
        elif f[0:4] == 'a = ':
            if f[4:12] == 'usr.say:' and f[12:13] != '[':
                a = input(f[12:])
            elif f[4:13] == 'usr.say:[':
                a = eval(input(f[13:]))
            elif f[4:5] == 'y':
                if f[5:8] == ' + ':
                    if f[8:9] == 'z':
                        a = y + z
        elif f[0:8] == 'rnd.say:':
            while f[w:w2] != ';':
                w += 1
                w2 += 1
            if f[w:w2] == ';':
                d = w2 - 1
                num1 = int(f[8:d])
                num2 = int(f[w2:])
                print(random.randint(num1,num2))
        elif f[0:7] == 'access:':
            if f[7:10] == '|x|':
                os.system(x)
            elif f[7:10] == '|y|':
                os.system(y)
            elif f[7:10] == '|z|':
                os.system(z)            
            elif f[7:10] == '|a|':
                os.system(a)
            elif f[7:10] == '|b|':
                os.system(b)
            elif f[7:10] == '|c|':
                os.system(c)
            else:
                os.system(f[7:])
        elif f[0:8] == 'retreat:':
            f = int(line)
            s = f[8:] - 1
        elif f[0:2] == 'if':
            if f[2:4] == ' x':
                if f[4:8] == ' :: ':
                    if f[8:9] == "'":
                        while f[m:h] != ';':
                            h += 1
                            m += 1
                        if f[m:h] == ';':
                            d = h - 1
                            if x == f[9:d]:
                                j = h + 8
                                L = h + 4
                                q = h + 5
                                j2 = h + 7
                                if f[h:j] == 'com.say:':
                                    print(f[j:])
                                elif f[h:j] == 'clearall':
                                    os.system('cls')
                                elif f[h:j] == 'rnd.say:':
                                    while f[w:w2] != ';':
                                        w += 1
                                        w2 += 1
                                    if f[w:w2] == ';':
                                        d1 = w2 - 1
                                        h2 = h + 8
                                        print(random.randint(eval(f[h2:w]),eval(f[w2:])))
                                elif f[h:q] == 'cut()':
                                    exit()
                                elif f[h:j2] == 'access:':
                                    j3 = j2 + 3
                                    if f[j2:j3] == '|x|':
                                        os.system(x)
                                    elif f[j2:j3] == '|y|':
                                        os.system(y)
                                    elif f[j2:j3] == '|z|':
                                        os.system(z)
                                    elif f[j2:j3] == '|a|':
                                        os.system(a)
                                    elif f[j2:j3] == '|b|':
                                        os.system(b)
                                    elif f[j2:j3] == '|c|':
                                        os.system(c)
                                    else:
                                        os.system(f[j2:])
                                elif f[h:L] == 'x = ':
                                    G = L + 8
                                    if f[L:G] == 'usr.say:':
                                       x = input(f[G:])
                                    elif f[L:G] == 'usr.say]':
                                       x = eval(input(f[G:]))
                                elif f[h:L] == 'y = ':
                                    G = L + 8
                                    if f[L:G] == 'usr.say:':
                                       y = input(f[G:])
                                    elif f[L:G] == 'usr.say]':
                                       y = eval(input(f[G:]))
                                elif f[h:L] == 'z = ':
                                    G = L + 8
                                    if f[L:G] == 'usr.say:':
                                       z = input(f[G:])
                                    elif f[L:G] == 'usr.say]':
                                       z = eval(input(f[G:]))
                        else:
                            print('')

            elif f[2:4] == ' y':
                if f[4:8] == ' :: ':
                    if f[8:9] == "'":
                        while f[m:h] != ';':
                            h += 1
                            m += 1
                        if f[m:h] == ';':
                            d = h - 1
                            if y == f[9:d]:
                                j = h + 8
                                L = h + 4
                                q = h + 5
                                j2 = h + 7
                                if f[h:j] == 'com.say:':
                                    print(f[j:])
                                elif f[h:j] == 'clearall':
                                    os.system('cls')
                                elif f[h:j] == 'rnd.say:':
                                    while f[w:w2] != ';':
                                        w += 1
                                        w2 += 1
                                    if f[w:w2] == ';':
                                        d1 = w2 - 1
                                        num1 = int(f[j:d1])
                                        num2 = int(f[w2:])
                                        print(random.randint(num1,num2))
                                elif f[h:q] == 'cut()':
                                    exit()
                                elif f[h:j2] == 'access:':
                                    j3 = j2 + 3
                                    if f[j2:j3] == '|x|':
                                        os.system(x)
                                    elif f[j2:j3] == '|y|':
                                        os.system(y)
                                    elif f[j2:j3] == '|z|':
                                        os.system(z)
                                    elif f[j2:j3] == '|a|':
                                        os.system(a)
                                    elif f[j2:j3] == '|b|':
                                        os.system(b)
                                    elif f[j2:j3] == '|c|':
                                        os.system(c)
                                    else:
                                        os.system(f[j2:])
                                elif f[h:L] == 'x = ':
                                    G = L + 8
                                    if f[L:G] == 'usr.say:':
                                       x = input(f[G:])
                                    elif f[L:G] == 'usr.say]':
                                       x = eval(input(f[G:]))
                                elif f[h:L] == 'y = ':
                                    G = L + 8
                                    if f[L:G] == 'usr.say:':
                                       y = input(f[G:])
                                    elif f[L:G] == 'usr.say]':
                                       y = eval(input(f[G:]))
                                elif f[h:L] == 'z = ':
                                    G = L + 8
                                    if f[L:G] == 'usr.say:':
                                       z = input(f[G:])
                                    elif f[L:G] == 'usr.say]':
                                       z = eval(input(f[G:]))
                        else:
                            print('')
            elif f[2:4] == ' z':
                if f[4:8] == ' :: ':
                    if f[8:9] == "'":
                        while f[m:h] != ';':
                            h += 1
                            m += 1
                        if f[m:h] == ';':
                            d = h - 1
                            if z == f[9:d]:
                                j = h + 8
                                L = h + 4
                                q = h + 5
                                j2 = h + 7
                                if f[h:j] == 'com.say:':
                                    print(f[j:])
                                elif f[h:j] == 'clearall':
                                    os.system('cls')
                                elif f[h:j] == 'rnd.say:':
                                    while f[w:w2] != ';':
                                        w += 1
                                        w2 += 1
                                    if f[w:w2] == ';':
                                        d1 = w2 - 1
                                        num1 = int(f[j:d1])
                                        num2 = int(f[w2:])
                                        print(random.randint(num1,num2))
                                elif f[h:q] == 'cut()':
                                    exit()
                                elif f[h:j2] == 'access:':
                                    j3 = j2 + 3
                                    if f[j2:j3] == '|x|':
                                        os.system(x)
                                    elif f[j2:j3] == '|y|':
                                        os.system(y)
                                    elif f[j2:j3] == '|z|':
                                        os.system(z)
                                    elif f[j2:j3] == '|a|':
                                        os.system(a)
                                    elif f[j2:j3] == '|b|':
                                        os.system(b)
                                    elif f[j2:j3] == '|c|':
                                        os.system(c)
                                    else:
                                        os.system(f[j2:])
                                elif f[h:L] == 'x = ':
                                    G = L + 8
                                    if f[L:G] == 'usr.say:':
                                       x = input(f[G:])
                                    elif f[L:G] == 'usr.say]':
                                       x = eval(input(f[G:]))
                                elif f[h:L] == 'y = ':
                                    G = L + 8
                                    if f[L:G] == 'usr.say:':
                                       y = input(f[G:])
                                    elif f[L:G] == 'usr.say]':
                                       y = eval(input(f[G:]))
                                elif f[h:L] == 'z = ':
                                    G = L + 8
                                    if f[L:G] == 'usr.say:':
                                       z = input(f[G:])
                                    elif f[L:G] == 'usr.say]':
                                       z = eval(input(f[G:]))
                        else:
                            print('')
                                    
        

                                
        else:
            print('')
            fail += 1
            d1 += ',' + str(s)
    print('Program finished! unknown lines spotted: ',fail - 1,' lines: ',d1,' (Note: the final line is often seen as an unknown line, so disregard that.)')
    input('')

#Soyuz owns this code
#there ain't no copyright but don't claim it as yours :(
#that whould just be rude...
#anyways here's a cat (^0x0^)
