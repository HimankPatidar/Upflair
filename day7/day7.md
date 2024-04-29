Exception Handling --

try except, else, finally block\
try = try block is used to write the code that may cause an exception It will run if the code does not have any exceprtion
except = except block is used to handle the exception if codehave any error the except block will. run
else = if try block is executed then else block will exeute
finally = In finally block we can write the code that will be executed whether the try block is executed or not

try :
    print("Welcome Back!!!")
    name = int(input("Enter your first Name : "))
    print("Hi!" , name)

except Exception as e:
    print("Please enter a valid name")

else : 
    print("Error is not occured")

finally:
    print("This will always run")

print("Still running")