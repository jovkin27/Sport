from module import*
from random import*
sportmen=[]
results=[]

while True:
    a=input('0 - exit\n1 - show sportmen and results\n2 - Add sportmen\n3 [N] best results\n4 Sorted list\
    \n5 TOP3\n6 Disqualification\n7 Search result by name\
    \n8 save data\n')
    if a=='0':
        print('See you soon')
        break
    elif a=='1':
        print(sportmen)
        print(results)
    elif a=='2':
        add_sportmen(sportmen,results)
    elif a=='3':
        n_results(sportmen,results)
    elif a=='4':
        sorted_list(sportmen,results)
    elif a=='5':
        top3(sportmen)
    elif a=='6':
        remove_sportmen(sportmen,results)
    elif a=='7':
        search(sportmen,results)
    elif a=='8':
        save_data(sportmen,results,"Sportmen.txt")
