from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu',['push','pop','find','exit'])

def select_menu():
    s = [f'({m.value}){m.name}'for m in Menu]
    while True:
        print(*s,sep = '   ',end="")
        n = int(input(': '))
        if 1<=n<=len(Menu):
            return Menu(n)
        
s = FixedStack(64)

while True:
    print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.push:
        x = input('please enter a data: ')
        try:
            s.push(x)
        except FixedStack.Full:
            print('stack overflow')
    
    elif menu == Menu.pop:
        try:
            x = s.pop()
            print(f'pop data {x}')
        except FixedStack.Empty:
            print('empty')
    
    elif menu == Menu.find:
        x = input('please input data: ')
        if x in s.stk:
            print(f'{s.count(x)} 개 있음')
        else:
            print('no data')

    else:
        break
       


