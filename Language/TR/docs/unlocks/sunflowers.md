# Ayçiçekleri
[Ayçiçekleri](objects/sunflower) güneşin gücünü toplar. Bu gücü hasat edebilirsiniz.

Ekimleri havuç veya kabak ekmekle tamamen aynıdır.

Büyümüş bir ayçiçeğini hasat etmek güç verir.
Çiftlikte en az 10 ayçiçeği varsa ve yaprak sayısı en fazla olanı hasat ederseniz `8` kat daha fazla güç alırsınız!
Eğer daha fazla yaprağı olan başka bir ayçiçeği varken bir ayçiçeğini hasat ederseniz, bir sonraki hasat ettiğiniz ayçiçeği de sadece normal güç verir (`8` kat bonus yok).

`measure()` drone'un altındaki ayçiçeğinin yaprak sayısını döndürür.
Ayçiçeklerinde en az `7`, en çok `15` yaprak olur.
Tam büyümeden önce de ölçülebilirler.

Birden fazla ayçiçeği aynı yaprak sayısına sahip olabilir; bu yüzden en fazla yaprağa sahip birden fazla ayçiçeği de olabilir. Bu durumda hangisini hasat ettiğinizin önemi yoktur.

Gücünüz olduğu sürece drone onu kullanarak iki kat hızlı çalışır.
Her 30 eylemde (hareket, hasat, ekim gibi) 1 güç tüketir.
Diğer kod ifadelerini çalıştırmak da güç tüketebilir ama drone eylemlerine göre çok daha azdır.

Genel olarak, hız yükseltmeleriyle hızlanan her şey güç tarafından da hızlandırılır.
Güçle hızlanan her şey, hız yükseltmelerini yok sayarak, yürütme süresiyle orantılı miktarda güç tüketir.
