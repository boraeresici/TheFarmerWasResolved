# Fonksiyonlar
Yeni bir fonksiyon tanımlamak için `def` anahtar kelimesini kullanın:
`def f(arg1, arg2 = False):
	#function code`

Fonksiyonu çağırmak için `()` çağrı operatörünü kullanabilirsiniz:
`f(42)`

Fonksiyonlardaki yerel ve global değişkenleri öğrenmek için [Scopes (Kapsamlar)](docs/scripting/scopes.md) sayfasına da bakın.

## Giriş
`harvest()` gibi yerleşik fonksiyonları zaten gördünüz.
Kendi fonksiyonlarınızı da tanımlayabilirsiniz; bu, kodunuzu modüler bir şekilde düzenlemenizi sağlar. Temelde, bir kod bloğuna bir isim verip istediğiniz yerden çağırmanıza olanak tanır.

## Fonksiyon Tanımları
Örneğin, drone'u birden fazla kez hareket ettiren bir fonksiyon tanımlayabilirsiniz.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

`def` anahtar kelimesi bunun bir fonksiyon tanımı olduğunu belirtir.
`move_n_dir` fonksiyonun adıdır. Bu, geçerli herhangi bir değişken adı olabilir ve fonksiyonu çağırmak için kullanılır.
`n` ve `dir` parametrelerdir. Bunlar, fonksiyona verilen değerleri tutan değişkenlerdir (bu değerlere argüman da denir). İstediğiniz kadar parametre ekleyebilirsiniz.
`:` sonrası, fonksiyon çağrıldığında çalışacak kod bloğu gelir.

Yukarıdaki tanımla aşağıdaki kod, drone'u `10` kare `North` ve `2` kare `West` yönünde hareket ettirir.

`move_n_dir(10, North)
move_n_dir(2, West)`

`def function():` gördüğünüzde bunu aslında şu tür bir değişken ataması gibi düşünmelisiniz:
`function = create_new_function_object()`
Tüm atamalarda olduğu gibi, değişken atanmadan kullanılamaz!
`def` ifadesi, fonksiyon çağrılarından önce çalışmalıdır.
Bu kod hata verir:

`func()
def func():
	pass`

## Dönüş Değerleri
Bir fonksiyonun değer döndürmesi için `return` anahtar kelimesini kullanın.
Örneğin, aşağıdaki fonksiyon "exclusive or" işlemini tanımlar. Exclusive or, bir değer `True` ve diğeri `False` ise `True` döndürür:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

Birden fazla değer döndürmek için [Tuples (Demetler)](docs/scripting/tuples.md) kullanılabilir.

## Varsayılan Argümanlar
Argüman verilmezse kullanılacak varsayılan değerler de atayabilirsiniz.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Varsayılan değeri olan bir argümandan sonra, varsayılan değeri olmayan bir argüman gelemez.

## İleri Fonksiyon Kullanımı
Fonksiyonlar, diğer tüm değerler gibi birer değerdir ve `def` ifadesi, fonksiyonu verdiğiniz isme atayan bir atama ifadesi gibi davranır.
Bu, şöyle şeyler yapmanıza imkan tanır:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Burada `f()` fonksiyonu, `d` adında yeni bir fonksiyon tanımlar ve döndürür. İkinci `()` dönen fonksiyonu çalıştırır ve flip yapar.
(Bu tür şeyler genelde iyi bir fikir değildir; çünkü olup biteni görmek zordur)

Başka fonksiyonları argüman olarak alan fonksiyonlar gerçekten yaratıcı şeyler yapmanızı sağlar:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Bu kod drone'u 10 kez `North` yönüne hareket ettirir ve ardından 10 kez gübre kullanır.
