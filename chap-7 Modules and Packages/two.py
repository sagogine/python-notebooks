import one

print('Tope level in two.py')


one.func()

if __name__=='__main__':
    print('two.py is being run directly')
else:
    print('two.py is being is being imported')
