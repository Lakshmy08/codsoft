class calc:
    def __init__(self):
        self.a=int(input())
        self.b=int(input())
    
    def add(self):
        sum=self.a+self.b
        return sum
    def sub(self):
        dif=self.a-self.b
        return dif
    def mul(self):
        pro=self.a*self.b
        return pro
    def div(self):
        quo=self.a/self.b
        return quo

def main():
    print("enter numbers")
    cal=calc()
    print("1.addition\n2.subtraction\n3.multiplication\n4.division")
    ch=int(input("enter your choice "))
    if(ch==1):
        a=cal.add()
        print("the sum is ",a)
    elif(ch==2):
        b=cal.add()
        print("the difference is ",b)
    elif(ch==3):
        c=cal.mul()
        print("the product is ",c)
    elif(ch==4):
        k=cal.div()
        print("the quotient is ",k)
    else:
        print("enter valid choice")

if __name__=="__main__":
    main()
    

    