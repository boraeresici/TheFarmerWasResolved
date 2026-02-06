# Sulama
Bitkiler sulandığında daha hızlı büyür. Zeminin su seviyesi `0` ile `1` arasındadır.
`get_water()` fonksiyonu, üzerinde bulunduğu zeminin su seviyesini döndürür.

Bir bitkinin büyüme hızı, su seviyesi 0 iken 1x ve su seviyesi 1 iken 5x olacak şekilde doğrusal olarak artar.

Zemin zamanla kurur: Ortalama olarak saniyede mevcut suyunun %1'ini kaybeder, ancak bunda biraz rastgele değişkenlik vardır. Yüksek bir su seviyesini korumak, düşük bir seviyeyi korumaktan çok daha fazla su tüketir.

Bitkilerinize su kullanabilirsiniz. Her 10 saniyede envanterinize otomatik olarak 1 su tankı eklenir.
`Unlocks.Watering` yükseltmesi, her 10 saniyede aldığınız su miktarını iki katına çıkarır.

Bir tank `0.25` su tutar.

Herhangi bir zeminin üzerinde `use_item(Items.Water)` çağırarak zemini sulayın.
