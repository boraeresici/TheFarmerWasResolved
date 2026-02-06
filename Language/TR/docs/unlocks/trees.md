# Ağaçlar
[Ağaçlar](objects/tree), çalılara göre odun elde etmenin daha iyi bir yoludur. Her biri 5 odun verir. Çalılar gibi, çim ya da toprak üzerine ekilebilirler.

Ağaçlar biraz boşluk ister ve yan yana ekilmek büyümelerini yavaşlatır. Büyüme süresi, doğrudan kuzey, doğu, batı veya güneyindeki her ağaç için iki katına çıkar. Yani her kareye ağaç dikerseniz, büyümeleri `2*2*2*2 = 16` kat daha uzun sürer.

<spoiler=show> `%` operatörü burada işinize yarayabilir. `%` operatörünün bölmenin kalanını verdiğini unutmayın. Çift sayılar `2`'ye bölündüğünde kalan `0`, tek sayılar `2`'ye bölündüğünde kalan `1` olur.
Böylece bir sayının çift olup olmadığını şöyle kontrol edebilirsiniz:

`def is_even(n):
	return n % 2 == 0`

Bu, n çiftse `True`, değilse `False` döndürür.
</spoiler>
