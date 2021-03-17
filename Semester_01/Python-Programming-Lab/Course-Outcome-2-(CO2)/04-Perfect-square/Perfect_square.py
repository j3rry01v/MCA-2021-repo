# generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square
import math

start = int(input("Enter a starting range in 4 digit:"))
end = int(input("Enter an ending range in 4 digit:"))
perfect = []
for i in range(start,end+1):
    flag = 0
    num=i
    while num>0 :
        digit = num%10
        if digit not in [0,2,4,6,8]:
            flag=1
            break
        num=int(num/10)
    if flag==0 and math.sqrt(i) % 1 == 0:
        perfect.append(i)

print("The list of perfect square numbers are:",perfect)