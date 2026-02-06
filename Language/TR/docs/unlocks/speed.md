# Hız Yükseltmesi
Çalıştırma hızı iki katına çıktı. Sorun şu ki drone artık çimin büyüyebileceğinden daha hızlı hasat ediyor ve sonuç olarak hiç hasat olmuyor. Bununla başa çıkmak için [if (koşul)](docs/scripting/if.md) dalları ve [can_harvest](functions/can_harvest) fonksiyonu artık açıldı.

## Hasat Etmeden Önce Kontrol
Şimdiye kadar koşul olarak yalnızca `True` ve `False` vardı; bu da `if` ile elbette pek kullanışlı değil.

Yeni `can_harvest()` fonksiyonu daha iyi bir koşul sağlar. `can_harvest()` drone'un altındaki bitki hasat edilebiliyorsa `True`, değilse `False` döndürür.

`if can_harvest():
	#do something`

Bu fonksiyonu bu şekilde koşul olarak kullanabilmenizin nedeni, boolean bir değer döndürmesidir.

Bir dönüş değeri, işlev çalıştıktan sonra fonksiyon çağrısı ifadesinin dönen değere eşitlenmesi demektir.

Yukarıdaki kod çalıştığında olanlar:
	-if (koşul) çalışır
	-`can_harvest()` çağrılır
	-`can_harvest()` görevini yapar
	-`can_harvest()` `True` ya da `False` döndürür
	-ifade artık `if True:` ya da `if False:` olur
	-kod bloğu yalnızca hasat edilebiliyorsa çalışır

Artık `if` kullanarak drone'un çok erken hasat etmesini engelleyebiliriz.
