def dfa(string, n):
    if (string[n] == 'a') and (n < len(string) - 1):
        s0(string, n + 1)
    else:
        print('Rejected')

def s0(string, n):
    if (string[n] == 'n'):
        s1(string, n + 1)
    elif (string[n] == 'm'):
        s7(string, n + 1)
    else:
        print('Rejected')


def s1(string, n):
    if (n == len(string)):
        print('Accepted')
    elif (string[n] == 'd'):
        s2(string,n + 1)
    elif (string[n] == 'c'):
        s3(string, n + 1)
    elif (string[n] == 'a'):
        s4(string, n + 1)
    else:
        print('Rejected')

def s2(string, n):
    if (n == len(string)):
        print('Accepted')
    else:
        print('Rejected')

def s3(string, n):
    if (n == len(string)) or (string[n] != 'a'):
        print('Rejected')
    else:
        s1(string, n + 1)

def s4(string, n):
    if (n == len(string)) or (string[n] != 'r'):
        print('Rejected')
    else:
        s5(string, n + 1)
        
def s5(string, n):
    if (n == len(string)) or (string[n] != 'y'):
        print('Rejected')
    else:
        s6(string, n + 1)
        
def s6(string, n):
    if (n == len(string)) or (string[n] != 'a'):
        print('Rejected')
    else:
        s1(string, n + 1)
        
def s7(string, n):
    if (n == len(string)) or (string[n] != 'i'):
        print('Rejected')
    else:
        s8(string, n + 1)
        
def s8(string, n):
    if (n == len(string)) or (string[n] != 'l'):
        print('Rejected')
    else:
        s1(string, n + 1)

lista = [
    'aa',
    ' ',
    'and',
    'a',
    'aaa',
    'a',
    'a ',
    'as',
    'ann',
    'aan',
    'an',
    'aana',
    'anaa',
    'anna',
    'ana',
    'aanca',
    'ancca',
    'ancaa',
    'anca',
    'annca',
    'ancca',
    'anarya',
    'aanarya',
    'anaryaa',
    'annarya',
    'anarrya',
    'anaryya',
    'anaryaa',
    'amil',
    'aamil',
    'amilaa',
    'amila',
    'ammil',
    'amiil',
    'amill',
    'amila',
    'anaa',
    'anaryaa',
]

for palabra in lista:
    dfa(palabra,0)
