# boolean là kiểu dữ liệu trả về 2 giá trị true hoặc flase 
# bool(5==6)
# bool(2==1+1)
# bool(5==7-1)
# Flowchart là một sơ đồ bao gồm các bước, và những điều kiện được sắp xếp theo trình tự nhất định để giải quyết 1 vấn đề.
# Khi lập trình, Developer thường hay dùng nó để thể hiện logic mà mình muốn code trước khi bắt tay vào làm. 
# Có thể nói, nó là loại chart dễ hiểu nhất đối với Developer.
# điều kiện lồng nhau 
# ex
# x=int (input ("mời nhập x :"))
# y=int (input ("mời nhập y :"))
# if x>y:
#     print ("x lớn hơn y")
# else :
#     if x<y:
#         print ("x nhỏ hơn y")
#     else:
#         print ("x bằng y")

#bài 1

x = float (input ("mời nhập cân nặng (kg): "))
y = float (input ("mời nhập chiều cao (cm) : "))
y = y/100
BMI=  x/(y*y)
print ("chỉ số BMI của bạn là : ",BMI)
if BMI<16 :
    print ("thiếu cân nghiêm trọng !!!")
elif 16<BMI<18.5:
    print ("thiếu cân")
elif 18.5<BMI<25:
    print ("bình thường")
elif 25<BMI<30:
    print("quá cân")
else:
    print ("béo phì")

# cách print mà không cần xuống dòng 
# print ("khối lệnh ",end= "" ) hoặc print (end="khối lệnh")
# print ("xin chào ",end="")
# print ("tên tôi là ",end="")
# print ("b-max",end="")

x = int (input ("mời nhập số :"))
for i in range (x):
    for a in range(x-1):
        print ("*",end="") 
        print ("x",end="")


n = int (input ("mời nhập n :"))
m = int (input ("mời nhập m :"))
for i in range (n):
        for c in range (m):
                print ("*",end=" ")
        print ()
                
