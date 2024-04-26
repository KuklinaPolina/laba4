import random


def a():
    n = 100
    z = 1
    while z <= n:
        print("Eclu xotute octanobut pragramu bbegute 0")
        s = int(input("Bbedute chuclo: "))
        if s == 0:
            break
        if (s % 3) == 0:
            print("Chuclo delutca na 3")
        else:
            print("Chuclo ne delutca na 3")
def b():
    try:
        s = 100
        n = int(input("Bbegute chuslo na kotoroe xotute pazgelut 100 "))
        o = s / n
        print("Polychutca: ", o)
    except ValueError:
        print("Pogelut na ctpoky nelza!")
    except ZeroDivisionError:
        print("Pogelut na 0 nelza!")
def c():
    d = int(input("Bbedute den: "))
    m = int(input("Bbedute mecac: "))
    g = int(input("Bbedute god: "))
    a1 = d * m
    a2 = int(g - 2000)
    def tf(a1, a2):
        if a1 == a2:
            return True
        else:
            return False
    print(tf(a1, a2))

def a2():
    A = str(input("Введите номер билета"))
    B = len(A)
    if (B % 2) == 0:
        C = B // 2
        D = sum(int(i) for i in A[:C])
        H = sum(int(i) for i in A[C:])
        if D == H:
            print("Билет счастливый")
        else:
            print("Билет не счастливый")
    else:
        print("kolichistvo cisel v bilete ne chotnoe")
a2()
def g5():
    a = random.randint(0,100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    d = random.randint(0, 100)
    e = random.randint(0, 100)
    s = 3





