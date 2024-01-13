no = input("enter nums")
nos = no.split(",")
#nums = list()
#print(nums)
#for n in nos:
#    nums.append(n)
#print(nums)
count = 0
sum = 0
for num in nos:
    count = count+1
    thin = int(num)
    sum = sum + thin
print("No of elements entered:",count)
print("Sum of elements entered:", sum)
Avg = sum/count
print("Average is:",Avg)

