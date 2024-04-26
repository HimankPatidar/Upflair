def Total_sum(num1, num2) :
    total = num1 + num2
    return total

def Multiply(num1,num2) :
    total = num1 * num2
    return total

def Division(num1,num2) :
    total = num1 / num2
    return total

ls = [1,2,3,4,5,6,7,8]
def Average_Finder(list1) :
    total_sum = sum(list1)
    total_element = len(list1)
    average = total_sum / total_element
    print("Total Average is : " , average)
    #return average

list1 = [12,13,14,15,16,17,18,19]


if __name__ == "__main__":
    Total_sum()
    print(Multiply(4, 2))
    Average_Finder()
    

