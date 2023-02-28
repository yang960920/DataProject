num1,num2,result = 200,100,0


def add_func(n1,n2) :
    res = n1 + n2
    return res

def minus_func(n1,n2) :
    res = n1 - n2
    return res

def mult_func(n1,n2) :
    res = n1 * n2
    return res

def div_func(n1,n2) :
    res = n1 / n2
    return res



result = add_func(num1,num2)

print(num1,'+',num2,'=',result)

result = minus_func(num1,num2)

print(num1,'-',num2,'=',result)

result = mult_func(num1,num2)

print(num1,'*',num2,'=',result)

result = div_func(num1,num2)

print(num1,'/',num2,'=',result)
