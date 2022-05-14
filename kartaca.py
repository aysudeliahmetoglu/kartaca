for i in range(1,100):
    result=i
    if(i%3==0):
        result+="foo"
    if(i%5==0):
        result+="bar"    
    print(result)