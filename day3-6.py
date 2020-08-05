d={}
while True:
    print('1.add word')
    print('2.show all the word')
    print('3.英翻中')
    print('4.中翻英')
    print('5.離開')
    a=input('enter')
    a=int(a)
    
    if a==1:
        while True:
            
            b=input('輸入中文')
            c=input('輸入英文')
            d[b]=c
            break
    elif a==2:
        print(d)
        break
    elif a==3:
        c=input('輸入英文')
        for k,v in d.items():
            if v==c:
                print(k)
        
    elif a==4:
        b=input('輸入中文')
        print(d[b])
    else:
        break
        
        