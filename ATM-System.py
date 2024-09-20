print(
    """
██████████████████████████████████
█────█───█─███─████────█────█────█
█─██─██─██──█──████─██─█─██─█─██─█
█────██─██─█─█─████────█────█─██─█
█─██─██─██─███─████─████─█─██─██─█
█─██─██─██─███─████─████─█─██────█
██████████████████████████████████
Author : A.Vahap Doğan

Merhaba işlem yapılabilmesi için sizden bir kart şifresi isteyecektir. Şifre: 1453 olacaktır ve diğer istemlere göre işlemlerinizi yapabilirsiniz.
    """
)

retry_count = 3
while retry_count > 0:
    try:
        sifre = int(input("Kart Şifresi : "))
        if sifre == 1453:
            break
        else:
            retry_count -= 1
            print(f"Hatalı Şifre. Kalan deneme hakkı: {retry_count}")
    except ValueError:
        print("Şifre sadece sayılardan oluşur!")

while True:
    try:
        name = input("Adınız: ")
        anapara = int(input("Ana Para Miktarı: "))
        break
    except ValueError:
        print("Sadece sayı giriniz!")

transaction_history = []

def record_transaction(transaction_type, amount):
    transaction_history.append(f"{transaction_type}: {amount} ₺")

print(
    """
Hoşgeldin {}. 
Hesabınızdaki para miktarı: {} ₺
İşlemler için lütfen bir işlem numarası seç:

1 -- Para Çekme
2 -- Para Yatırma
3 -- Bakiye Öğrenme
4 -- Para Transferi
5 -- İşlem Geçmişi
q -- Çıkış
""".format(name, anapara))

daily_withdrawal_limit = 1000
withdrawn_today = 0

while True:
    işlem = input("İşlem Numarası: ")
    if işlem == "1":
        while True:
            print("\n \n----- Para Çekme İşlemi ----- \n")
            try:
                çekilecek_para = int(input("Çekilecek Para Miktarı: "))
                if çekilecek_para > anapara:
                    print("Bakiye Yetersiz. Hesabınızdaki para miktarı: ", anapara)
                    print("Lütfen tekrar deneyiniz!")
                elif çekilecek_para + withdrawn_today > daily_withdrawal_limit:
                    print("Günlük para çekme limitini aştınız.")
                else:
                    durum = True
                    while durum:
                        onay_para_çekimi_giriş = input(
                        "Hesabınızdan {} ₺ miktarında para çekilecek. Onaylıyor musunuz? '(E/H)' : )".format(çekilecek_para))
                        onay_para_çekimi = onay_para_çekimi_giriş.upper()
                        if onay_para_çekimi == "E":
                            anapara -= çekilecek_para
                            withdrawn_today += çekilecek_para
                            record_transaction("Para Çekme", çekilecek_para)
                            print("Hesabınızdan {} ₺ miktar para çekildi. Kalan anaparanız: {}".format(çekilecek_para, anapara))
                            durum = False
                            break
                        elif onay_para_çekimi == "H":
                            print("İşleminiz gerçekleşmedi.")
                            durum = False
                            break
                        else:
                            print("Geçersiz İşlem!")
                            durum = True
                    break
            except ValueError:
                print("Lütfen sadece sayı giriniz!")

    elif işlem == "2":
        while True:
            print("\n \n----- Para Yatırma İşlemi ----- \n")
            try:
                yatırılacak_para = int(input("Yatırılacak para miktarı: "))
                anapara += yatırılacak_para
                record_transaction("Para Yatırma", yatırılacak_para)
                print("Hesabınıza {} ₺ para yatırıldı. Güncel anaparanız: {}".format(yatırılacak_para, anapara))
                break
            except ValueError:
                print("Sadece sayı giriniz!")

    elif işlem == "3":
        kötü = " bilmenizi isteriz."
        iyi = " söylemekten sevinç duyarız."
        if anapara < 500:
            print(
            """
            \n \n----- Bakiye Öğrenme ----- \n
            Merhaba {}. Umarım güzel bir geçiriyorsunuzdur :)
            Hesabınızdaki para miktarının {} ₺ olduğunu {}
            """.format(name, anapara, kötü))
        else:
            print(
            """
            \n \n----- Bakiye Öğrenme ----- \n
            Merhaba {}. Umarım güzel bir geçiriyorsunuzdur :)
            Hesabınızdaki para miktarının {} ₺ olduğunu {}
            """.format(name, anapara, iyi))

    elif işlem == "4":
        while True:
            print("\n \n----- Para Transferi ----- \n")
            try:
                transfer_no = int(input("Transfer edilecek IBAN Numarasını Yazınız: TR"))
                if len(str(transfer_no)) == 24:
                    transfer_para = int(input("Gönderilecek Para Miktarı: "))
                    durum1 = True
                    while durum1:
                        if anapara >= transfer_para:
                            transfer_onay_giriş = input(
                                "Hesabınızdan {} IBAN numarasına {} ₺ para transferi yapılacak. Onaylıyor musunuz? (E/H): ".format(
                                    transfer_no, transfer_para))
                            transfer_onay = transfer_onay_giriş.upper()
                            if transfer_onay == "E":
                                anapara -= transfer_para
                                record_transaction("Para Transferi", transfer_para)
                                print("İşleminiz başarıyla gerçekleştirildi. İşlem sonu bakiyeniz: {} ₺".format(anapara))
                                durum1 = False
                                break
                            elif transfer_onay == "H":
                                print("İşleminiz iptal edildi.")
                                durum1 = False
                                break
                            else:
                                print("Geçersiz İşlem!")
                                durum1 = True
                    else:
                        print("Bakiyeniz Yetersiz!")
                else:
                    print("IBAN no 24 basamaklı olmalıdır!")
            except ValueError:
                print("Sadece sayı giriniz!")

    elif işlem == "5":
        print("Geçmiş İşlemler:")
        for transaction in transaction_history:
            print(transaction)

    elif işlem.lower() == "q":
        exit_confirmation = input("Çıkmak istediğinize emin misiniz? (E/H): ").upper()
        if exit_confirmation == "E":
            print("İşlem Sonlandı.")
            break
    else:
        print("Geçersiz İşlem!")
