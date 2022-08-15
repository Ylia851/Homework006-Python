#1. Создайте программу для игры в "Крестики-нолики".

pole = list(range(1, 10))

def Pole():
    for i in range(3):
        print(pole[0 + i * 3], pole[1 + i * 3], pole[2 + i * 3])

Pole()

User1 = input('Введите Ваше Имя: ')
print(f'{User1} Вы - первый игрок! Вы играете Х!')
UserHod1 = 'X'
User2 = input('Введите Ваше Имя: ')
print(f'{User2} Вы - второй игрок! Вы играете О!')
UserHod2 = 'O'
UserHod = 0
if UserHod % 2 == 0:
    UserHod = UserHod1
else:
    UserHod = UserHod2

def InputHod(UserHod):
    
    print(f'Выберите ячейку, в которой вы хотите поставить  {UserHod}')
    Hod = int(input())
    if Hod > 9 or Hod < 1:
        print("Вы ввели неправильный номер ячейки. Повторите ввод: ")
    elif Hod <= 9 or Hod >= 1:
        pole[Hod - 1] == UserHod
    else:
        print('Ячейка уже занята! Сделайте ход в другой ячейке')

def Win():
    count = 0
    if (pole[0] == pole[1] == pole[2] == 'X') or (pole[3] == pole[4] == pole[5] == 'X') or (pole[6] == pole[7] == pole[8] == 'X') or (pole[0] == pole[4] == pole[8] == 'X') or (pole[2] == pole[4] == pole[6] == 'X') or (pole[0] == pole[3] == pole[6] == 'X') or (pole[1] == pole[4] == pole[7] == 'X') or (pole[2] == pole[5] == pole[8] == 'X'):
        print(f'Поздравляем! Выиграл {User1}. Игра закончена.')
    elif (pole[0] == pole[1] == pole[2] == 'O') or (pole[3] == pole[4] == pole[5] == 'O') or (pole[6] == pole[7] == pole[8] == 'O') or (pole[0] == pole[4] == pole[8] == 'O') or (pole[2] == pole[4] == pole[6] == 'O') or (pole[0] == pole[3] == pole[6] == 'O') or (pole[1] == pole[4] == pole[7] == 'O') or (pole[2] == pole[5] == pole[8] == 'O'):
        print(f'Поздравляем! Выиграл {User2}. Игра закончена.')
    else:
        return InputHod(UserHod)
    count +=1
    if count > 8:
        print("Ничья!")
Win()


#2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,. приоритет операций стандартный.
#*Пример:
#2+2 => 4;
#1+2*3 => 7;
#1-2*3 => -5;
#- Добавьте возможность использования скобок, меняющих приоритет операций.
#Пример:
#1+2*3 => 7;
#(1+2)*3 => 9;

#from curses.ascii import isdigit
#import re

print('Введите оперцию: ')
a = str(input())
#print(str(eval(a)))
def GetCoef(a):
    coef = []
    for i in a:
        if (i!='  '):
            coef.append(i.split('*'))
    print(coef)
n = GetCoef(a)

for i in n:    #если в списке встречаются числа, присвоить им значение вещественное
    nums = []
    if n[i].isdigit():
        num = list(map(float, n[i]))
        nums.appendt(i, num)
    else:
        nums.append(n[i])

print(nums)
for i in nums:
    if nums[i] == '*':
        res = nums[i-1] * nums[i+1]
    del(nums[i-1])
    nums.insert(res, i)   #можно ли так поменять n[i] на res
    del(nums[i+1])             #было [1, +, 2, *, 3] стало [1, +, 6] 

print(nums)
for i in nums:
    if nums[i] == '/':
        res = nums[i-1] / nums[i+1]
    del(nums[i-1])
    nums.insert(res, i)   
    del(nums[i+1])             

print(nums)
for i in nums:
    if nums[i] == '+':
        res = nums[i-1] + nums[i+1]
    del(nums[i-1])
    nums.insert(res, i)   
    del(nums[i+1])     

print(nums)
for i in nums:
    if nums[i] == '-':
        res = nums[i-1] - nums[i+1]
    del(nums[i-1])
    nums.insert(res, i)   
    del(nums[i+1]) 

print(nums)

#3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.

#желательно использовать одну из функций ускоренной обработки данных где-нибудь

path = 'textname.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()
print(data)

new_text = ''

def CodFun(text) -> str:
    count = 0
    txt = list.sort(text)
    
    for i in range(len(txt)):
        if txt[i] == txt[i+1]:
            count+=1
        else:
            new_text.append(txt[i])
            new_text.append(str(count))
            count = 1
    return new_text
    

def DecodFun(text):
    num = ''
    decodint_text = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            num += text[i]
        else:
            decodint_text = decodint_text + text[i] * int(num)
            num = ''
    return decodint_text


t = input(data)
print(CodFun(t))
print(DecodFun(t))    

