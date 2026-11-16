"""
Условие: Напишите класс CycleList, который инициализируется обычным списком.

Задание:

При обращении к индексу, который выходит за границы списка, класс не должен выдавать IndexError. 
Вместо этого он должен зацикливаться (идти по кругу).
Класс должен поддерживать итерацию, получение длины (len()) и строковое представление (str()).
"""

class CycleList:
    def __init__(self,data):
        self.data = data
    
    
    def __getitem__(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            return self.data[0]
        
    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        res = ""
        for i in self.data:
            res += i
        return res
        
cl = CycleList(["А","Б","В"])

print("Существующие индексы:")
print(cl[0])
print(cl[1])
print(cl[2])
print("Проверка на IndexError:")
print(cl[1337])
print("================================" )

print("Проверка str и len:")
print(len(cl))
print(str(cl))