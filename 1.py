num = int(input("Enter the number: "))
def fact(num):
    if num==0:
        return 1
    return fact(num-1)*num
print(f"Factotial of {num} is {fact(num)}")