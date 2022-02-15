import random

a = ['_', '_', '_', '_', '_', '_', '_',
     '|', ' ', '|', ' ', '|', ' ', '|',
     '_', '_', '_', '_', '_', '_', '_',
     '|', ' ', '|', ' ', '|', ' ', '|',
     '_', '_', '_', '_', '_', '_', '_',
     '|', ' ', '|', ' ', '|', ' ', '|',
     '_', '_', '_', '_', '_', '_', '_',
     ]


def board():
    i = 0
    while i < 49:
        if i % 7 != 0:
            print(a[i], end='')
        else:
            print()
            print(a[i], end='')
        i += 1


def insert(aa, s):
    match aa:
        case 1:
            a[8] = s
        case 2:
            a[10] = s
        case 3:
            a[12] = s
        case 4:
            a[22] = s
        case 5:
            a[24] = s
        case 6:
            a[26] = s
        case 7:
            a[36] = s
        case 8:
            a[38] = s
        case 9:
            a[40] = s


def cond():
    if (a[8] == a[10] == a[12] and a[8] != ' ') or (a[22] == a[24] == a[26] and a[22] != ' ') or (
            a[36] == a[38] == a[40] and a[40] != ' ') or (a[8] == a[22] == a[36] and a[8] != ' ') or (
            a[10] == a[24] == a[38] and a[24] != ' ') or (a[12] == a[26] == a[40] and a[26] != ' ') or (
            a[8] == a[24] == a[40] and a[8] != ' ') or (a[12] == a[24] == a[36] and a[24] != ' '):
        return True
    else:
        return False


aaa = ['_', '_', '_', '_', '_', '_', '_',
       '|', '1', '|', '2', '|', '3', '|',
       '_', '_', '_', '_', '_', '_', '_',
       '|', '4', '|', '5', '|', '6', '|',
       '_', '_', '_', '_', '_', '_', '_',
       '|', '7', '|', '8', '|', '9', '|',
       '_', '_', '_', '_', '_', '_', '_',
       ]
i = 0
while i < 49:
    if i % 7 != 0:
        print(aaa[i], end='')
    else:
        print()
        print(aaa[i], end='')
    i += 1

b = []
while len(b) < 9:
    print('\nEnter number:')
    num = int(input())
    if num not in b:
        b.append(num)
        insert(num, 'X')
        if cond():
            board()
            print('\nYou Wins')
            break
        # board()
        com_num = num
        while com_num in b and len(b) < 9:
            com_num = random.randint(1, 9)
        b.append(com_num)
        insert(com_num, 'O')
        board()
        if cond():
            print('\nComputer Wins')
            break
    else:
        print('Already placed!')
else:
    print('Draw! Game Ended')
