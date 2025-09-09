ar = list(map(int, input("Enter array elements separated by space : ").split()))

def addNumber(ar):
    totalSum = 0
    for ele in ar:
        totalSum += ele
    return totalSum

print(f"sum of all elements in array: {addNumber(ar)}")
