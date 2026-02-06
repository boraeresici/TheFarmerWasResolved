# Değişkenler
Değişkenler, bir değeri tutabilen isimli kaplar olarak düşünülebilir.
`=` operatörü, bir değişken tanımlamak ve içine değer koymak için kullanılır.

`variable_name = value`

Operatörün sol tarafı değişken adıdır. İstediğiniz herhangi bir isim verebilirsiniz.
Sağ taraf, sonucu değişkende saklanacak olan bir ifadedir.

`a` adında bir değişken tanımlayın ve içine `5` değerini koyun:
`a = 5`
`b` adında bir değişken tanımlayın ve `can_harvest()` fonksiyonunun dönüş değerini içine koyun:
`b = can_harvest()`

`=` operatörünü `==` operatörüyle karıştırmayın.
`==` operatörü iki değerin eşit olup olmadığını kontrol eder ve `True` ya da `False` döndürür.
`=` operatörü ise sağdaki değeri soldaki isme atar.

Bir değişken atandıktan sonra, içerdiği değeri almak için kod içinde kullanabilirsiniz.

`a = 5
for i in range(a):
	do_a_flip()`

Yukarıdaki döngü 5 kez çalışır; çünkü `a` `5`'e ayarlanmıştır.
`for` döngüsündeki `i` de her yinelemede dizinin geçerli değerine otomatik olarak atanan bir değişkendir. (`i` olmak zorunda değil, geçerli herhangi bir değişken adı verebilirsiniz.)

Değişkenler, aynı şeyi `while` döngüsüyle yapmanıza da izin verir:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Bu, yukarıdaki for döngüsüyle aynı şeyi yapar. Sadece i'yi elle artırırız.
Not: i'yi artırmak için onu kendi değeriyle `1`'in toplamına ayarlarız. Bir değişkenin değerini önceki değerine bağlı olarak değiştirmek çok yaygın bir şeydir.
Şu operatörlerle kısaltılabilir: `+=, -=, *=, /=, %=`

`i = i + 1` ile `i += 1` aynı şeydir
`a = a / 3` ile `a /= 3` aynı şeydir
