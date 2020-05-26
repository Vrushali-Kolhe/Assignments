a=5
b=0

try:
    #try the code which u think can occur error at runtime
    f1= open('ved.txt', 'r')  #file can not be found
    print(a/b)  #cant divide by zero
    raise SyntaxError

except FileNotFoundError:
    print("FileNotFoundError: ved.txt file does not exist in your computer.")

except ZeroDivisionError:
    print("ZeroDivisionError: Hey, You cannot divide a Number by Zero.")

except SyntaxError:
    print("SyntaxError: Somewhere your syntax goes wrong.")

except Exception:
    #error which is in not thought of the programmer can be handled in this
    print("Error: Something went wrong.")

finally:
    #inspite error occur or not tis block get performed
    print("I will execute always.")