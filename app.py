from calc_func import do_add,do_sub,do_division
from multiply import do_mul
def main():
    print("Welcome to the Calculator app")
    print("""
          \nSelect the Function from the given options:
          1.Add
          2.Subtract
          3.Multiply 
          4.Division
          """)
    
    user_input=input("Select the funtion:")
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    
    if user_input == "1":
        result= do_add(a,b)
    elif user_input == "2":
        result =do_sub(a,b) 
    elif user_input == "3":
        result = do_mul(a,b)    
    elif user_input == "4":
        result = do_division(a,b)    


    print("Result:",result)


if __name__=="__main__":
    main()