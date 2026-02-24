print("Hello!This is Engineer Esraa 's Calculator")
while True:
 num1 =float(input("Enter first number:"))
 num2 =float(input("Enter Second number:"))
            
 op=input("Enter operation (+,-,*,/):")
 if op =="+":
   print("Result is:",num1+num2)
 elif op=="-":
    print("Result is:",num1-num2)
 elif op=="*":
    print("Result is:",num1*num2)
 elif op=="/":
  if num2!=0:
    print("Result is:",num1/num2)
  else:
    print("Error!Divission by zero")
    
    
    
    
  

