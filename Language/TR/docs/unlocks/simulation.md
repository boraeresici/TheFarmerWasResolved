# Simülasyon

Simülasyonlar, gerçek çiftliğin durumunu değiştirmeden kodu hızlıca test etmenizi sağlar.
Simülasyonun başlangıç durumu serbestçe seçilebilir ve simülasyon bittiğinde gerçek çiftlik, simülasyon başlamadan önceki durumuyla tamamen aynı olur.

Simülasyonu başlatmak için `simulate()` fonksiyonu kullanılır.

çalıştırmanın başlayacağı dosya
`filename = "f1"`

her şey kilidi açık ve tam yükseltilmiş şekilde başla
`sim_unlocks = Unlocks`

10000 havuç ve 50 samanla başla
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

"a" adında 13 değerli bir global değişkenle başla
`sim_globals = {"a" : 13}`

sabit bir rastgele tohum kullan
`seed = 0`

simülasyonu 64 kat hızlandır
`speedup = 64`

simülasyonu çalıştır
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

`simulate()` fonksiyonu, verilen başlangıç dosyasını simüle etmenin kaç saniye sürdüğünü döndürür.

### Dosya Adı
Simulate fonksiyonunun ilk argümanı dosya adıdır. Bu, kod penceresinin üstünde görünen addır. Simülasyon, belirtilen dosyayı sanki üstündeki Çalıştır düğmesine tıklamışsınız gibi çalıştırır.

### Başlangıç Kilit Açmaları
Döngüler, if (koşul) ifadeleri, listeler, sözlükler gibi tüm programlama özellikleri her zaman açık kalır.

İkinci argüman, simülasyonun programlama özelliklerine ek olarak hangi kilit açmalar/yükseltmelerle başlayacağını belirtmenizi sağlar. Bu, kilit açmalardan oluşan bir dizidir. Simülasyon, dizideki tüm kilit açmaları maksimum seviyede başlatır.

Maksimumdan farklı bir yükseltme seviyesi belirtmek istiyorsanız, kilit açmaları seviyelerle eşleyen bir dictionary (sözlük) verebilirsiniz. Bu durumda negatif değerler maksimum kilit açma seviyesine karşılık gelir.

### Başlangıç Öğeleri
Üçüncü argüman, öğeleri sayılarla eşleyen bir dictionary (sözlük) vermenizi sağlar. Bu, simülasyona hangi öğelerle başlanacağını belirtir.

### Başlangıç Globals
Simülasyon tamamen yeni bir program çalıştırdığı için, simülasyonu başlatan programdaki değişkenlere erişemezsiniz.
Ancak dördüncü argümanla simülasyona değerler aktarabilirsiniz. Bu, değişken adlarını (string olarak) değerlere eşleyen bir sözlüktür. Bu değişkenler simülasyon içindeki çalıştırmanın global kapsamına eklenir.

Bunun tüm değerleri kopyaladığını unutmayın; simülasyon içinde değiştirmeniz, dışarıdaki orijinal değerleri etkilemez. Simülasyondan, çalıştırma süresi dışında değer döndürmek mümkün değildir.

### Rastgele Tohum
Beşinci argüman simülasyonda kullanılan rastgele tohumu belirtmenizi sağlar. Bu pozitif bir tamsayı olmalıdır. Negatif değerler rastgele tohum kullanılmasına neden olur.

Rastgele tohum; bitki büyüme sürelerinden labirent düzenlerine ve su azalım sürelerine kadar her şeyi etkiler. Aynı rastgele tohumu ve aynı başlangıç koşullarını kullanarak aynı simülasyonu birden fazla kez başlatırsanız sonuç her zaman aynı olmalıdır.

### Hızlandırma
Altıncı argüman simülasyonun başlangıç hızlandırmasıdır. Bu, işleri hızlıca test etmenizi sağlar. Oyun ayarlanan hıza yetişemezse otomatik olarak yavaşlar.

Hızlandırma, simülasyon sonucunu hiçbir şekilde etkilemez. Sadece bekleme süresini azaltmak için vardır.
