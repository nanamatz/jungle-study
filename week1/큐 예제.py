from enum import Enum
from fixed_queue import FixedQueue
Menu = Enum('Menu',['enque','deque','find','exit'])

def select_menu():
    s = [f'({m.value}){m.name}'for m in Menu]
    while True:
        print(*s,sep = '   ',end="")
        n = int(input(': '))
        if 1<=n<=len(Menu):
            return Menu(n)
        
q = FixedQueue(64)

while True:
    print(f'현재 데이터 개수: {0} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.enque:
        x = input('please enter a data: ')
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('stack overflow')
    
    elif menu == Menu.deque:
        try:
            x = q.deque()
            print(f'deque data {x}')
        except FixedQueue.Empty:
            print('empty')
    
    elif menu == Menu.find:
        x = input('please input data: ')
        if x in q.que:
            print(f'{q.count(x)} 개 있음')
        else:
            print('no data')

    else:
        break
       


