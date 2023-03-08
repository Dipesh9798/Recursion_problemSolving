##sum of first n numbers
def sumN(i,summ,n):
    if i>n:
        print(summ)
        return
    sumN(i+1,summ+i,n)
n=int(input())
sumN(1,0,n)

def summ(n):
    if n==0:
        return 0
    return n+summ(n-1)
print(summ(n))

##reverse an array using recursion
def rev(l,r,arr):
    if l>=r:
        return
    arr[l],arr[r]=arr[r],arr[l]
    rev(l+1,r-1,arr)
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
rev(0,n-1,arr)
print(arr)

##check for a string is palindrome
def isPal(i,n,string):
    if i>=(n//2):
        return True
    if string[i]!=string[n-i-1]:
        return False
    return isPal(i+1,n,string)
n=int(input())
string=input()
print(isPal(0,n,string))


##fibonnaci numbers using recursion
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
n=int(input())
print(fibo(n))


##Recursion on array subsequence
def subs(i,arr,sub):
    if i>=len(arr):
        print(sub)
        return
    sub.append(arr[i])
    subs(i+1,arr,sub)
    sub.remove(arr[i])
    subs(i+1,arr,sub)
arr=list(map(int,input().split()))
sub=[]
subs(0,arr,sub)  

##Recursion on string subsequence--incomplete code
def subs(i,strinput,strtemp):
    if i>=len(strinput):
        print(strtemp)
        return
    strtemp=strtemp+strinput[i]
    subs(i+1,strinput,strtemp)
    strtemp.replace(strinput[i],"")
    subs(i+1,strinput,strtemp)
strinput=input()
strtemp=""
subs(0,strinput,strtemp) 

##find subsequence with given sum using recursion

def subs(i,arr,sub,s,inpsum):
    if i==len(arr):
        if s==inpsum:
            print(sub)
        return 
    sub.append(arr[i])
    s+=arr[i]
    subs(i+1,arr,sub,s,inpsum)
    sub.remove(arr[i])
    s-=arr[i]
    subs(i+1,arr,sub,s,inpsum)
arr=list(map(int,input().split()))
inpS=int(input())
sub=[]
subs(0,arr,sub,0,inpS)
        