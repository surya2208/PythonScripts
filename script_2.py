
'''
import script_1

def mult(a, b):
    print(f'The mul of {a} and {b} is {a*b}')
    return None


# x=10
# y=20
# script_1.addition(x,y)
# # script_1.sub(x,y)
# # mult(x,y)

def main():
    x=10
    y=20
    script_1.addition(x,y)
    script_1.sub(x,y)
    mult(x,y)
    return None

if __name__=="__main__":
    main()

'''

import script_1
print("This is from script2:", __name__)

