import random

#สุ่มเลขระหว่าง 0-9
test_random = random.randint(0, 20)

print("--เกมทายตัวเลข--")


#รับค่าการทายเลขจากผู้ใช้
guess_number = int(input("What is your guess number(0-20)ฦ: "))

# condition ==> if-elif-else
if test_random == guess_number:
    print("เก่งมาก")
        
elif guess_number < test_random:
    print("ผิด น้อยไป")

elif guess_number > test_random:
    print("ผิด มากไป")
