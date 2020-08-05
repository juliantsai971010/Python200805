while True:
    print('1.加')
    print('2.減')
    print('3.乘')
    print('4.除')
    print('5.離開')
    a=input('enter')
    a=int(a)
    
    if a==1:
        一=input('first number')
        二=input('second number')
        
        一=int(一)
        二=int(二)
        print(一+二)
        break
    elif a==2:
        一=input('first number')
        二=input('second number')
       
        一=int(一)
        二=int(二)
        print(一-二)
        break
    elif a==3:
        一=input('first number')
        二=input('second number')
        
        一=int(一)
        二=int(二)
        print(一*二)
        break
    elif a==4:
        一=input('first number')
        二=input('second number')
        
        一=int(一)
        二=int(二)
        print(一/二)
        break
    else:
        break
        
    