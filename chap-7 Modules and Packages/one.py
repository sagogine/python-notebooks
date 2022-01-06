#one.py

def func():
    print('Func in one.py')

print("top level on one.py")

if __name__ == '__main__':
    print("One.py is being run directly")
else:
    print('One.py has been imported')
