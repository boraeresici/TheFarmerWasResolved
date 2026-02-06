# Gübre
Bir noktadan sonra bitkilerin büyümesini beklemek artık yeterince verimli olmaz.
Suya benzer şekilde, her 10 saniyede bir otomatik olarak 1 gübre alırsınız ve her yükseltmeyle bu miktar iki katına çıkar.

Gübre, bitkilerin anında büyümesini sağlayabilir. `use_item(Items.Fertilizer)` drone'un altındaki bitkinin kalan büyüme süresini 2 saniye azaltır.

Bunun bazı yan etkileri vardır.
Gübreyle büyütülen bitkiler enfekte olur.

Bir bitki enfekte olduğunda, hasat edildiğinde veriminin yarısı `Items.Weird_Substance` olur.
Weird Substance bitkilerde de kullanılabilir; bu, bitkinin ve bitişik tüm bitkilerin enfekte durumunu açıp kapatır.

Yani `use_item(Items.Weird_Substance)` enfekte bir bitkide kullanılırsa onu iyileştirir, sağlıklı bir bitkide kullanılırsa onu enfekte eder.

Sağlıklı komşuları olan enfekte bir bitkide kullanırsanız bitkiyi iyileştirir ama komşuları enfekte eder ve bunun tersi de geçerlidir.
