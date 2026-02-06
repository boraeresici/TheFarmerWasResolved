# Genişletme 2
Çiftliğiniz tekrar büyüdü! Artık kareler düzgün bir sıra halinde değil, bu yüzden kare bir ızgarayı dolaşmanın bir yolunu bulmanız gerekiyor.

`while` döngüsüyle bu, duyular ve operatörler açılana kadar mümkün değildir.
`for` döngüsünü tanıtma zamanı.

`for` loop (döngü) ile ilgili her şeyi [For Loop (Döngü)](docs/scripting/for.md) sayfasında okuyabilirsiniz; ancak şimdilik onu yalnızca sabit bir sayıda kodu tekrar etmek için kullanacaksınız.

`#n kez flip yap
for i in range(5):
	do_a_flip()`

`range(n)` `0` ile `n-1` arasında, `n` eleman içeren bir sayı aralığı oluşturur. `for` döngüsü, bu dizideki her eleman için döngü gövdesini bir kez çalıştırır. Bu örnekte `do_a_flip()` `5` kez çağrılır.

`get_world_size()` fonksiyonu da artık kullanılabilir. Çiftliğinizin bir kenarının uzunluğunu döndürür. Böylece bir sonraki genişleme yükseltmesi geldiğinde bozulmayacak kod yazabilirsiniz.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Bu örnek, çiftliğin herhangi bir boyutu için bir sütunu hasat eder.

Drone'u çiftlikte nasıl hareket ettireceğinizi bulmakta takılırsanız aşağıdaki ipucuna bakın.
<spoiler=show hint>Elbette çiftlikte dolaşmanın birkaç yolu vardır.
Aradığımız şey, çiftlik tekrar büyüdüğünde bozulmayacak şekilde sistemli bir dolaşım yöntemidir.
Çiftliğin her yerine sistemli şekilde gitmenin bir yolu, aşağıdaki 2 adımı sonsuza kadar tekrar etmektir:

1.`North` yönünde hareket et, sınırı aşıp başa sarana kadar.
2.`East` yönünde hareket et

`for i in range(get_world_size()):` bu fikri koda dönüştürmek için yardımcı olabilir.
</spoiler>
<spoiler=show possible solution> Temel dolaşım şöyle görünebilir:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#her karede flip yap
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
