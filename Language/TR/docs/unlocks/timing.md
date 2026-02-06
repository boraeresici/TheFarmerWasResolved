# Zamanlama
Yöntemlerinizi gerçekten optimize etmek istiyorsanız bu oyunda zamanın nasıl ölçüldüğünü anlamanız gerekir. Bu kilit açma tamamen bununla ilgilidir.

## Yeni Fonksiyonlar
Bir şeylerin ne kadar sürdüğünü ölçmek için iki faydalı fonksiyon vardır:

`get_time()` oyunun başlangıcından beri geçen süreyi saniye cinsinden döndürür.

`get_tick_count()` çalıştırmanın başlangıcından beri yapılan tik sayısını döndürür.

Bu iki fonksiyon ve `quick_print()` tamamen ücretsizdir. Hatta çağrı işlemi bile ücretsizdir.

## Çalışma Süresi Ayrıntıları

### Ön Bilgi
Bu, gerçek dünyada performansın nasıl çalıştığı değildir. Bunlar, oyunda tutarlı ve anlaşılır bir zamanlama modeli olması için uydurulmuş kurallardır.
Muhtemelen yalnızca kodunuzu aşırı optimize etmek isterseniz önem vereceksiniz.

Kod çalıştırmanın temel zaman birimine "tik" denir. Hız yükseltmeleri ve güç olmadan, çalıştırma saniyede `400` tik hızında ilerler.

Genel olarak, `+, -, *, /, //, %, and, or, ...` gibi iki değeri birleştiren işlemler çalışmak için bir tik alır.
Tek değerli `-` ve `not` ücretsizdir.
Bir `if` dalı da çalışmak için bir tik alır (koşul ifadesini değerlendirme süresine ek olarak).
Fonksiyon çağrıları ve değişken okuma/yazmaları ücretsizdir ama fonksiyon tanımları 1 tik alır.
`import` ifadeleri ücretsizdir.
`.` operatörüyle içe aktarılmış bir modüle erişmek ücretsizdir.
Bir fonksiyon veya modül argümanlar ya da değişken atamalarıyla geçirilmişse, onu kullanmak 0 yerine 1 tik tutar.
`for` ve `while` döngülerinin başlaması bir tik alır, ancak yinelemeler ücretsizdir (koşul/dizi ifadelerini değerlendirme süresi hariç).
`return`, `break` ve `continue` tamamen ücretsizdir.
`pass` bir tik alır; bu yüzden hassas gecikmeler oluşturmak için kullanılabilir.
Bir veri yapısına indeksleme, indeks operatörü için bir tik alır ve dictionary (sözlük) ya da set (küme) durumunda, anahtarın boyutuna bağlı olarak ek tikler alır.

Yerleşik fonksiyonların yürütme sırasında kaç tik aldığı, her fonksiyonun kendi dokümantasyonunda ayrıca belirtilmiştir.
