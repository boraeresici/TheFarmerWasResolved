# Tuples (Demetler)
Tuples (Demetler), birden fazla değeri tek bir değerde birleştirmenin harika bir yoludur.
Bir tuple (demet) oluşturmak için değerleri virgülle ayırmanız yeterlidir:

`tuple = 1, 2`

Onları tekrar birkaç değişkene açabilirsiniz. Aşağıdaki kodda, `(1,2)` tuple (demet)'ı iki değişkene, `a` ve `b`'ye açılır.

`a, b = 1, 2`

Tuples (Demetler) listeler gibi indekslenebilir, ancak değiştirilemezler ve oluşturulduktan sonra değiştirilemezler.

`tuple = 1, 2`

`print(tuple[1])`
`2` yazdırır

`tuple[0] = 3`
hata verir
<unlock=dicts>
Listelerin aksine, tuples (demetler) dictionary (sözlük)'lerde anahtar olarak kullanılabilir.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`(4,5)` yazdırır</unlock>

Fonksiyonlardan birden fazla değer döndürmek için de kullanışlıdır.

`def f():
    return 1, 2

a, b = f()`
