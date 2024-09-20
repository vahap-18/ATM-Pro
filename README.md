# ATM Sistemi Projesi

Bu Python programı, para çekme, para yatırma, bakiye öğrenme ve para transferi işlemlerini gerçekleştiren bir ATM simülasyonudur. Kullanıcı, ATM sistemine giriş yapmak için bir kart şifresi girmekte ve ardından çeşitli finansal işlemler gerçekleştirmektedir.

## Özellikler

- **Kullanıcı Girişi**: Kullanıcıdan bir kart şifresi ve isim alınır.
- **Para Çekme**: Kullanıcı, hesabından para çekebilir. Bakiye kontrolü yapılmaktadır.
- **Para Yatırma**: Kullanıcı, hesabına para yatırabilir.
- **Bakiye Öğrenme**: Kullanıcı, hesabındaki bakiyeyi öğrenebilir. Bakiyenin durumu hakkında kullanıcıya bilgi verilir.
- **Para Transferi**: Kullanıcı, belirtilen IBAN numarasına para transferi yapabilir. IBAN doğrulaması sağlanmaktadır.
- **Gelişmiş Hata Yönetimi**: Kullanıcıdan gelen hatalı girişler için kullanıcı dostu hata mesajları verilmektedir.
- **İlerleme Çubuğu**: İşlemler sırasında bir ilerleme çubuğu gösterilir.

## Gereksinimler

Bu programı çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

- `tqdm` (İlerleme çubuğu için)

Gerekli kütüphaneyi yüklemek için:

```bash
pip install tqdm
```

## Kullanım

1. **Programı çalıştırın**:
   Programı başlatmak için terminalde aşağıdaki komutu çalıştırın:

   ```bash
   python atm_system.py
   ```

2. **Giriş Bilgilerini Girin**:
   Program çalıştırıldığında sizden bir kart şifresi ve adınız istenecek.

3. **İşlemleri Seçin**:
   İşlem numarasını girerek para çekme, yatırma, bakiye öğrenme veya para transferi yapabilirsiniz.

4. **Programdan Çıkış**:
   İşlem tamamlandığında veya çıkmak istediğinizde 'q' tuşuna basarak programdan çıkabilirsiniz.
