# Kumpul di moodle, by Michael Jonathan Sandy
n = int(input("Masukan bilangan :"))
while n < 20 or n % 2 == 0:
    print("Bilangan salah !")
    n = int(input("Masukan bilangan :"))
else:
    print("Benar")