#bai 1
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory["pocket"]=[ 'seashell', 'strange berry',  'lint']

print (inventory)
del inventory["backpack"][1]
inventory["gold"] += 50
print (inventory)



# bai 2
price = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
xuat = {}
for i in price :
    print (i)
    print ("gia tien :",price[i])
    print ("chứng khoán :",stock[i])
for i in price :
    xuat[i]=price[i]*stock[i]
print(xuat)
tong = 0
for k in range(len(xuat)):
    tong= tong + xuat[i]
print ("so tien  co dc la",tong)

#bai 3 
while True :
    print ("nếu x = 8,đâu là giá trị của 4(x+3) ?")
    dic = {"1":"34","2":"36","3":"40","4":"44"}
    for i in dic :
        print (i,",",dic[i])
    nhap = int (input ("mời nhập đáp án :"))  
    if nhap == 4:
            print ("bingo")
            break
    else :
            print (":(")
# bai 4
print ("nếu x = 8,đâu là giá trị của 4(x+3) ?") 
dic = {"1":"34","2":"36","3":"40","4":"44"}
for i in dic :
    print (i,",",dic[i])
nhap = int (input ("mời nhập đáp án :"))  
if nhap == 4:
    print ("bingo")
    a=1 
else :
    print (":(")
    a=0
print ("Jack đã đạt được những điểm này trong 5 bài kiểm tra toán: 49,81,72,66 và 52. Nghĩa là gì")
dic2 = {"1":"about 55","2":"about 65","3":"about 75","4":"about 85"}
for k in dic2 :
    print (k,",",dic[k])
nhap2 = int (input ("mời nhập đáp án :"))
if nhap2 == 2 :
    print ("bingo")
    b=1
else :
    print (":(")
    b=0
print ("bạn đã trả lời đúng ",a+b,"trong 2 câu hỏi") 