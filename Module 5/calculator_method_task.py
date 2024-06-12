class Calculator:
    brand='Casio MS990'

    def add(self,num1,num2):
        summation=num1+num2
        return summation
    
    def subtract(self,num1,num2):
        subtraction=num1-num2
        return subtraction
    
    def multiply(self,num1,num2):
        mul=num1*num2
        return mul
    
    def divition(self,num1,num2):
        div=num1/num2
        return div
    


cal=Calculator()
result=cal.add(50,20)
print(result)
result=cal.subtract(50,20)
print(result)
result=cal.multiply(50,20)
print(result)
result=cal.divition(50,20)
print(result)