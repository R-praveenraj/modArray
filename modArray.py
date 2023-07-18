# # You are given a large number in the form of a array A of size N where each element 
#denotes a digit of the number.
# # You are also given a number B. You have to find out the value of A % B and return it.
# # input 1
# # A = [1, 4, 3] B = 2
# # Input 2
# # A = [4, 3, 5, 3, 5, 3, 2, 1] B = 47
# Output 1:
# 1
# Output 2:
# 20
def modArray(a,b):
    d=""
    for i in range(len(a)):
        d+=(str(a[i]))
    return int(d)%b
a=list(map(int,input().split()))
b=int(input())
print(modArray(a,b))