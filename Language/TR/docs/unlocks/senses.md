# Duyular
Drone artık görebilir!

`get_pos_x()` ve `get_pos_y()` fonksiyonları drone'un mevcut x ve y konumunu döndürür. Başlangıç konumunda ikisi de `0`'dır. x konumu `East` yönünde her karede `1` artar, y konumu ise `North` yönünde her karede `1` artar.

`num_items(item)` bir öğeden kaç tane olduğunu döndürür.
Örneğin `num_items(Items.Hay)` ne kadar samanınız olduğunu döndürür.

`get_entity_type()` ve `get_ground_type()` drone'un altındaki varlığın ya da zeminin türünü döndürür.

Bir çalının üzerindeyseniz flip yapın:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

`None` anahtar kelimesi de artık açıldı! `None`, bir değer olmadığını temsil eden bir değerdir.
Örneğin, `return` ifadesi olmayan bir fonksiyon aslında `None` döndürür.

Drone'un altında bir varlık yoksa `get_entity_type()` `None` döndürür.

Belirli bir kilit açmadan kaç tane olduğunu öğrenmek için `num_unlocked(unlock)` fonksiyonunu kullanın.

Örneğin, `num_unlocked(Unlocks.Speed)` sahip olduğunuz hız yükseltmesi sayısını döndürür.

`num_unlocked(Unlocks.Senses)` duyular açıldıysa `1`, açılmadıysa `0` döndürür.

`num_unlocked()` fonksiyonunu Items, Entities veya Grounds üzerinde de kullanabilirsiniz. Bu durumda açık ise `1`, değilse `0` döndürür.

Dikkat: `num_unlocked(Unlocks.Carrots)` bu kilidin kaç kez açıldığını/yükseltildiğini döndürür.
`num_unlocked(Items.Carrot)` ise yalnızca `0` ya da `1` döndürür. (Diğer bitkiler için de aynı)
