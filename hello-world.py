

umur = 11
susu = 1
telur = 2
print(f"Hello python user umur kamu sekarang adalah {umur}")


if umur > 18:
    print("Anda sudah dewasa")
elif umur <= 20: 
    print("Anda masih anak-anak, \"Terima kasih telah mendaftar\"")


if telur > 6:
    susu = 6 
    print("Kamu membawa susu sebanyak", susu )
elif telur <= 6: 
    print("Kamu membawa susu hanya", susu)
    
#Perulangan
    for i in range(umur):
        print(f"Ini adalah umur ke {i}")

#Perulangan dengan while 
