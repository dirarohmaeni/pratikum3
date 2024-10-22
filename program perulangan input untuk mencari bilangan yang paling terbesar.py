max = 0

while True:
    
    x = int(input("Masukkan bilangan (0 untuk berhenti): "))
    

    if x == 0:
        break
    
    
    if x > max:
        max = x

print("Bilangan terbesar adalah:", max)
