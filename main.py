def zad1(number):
    try:
        if int(number) % 3 == 0:
            print("Делится")
        else:
            print("Не делится")
    except:
        print("Вы ввели что-то не то")

zad1(input("Введите число: "))

def zad2(number):
    try:
        answer = 100/int(number)
    except ValueError:
        print("Вы ввели не число")
    except ZeroDivisionError:
        print("На 0 делить нельзя")
    else:
        print(100 / int(number))

zad2(input("Введите делитель для 100: "))

def zad3(date):
    try:
        if int(date.split(".")[0]) > 12 or int(date.split(".")[1]) > 12 or int(date.split(".")[1]) < 1 or int(date.split(".")[0]) < 1:
            return "Вы неправльно ввели дату или месяц"
        else:
            if int(date.split(".")[0]) * int(date.split(".")[1]) == int(date.split(".")[2][2:]):
                return True
            else:
                return False
    except:
        return "Вы ввели дату неправильно"
print(zad3(input("Введите дату: ")))

def zad4(num):
    try:
        sum1 = 0
        sum2 = 0
        for i in num[:int(len(num) / 2)]:
            sum1 += int(i)
        for j in num[int(len(num) / 2):]:
            sum2 += int(j)
        if sum1 == sum2:
            print("У вас счастливый билетик")
        else:
            print("У вас не счастливый билетик")
    except:
        print("Вы ввели что-то не то")

zad4(input("Введите номер билетика: "))
