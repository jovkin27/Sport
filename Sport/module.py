from random import*
import time
sportmen=[]
results=[]

def add_sportmen(sportmen:list,results:list):
   """
   """
   b=randrange(2,5)
   ac=int(input('How much sportmen will competite?\n'))
   for i in range(ac):
       name=input('Name:')
       sportmen.append(name)
       results.append(3+b)
       b+=b
   return sportmen,results


def n_results(sportmen:list,results:list):
    q=0
    ac=int(input('How much results you want?\n'))
    if ac>len(sportmen):
        print('Sportmen out of range,Try again')
    elif ac<=len(sportmen):
        for i in range(ac):
            abc=sportmen[q]
            abcd=results[q]
            q+=1
            print(f'{q} place had, {abc} - {abcd}m')
    return abc,abcd


def sorted_list(sportmen:list,results:list):
    q=0
    print(f'Sorted list of competitors:')
    for i in range(len(results)):
        results.sort()
        sportmen[q]
        q+=1
        print(f'{q} place had: {results[q-1]}m - {sportmen[q-1]}')
    print(f'Sorted list is: {results}')
    return sportmen,results


def top3(sportmen:list):
    q=1
    top=['the best','second','not bad']
    top3_list=[]
    y=0
    k=0
    for i in range(1,4):
        print(f'{sportmen[y]} is {top[k]} - {q} place')
        top3_list.append(sportmen[y])
        q+=1
        y+=1
        k+=1
    return sportmen


def remove_sportmen(sportmen:list,results:list):
    ac=int(input('Please enter result range\n'))
    acc=0
    for i in range(len(results)):
        if results[acc]<ac:
            results.pop(acc)
            sportmen.pop(acc)
        elif results[acc]>ac:
            acc+=1
    return results,sportmen


def search(sportmen:list,results:list):
    q=0
    ac=input('name:')
    while True:
        try:
            i=sportmen.index(ac,q)
            abc=print(f'This {sportmen[i]} had {results[i]}')
            q+=1
        except:
            break
    return sportmen, results


def save_data(sportmen:list,results:list,file:str):
    """
    """
    file=open("Sportmen.txt", 'w')
    file2=open("Results.txt", 'w')
    results=list(map(str,results))
    for e in sportmen:
        file.write(e)
        file.write('\n')
    file.close()

    for r in results:
        file2.write(r)
        file2.write('\n')
    file.close()