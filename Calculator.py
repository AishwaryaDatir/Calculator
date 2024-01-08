def add(a,b):
    ans=a+b
    print("ans=",ans)
def sub(a,b):
    ans=a-b
    print("ans=",ans)

def mul(a,b):
    ans=a*b
    print("ans=",ans)

def mul(a,b):
    ans=a/b
    print("ans=",ans)
    
while True:
    ch=int(input("Enter Choice:\n1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit"))
    if ch==1:
           print("code for add")
           fn=int(input("Enter First Number:"))
           sn=int(input("Enter Second Number:"))
           add(fn,sn)
    elif ch==2:
           print("code for sub")
           fn=int(input("Enter First Number:"))
           sn=int(input("Enter Second Number:"))
           add(fn,sn)

    elif ch==3:
           print("code for mul")
           fn=int(input("Enter First Number:"))
           sn=int(input("Enter Second Number:"))
           add(fn,sn)

    elif ch==4:
           print("code for div")
           fn=int(input("Enter First Number:"))
           sn=int(input("Enter Second Number:"))
           add(fn,sn)

    elif ch==5:
           print("code for exit")
           break
    else:
        print("Invalid choice")



