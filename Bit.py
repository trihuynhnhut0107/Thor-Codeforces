
def PlusOne(a):
    if (a == "X++" or a == "++X"):
        return True
    else:
        return False

def MinusOne(a):
    if(a == "X--" or a == "--X"):
        return True
    else:
        return False

def main():
    n = int(input())
    count=int(0)
    for i in range(n):
        order = input()
        if (PlusOne(order)):
            count += 1
        else:
           if(MinusOne(order)):
               count -=1
    print(count)

if __name__ == "__main__":
    main()



