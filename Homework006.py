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

