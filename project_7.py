# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
def identity (x, y, z):
    if not(x or y or z) == (not x and not y and not z):
        print(True)
    else: print(False)
if(identity(0,0,0)==identity(0,0,1)==identity(0,1,0)==identity(1,0,0)
    ==identity(0,1,1)==identity(1,1,0)==identity(1,0,1)==identity(1,1,1)) == True:
    print('Тождество истинно')
else: print(False)