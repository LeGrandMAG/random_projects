list = [ {
    "hour": 9.30, 
    "time":1}
        ]


print(list[0]['hour'])


i = 0
def ClassHour(): 
    while(i<10):
        i+=1
        
        a = list[i-1]['hour'] + 1
        b = list[i-1]['time'] + 1
        print(f'a is {a}')
        print(f'b is {b}')
        c = { 'hour':a, 'time': b}
        list.append(c)
        print(f"The hour is {a} and the time is {b}  ")
        print(f' I is {i}')
        
    v = t

    if (v<=0):
        print("Please insert a number above 0")
    else:
        e = list[v-1]['hour']
        f = list[v-1]['time']
        print(f'the period is {f} and the time is {e}')

    z = int(input("press a key to exit"))