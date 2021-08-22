# enkripsi-CaesarCipher-Python

def header():
    print("ENKRIPSI DAN DEKRIPSI CAESAR CIPHER")
    print("Copyright Ridhomr")

def menu():
    while True:
        print()
        print(" MENU ")
        print("1. Enkripsi ")
        print("2. Dekripsi")
        print("3. Exit")
        print()

        input_menu = int(input("Masukan Menu yang anda pilih, ex [1] ? "))
        if input_menu == 1:
            hasil_enkripsi = enkripsi()
            print()
            print("Hasil enkripsi: " + hasil_enkripsi)
            print("Kembali ke Menu Awal.....")
        elif input_menu == 2:
            dekripsi()
            print()
            print("Hasil dekripsinya bisa di lihat di atas")
            print("Kembali ke Menu Awal.....")
        elif input_menu == 3:
            break
        else:
            print("Error: pastikan anda memasukan angka yang benar !")


def enkripsi():
    input_text = str(input("Masukan Text yang akan anda enkripsi, ex [lindo] ? "))
    input_key = int(input("Masukan key/shift yang akan anda pakai, ex [number] ? "))
    result = ""
    #transverse the plain text
    for i in range(len(input_text)):
        char = input_text[i]
    # Encrypt uppercase characters in plain text

        if char.isupper():
            result += chr((ord(char) + input_key - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        elif char == " ":
            result += " "
        else:
            result += chr((ord(char) + input_key - 97) % 26 + 97)

    return result

def dekripsi():
    Alpabeth1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    #Alpabeth2 = "abcdefghijklmnopqrstuvwxyz"
    input_encrypted = str(input("Masukan pesan yang akan di dekripsi, ex [grgr wdpsdq] ?" ))

    for key in range(len(Alpabeth1)):
        translated = ""
        for symbol in input_encrypted:
            if symbol in Alpabeth1:
                num = Alpabeth1.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(Alpabeth1)
                translated = translated + Alpabeth1[num]
            else:
                translated = translated + symbol

        print('Hacking key #%s: %s' % (key, translated))

def main():
    header()
    menu()


if __name__ == '__main__':
    main()
