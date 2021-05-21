'hello world'



dizi = 'python java c'
print(dizi.split())


print('hello world')

print(''' hello baby's ''')

print ('''')

print('''''')

print('''''''')

print('x < y') #bu benim ilk commentim


print(print.__doc__)

print(sum.__doc__)

print(map.__doc__)

print(input.__doc__)

x= 11

print(x)

x=22

print(x)

x=11
y=33
z=55




print(x,y,z,)

x= 33
x= 44
x= 55
print (x)

x= 22
print(x)
x= 44
print (x)
x=77
print(x)

last&name^^^


29/3

29//3

'osman'+6

'osman'+str(6)

pi=3.14
r=5
area=pi*r**2
print(area)

print('None or True and 1')

color= 'blue'
fruit= 'banana'
vegetable= 'patato'
animal= 'giraffe'
print( color,fruit,vegetable, animal,sep='\t')


animal= 'giraffe'
print(animal[2:6:3])


name= 'Betül' 
job='engineer'
domain='food'
message=(
    f" hi{name}\n"
    f" you are {job}\n"
    f" in {domain} section."
    )
print (message)

text = "{0}! I am a {1} programmer and I {2} Clarusway.".format("Hello", "new", "love")
print(text)

sentence= 'I live and work in Virginia.'
print(sentence)
sentence= sentence.upper()
print(sentence)
sentence+= sentence.upper()
print(sentence)


sentence= 'I live and worK İN VirgiNIA.'
title_sentence=sentence. title()
sentence=sentence.upper()
print(sentence)
print(title_sentence)
changed_str=(title_sentence. replace('i' , '+')) 
print(changed_str)


sentence = "I lIve in sARAJEVO."
sentence= sentence.capitalize()
print(sentence)
sentence=sentence.title()
print(sentence)



x= 'Hello world'
print('%.5s'%x)

name = "Joseph"
job = "teachers"
domain = "Data Science"
message = (
     f"Hi {name}. "
     f"You are one of the {job} "
     f"in the {domain} section."
)
print(message)

name = "Joseph"
job = "teachers"
domain = "Data Science"
message = (
     f"Hi {name}.\n"
     f"You are one of the {job} \n"
     f"in the {domain} section.\n "
)
print(message)

my_list = ['Joseph', 'Clarusway', 2020]
new_list1 = list(my_list)  
new_list2 = [my_list]  
print(new_list1)
print(len(new_list1)) 
print(new_list2)
print(len(new_list2))

list_1 = ['one', 'four', 'nine']
list_1.sort()
print(list_1)
list_1.insert(-2,'love')
print(list_1)




try_tuple = ('love',)
print(try_tuple)
print(type(try_tuple)) # it's a tuple type.


sehirler.sort(key=len, reverse=False)
print(sehirler)

"a","b","c".split("tokyo")

"a,b,c".split("tokyo")

"a,b,c".split("-")

("a","b","c").list()

sehirler= ['istanbul',"van", "ankara" ]
sorted(sehirler, key=len, reverse=True)

even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(even_numbers[4:9])

print(len([12, 34, 56]))

print(len([[12, 34, 56]]))

print(len([[12, 34, 56]][0]))

student_ages = {"Harry": 29,
                "Clark": 32,
                "Peter": 22,
                "Bruce": 36
                }
print(student_ages ["Clark"])            

print(len(set('listen to the voice of enlisted')))


liste=["eat", "tea", "tan", "ate", "nat", "bat"]
sorted_list=[]
sonuc=[]
for i in liste:
  if sorted(i) not in sorted_list:
    sorted_list.append(sorted(i))
for a in range(len(sorted_list)):
  sonuc.append([i for i in liste if sorted(i)==sorted_list[a]])
print(sonuc) 

num_1 = float(input("Enter the first number: "))
op = input("Enter the operator(+, -, *, /, //, %): ")
num_2 = float(input("Enter the second number: "))
if op == "+":
  print(num_1 + num_2)
elif op == "-":
  print(num_1 - num_2)
elif op == "*":
  print(num_1 * num_2)
elif op == "/":
  print(num_1 + num_2)
elif op == "//":
  print(num_1 // num_2)
elif op == "%":
  print(num_1 % num_2)
else:
  print("Invalid operator")

if True:
  print("ıt is true")

if False:
  print("ıt is true")

if 0:
  print("ıt is true")

if 3:
  print("ıt is true")

if None:
  print("ıt is true")

age = input("Enter your age : ")
while not age.isdigit() :
    print("You entered incorrectly!")
    age = input("Enter your age correctly please : ")
print("Great! You entered valid age :", age)

number = 23
number=int(input("Enter a number:"))
print("number")
if number>=10 :
      print("The number is equal or greater than 10")
elif number<10:
      print("The number is equal or less than 10")
else:
      print("None")

number = 23
number=int(input("number"))
if number>=10 :
      print("The number is equal or greater than 10")
else :
      print("The number is equal or less than 10")


for i in {'n1' : 'one', 'n2' : 'two'} :
   print(i)

iterable = [1, 2, 3, 4]


for iterable in iterable:
    print(iterable)

  sayac=0
flowers=['Rose', "Orchid", 'Tulip']
while len(flowers)> sayac:
    print (flowers [sayac])
sayac+1


strs = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac"]
anag = {}
for i in strs:
    element = "".join(sorted(i))
    if element in anag:
        anag[element].append(i)
    else:
        anag[element] = [i]
print(list(anag.values()))

# initialize the list of an integer array representing the elevation, and set it to empty
height = []
# Unless user types `ok`, get input of numbers from the user
while True:
    num = input("Type 'ok' when you are done: ")
    # if the input is not equal to `ok`, add the input number to the height array
    if num != "ok":
        height.append(int(num))
    # if the input equals to `ok`, get out of the while loop
    else:
        break
# initialize areas which holds total amount of water to be trapped, and set to 0
areas = 0
# initialize maximum left and right, and set to 0
max_l = max_r = 0
# initialize left, and set to 0
l = 0
# initialize right and set to the last index of the input array
r = len(height)-1
# unless the current position of the height on left
# is not greater than the one on right, run the loop
while l < r:
    # if the current position on left is lower than the right,
    # max level on left determines the amount of water to be trapped.
    if height[l] < height[r]:
        # if the current height on left is greater than max height on left
        # then the water not to be trapped, and set the max height to the new max
        if height[l] > max_l:
            max_l = height[l]
        # otherwise, add the amount of water to be trapped.
        else:
            areas += max_l - height[l]
        # increase current position on left by one
        l += 1
    # if the current position on left is higher than the right,
    # max level on right determines the amount of water to be trapped.
    else:
        # if the current height on right is greater than max height on height
        # then the water not to be trapped, and set the max height to the new max
        if height[r] > max_r:
            max_r = height[r]
        # otherwise, add the amount of water to be trapped.
        else:
            areas += max_r - height[r]
        # decrease current position on right by one
        r -= 1
# print the amount of water to be trapped
print("\nRain-trapped area : ", areas)

# initialzing a list of strings
anagrams = [‘cat’, ‘dog’, ‘fired’, ‘god’, ‘pat’, ‘tap’, ‘fried’, ‘tac’]
# initializing an empty dict
grouped_anagrams = {}
# iterating over the list to group all anagrams
for string in anagrams:
   # sorting the string
   sorted_string = str(sorted(string))
   # checking the string in dict
   if sorted_string in grouped_anagrams:
      # adding the string to the group anagrams
      grouped_anagrams[sorted_string].append(string)
   else:
         # initializing a list with current string
         grouped_anagrams[sorted_string] = [string]
# printing the values of the dict (anagram groups)
print(list(grouped_anagrams.values()))

liste=["eat", "tea", "tan", "ate", "nat", "bat"]
sorted_list=[]
sonuc=[]
for i in liste:
  if sorted(i) not  in sorted_list:
    sorted_list.append(sorted(i))
print(sorted_list)   
for a in range(len(sorted_list)):
  sonuc.append([i for i in liste if sorted(i)==sorted_list[a]])
print(sonuc)

sayi = 3

if sayi%2 == 0:
    print(str(sayi) + " çift sayıdır")
else:
    print(str(sayi) + " tek sayıdır")

yas = 28

if yas < 18:
    print("Ergensiniz")
elif yas >= 18 and yas < 66:
    print("Gençsiniz")
elif yas >= 66 and yas < 79:
    print("Orta yaşlısınız")
elif yas >= 80 and yas < 100:
    print("Yaşlısınız")
else:
    print("Yaş grubunuzu belirleyemedik!")

def faktoriyel(x):

    if x == 1:
        return 1
    else:
        return x * faktoriyel(x-1)

sonuc = faktoriyel(5)

print(sonuc)

class ogrenci: 
    isim = None 
    yas = None
    
    def selamVer():
        print("Merhaba")

saved_amount = int(input('Please enter your saved amount: '))
if saved_amount <= ps4_price/2:
    print('You must save more, keep saving!')
elif saved_amount > ps4_price/2 and saved_amount < ps4_price:
    print('You saved more than half, keep saving!')
else:
    print('Yippee! You can buy your PS4')

math_mark = int(input('Please enter the mark: '))

if math_mark >= 85:
    print('A (Excellent)')
elif math_mark < 85 and math_mark >= 70:
    print('B (Good)')
elif math_mark < 70 and math_mark >= 60:
    print('C (Medium)')
elif math_mark < 60 and math_mark >= 45:
    print('D (Not Bad)')
else:
    print('F (Failed)')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in [range]([len](weekdays)):
    print('Day', day+1, ':', weekdays[day])

sayı = int (input ('Lütfen bir sayı girin:')) 
count = 0 
while count <sayı: 
    print (count ** 2) 
    count += 1

sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

for i in sample_list:
   print ("The type of", i, "is", type(i))

sentence = input("give me a sentence :")
words = sentence.split()
i = 0
longest = 0
while i < len(words) :
    if len(words[i]) > longest :
        longest = len(words[i])
    i += 1
print("the lengt of the longest word is :", longest)

word = input("Give me a word")
for i in word:
    print(i, end="-")

user = {"name": "Daniel", "surname": "Smith", "age": 35}
for attribute in user:
    print(attribute)

wordss = ["abd", "bad", "dab", "abc", "acb", "abe", "aeb", "abf"]
list1 = []
list2 = []
list3 = []
list4 = []
for kelime in wordss :
    for harf in kelime:
        if harf == "d" :
            list1.append(kelime)
        elif harf == "c" :
            list2.append(kelime)
        elif harf == "e" :
            list3.append(kelime)
        elif harf == "f" :
            list4.append(kelime)
print(list1, list2, list3, list4, sep="\n")

evens = 0
odds = 0
for i in numbers :
    if not i%2 :
        evens += 1
    else:
        odds += 1
print("The count of even numbers : ", evens)
print("The count of odd numbers : ", odds)

liste = []
for i in range(75):
    liste.append(i)
summ = sum(liste)
print(summ)

a = []
for i in range(1,75):
  a.append(i)
sum(a)

names = ["susan", "tom", "edward"]
mood = ["happy", "sad"]
for i in names:
    for ii in mood:
        print(i +" is "+ ii)

sentence = input("give me a sentence")
words = sentence.split()
i=0
longest=0
while i < len(words):
    if len (words[i])> longest:
      longest = len(words[i]) 
      i+=1


amount = int (input(“How many numbes will you enter?:  "))
new=[]
i=1
for i in range(1,amount+1):
  new.append(int(input(“Please enter the number: “)))
  i+=1
sorted_new=sorted(new,reverse=True)
print(“The largest number is “,sorted_new[0])

number=int(input("enter a positive number:   "))
if number!=2: 
  if not number%2 or not number%3 or not number%5 or not number%7:
    print("{} is not a prime number".format(number))
  else:
    print("{} is  a prime number".format(number))
else:
  print("{} is not a prime number".format(number))

number=int(input("enter a positive number:   "))
n=2
check=False
while n<number:
  if number%n:
    check=True
  n+=1
if check:
  print("{} is not a prime number".format(number))
else:
  print("{} is a prime number".format(number))





grocery = "bread", "water", "oil"
enum_grocery = list(enumerate(grocery,1000))
print(enum_grocery)


number = int(input("Please enter a number : "))
for i in range(2,number):
    if number%i==0:
        print(number,"is not a prime number")
        break
else:
    print(number,"is a prime number")

n = int(input("Enter a number to check if it is a prime number."))
count = 0
for i in range(1, n+1) :
    if n % i == 0 :
        count += 1
if (n == 0) or (n == 1) or (count >=3) :
    print(n, "is not a prime number.")
else:
    print(n, "is a prime number")


fruits = {'Apples': 5, 'Oranges': 3, 'Bananas': 4}
fruit_names = [x for x in fruits.keys()]
print( fruits)
print(fruit_names)


i = 5
while True:
 if i%0O11 == 0:
  break
 print(i)
 i += 1   
 


x = 'abcd'
for i in range(len(x)):
 i[x].upper()
print (x)


k=[2,3,4]
k2=list(reversed(k)) 
print(k2)

def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter.lower() in vowels:
        return True
    else:
        return False
        

sentence = "the clarusway is the best"
filteredVowels = filter(filterVowels, sentence)
print(filteredVowels)

def pos_args(a, b):
    print(a, 'is the first argument')
    print(b, 'is the second argument')
pos_args(3,4)
print()
pos_args(4,3)

x = 'abcd'
for i in range(len(x)):
 x1=x[i].upper()
print (x1)


def slicer(*nums):
    even_list = []
    odd_list = []
    for i in nums:
        if nums %2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
print("even_list:", even_list)

          

def organizer(**a):
    keys=[]
    values=[]
    for key, value in a.items():
        keys.append(key)
        values.append(value)
       organizer(beth=26,oscar=42,justin=15,frank=33)       
    print(keys)
    print(values)

def my_function(a,b):
    print(a*b)
my_function(10,20)


def my_function (a,b):
    print (a**2 + b**2)**0.5
my_function (3,4)

def my_function (a,b):
    hypotenuse= (a**2 + b**2)**0.5
    print (hypotenuse)
print(my_function (3,4))

def my_function(a,b):
    area = a*b
    print(area)
print(my_function(8,6))

def longer(a, b):
    if len(a) >= len(b):
        return a
    else:
        return b

print(longer('Richard', 'John'))

def my_function(a, b):
    hypotenuse = (a**2 + b**2)**0.5
    return hypotenuse
my_function(4,3)    


def gene(x, y):  # defined by positional args
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")
 
dict_gene = {'y' : "Marry", 'x' : "Fred"}
gene(**dict_gene)  # we call the function by a single argument(variable)


def gene(x='Solomon', y='David'):  # defined by kwargs (default values assigned to x and y)
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")
 
dict_gene = {'y' : "Marry", 'x' : "Fred"}
gene(**dict_gene) 

nums1 = [9, 6, 7, 4]
nums2 = [3, 6, 5, 8]
numbers = list(map(lambda x, y : (x+y)/2, nums1, nums2))
print(numbers)

word1 = ["you", "much", "hard"]
word2 = ["i", "you", "much"]
word3 = ["love", "ate", "works"]
result = map(lambda x, y, z : x +' ' + y + ' ' + z, word2, word3, word1)
for i in result:
  print(i)

vowel_list = ["a","e","i","o","u"]
first_ten =["a","b","c","d","e","f","g","h","i","j"]
vowels = filter(lambda x: True if x in vowel_list else False, first_ten)
print("Vowels are : ", list(vowels))

def repeater(n):
    return lambda x: x * n
repeat_2_times = repeater(2)  # repeats 2 times
repeat_3_times = repeater(3)  # repeats 3 times
repeat_4_times = repeater(4)  # repeats 4 times
print(repeat_2_times('alex '))
print(repeat_3_times('lara '))
print(repeat_4_times('linda '))

def functioner(emoji = None):
    return lambda message: print(message, emoji)
(lambda message: print(message, ":)"))(66)
(lambda message: print(message, ":)"))([66])
print_smile = functioner(":)")
print_sad = functioner(":(")
print_neutral = functioner(":|")
print(print_smile("Hello"))
print(print_sad("bugünkü dersteki yüz ifadem -->"))
print(print_neutral("Hello"))

def function1(var1=5, var2=7):
 var2=9
 var1=3
 print (var1, " ", var2)
function1(10,12)




SEHİR="İSTANBUL"
print(SEHİR)

sehir= {2: "istanbul", 3: "ankara", "number": 40}
print(sehir)
print(list(sehir.items()))

colors= "red","blue", "pink"
print(type(colors))


bos= set()


num1= int(input("enter first number:"))
num2=int(input(" enter second number:"))
num3= int((input( "enter third number:"))
if (num1>num2) and (num1>num3):
  print("the larger number is", num1)
   elif (num2>num3) and (num2>num1):
    print("the larger number is", num2")
     else: 
      print("the larger number is", num3) 

sentence=input("give me a sentence:")
words= sentence.split()
i=0
longest=0
while i < len (words):
  if len (words[i]) > longest:
    longest= len (words[i])
    i+=1
    print ("the length of the longest word is:")


kardiz = input("Kısaltmasını öğrenmek istediğiniz kurum adını girin: ")

for i in kardiz.split():
    print(i[0], end="")



# Yeni Bölüm

pwd


pip--version

!pip list

pip show yellowbrick 

pip install pep8

pwd


from upper_package import my_package1, my_package2


from upper_package.my_package1 import my_module_1, my_module_2

dir(my_package1)

from upper_package.my_package2 import my_module_3, my_module_4

my_module_2.divide(10,5)

my_module_1.addition(4,5)

my_package1.__spec__

from upper_package.my_package1.my_module_2 import divide, hello 

hello ()

divide (22, 11)

import math

from math import log10



log10(1000)

print(math.__doc__)

print(my_module_2.__doc__)

print(my_module_3.repeater(3, 6))

print(my_module_4.__doc__)

pip --version

! pip list 

pip show pep8

pip install pep8

pip show pep8

