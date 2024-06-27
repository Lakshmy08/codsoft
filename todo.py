class todolist:
    def __init__(self):
        self.todo=[]
    def addtask(self):        
        print("enter task to add")
        toadd=input()
        self.todo.append(toadd)
        print(toadd," added successfully")
    def deltask(self):
        print("enter task to delete")
        todel=input()
        if(len(self.todo)!=0):
            if(todel in self.todo):
                self.todo.remove(todel)
                print(todel," marked as done and deleted successfully")
            else:
                print("task not found")
        else:
            print("list empty")
    def printtask(self):
        if(len(self.todo)==0):
            print("list empty")
        else:    
            for i in self.todo:
                print("Tasks To do")
                print(i)
    def cleartask(self):
        if(len(self.todo)!=0):
            self.todo.clear()
            print("Todo list cleared successfully")

def main():
    t=todolist()
    c='T'
    while(c=='T'):
        print("1.Add task\n2.Delete task\n3.Print task\n4.Clear task\nEnter your choice")
        n=int(input())
        if(n==1):
            t.addtask()
        elif(n==2):
            t.deltask()
        elif(n==3):
            t.printtask()
        elif(n==4):
            t.cleartask()
        else:
            print("Enter valid choice")
        print("Do you want to continue?(T/F)")
        c=input()
        
if __name__=="__main__":
    main()


