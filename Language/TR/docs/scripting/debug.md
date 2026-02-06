# Debug (Hata Ayıklama)
Bazen kodunuz çalışmaz ve nedenini bulmanız gerekir. Bunun için yardımcı olacak birkaç araç vardır.

İlki, programı adım adım çalıştırmaktır.
Çalıştır düğmesinin yanındaki düğmeyle ya da bir kesme noktası (breakpoint) koyarak adım adım moduna geçebilirsiniz.

Kesme noktaları, kodun solundaki kesme noktası paneline tıklanarak eklenebilir.
![](Breakpoints227)
Çalıştırma, kesme noktasının olduğu satıra geldiğinde otomatik olarak adım adım moduna geçer.

Bir değişkenin üzerine fareyi getirirseniz, mevcut değeri gösterilir.

`print()` fonksiyonu da çok faydalıdır. Kendisine verilen herhangi bir değeri doğrudan havaya yazar.

Örnekler:

"0.24" yazdır.
`print(0.24)`

"True" ya da "False" yazdır.
`print(can_harvest())`

Mevcut konumu yazdır.
`print(get_pos_x(), get_pos_y())`

Print fonksiyonu değeri doğrudan havaya ve [Çıktı](docs/output.md) sayfasına yazdırır.

Havaya yazmak, çok fazla değer yazdırmak istiyorsanız bazen biraz yavaş olabilir.
Bu durumda sadece çıktı penceresine yazdıran `quick_print()` fonksiyonunu kullanabilirsiniz.

Çıktı penceresi uyarıları ve hataları da kaydeder; bu yüzden bir şey beklendiği gibi çalışmıyorsa kontrol etmek faydalı olabilir.

Çalıştırma durduğunda çıktı, oyun klasöründeki output.txt dosyasına da yazılır. [output.txt](persistent_data_path/output.txt).
