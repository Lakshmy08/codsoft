import random

class password:
    def gen(self,len):
        word="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
        code=""
        for i in range(len):
            code+=random.choice(word)
        return code
    

def main():
    print("enter length of password")
    l=int(input())
    p=password()
    u=p.gen(l)
    print(u)

if __name__=="__main__":
    main()