# Operatörler
aritmetik operatörler: `+, -, *, /, //, %, **`
karşılaştırma operatörleri: `==, !=, <=, >=, <, >`
mantıksal operatörler: `not, and, or`

Not: Oyundaki tüm sayılar kayan nokta sayılardır. Bu yüzden tüm aritmetik operatörler kayan nokta operatörleridir.
`//` bölmeden sonra sayıyı aşağı yuvarlayacak şekilde tanımlanmıştır.

Atama operatörleri için "Variables (Değişkenler)" kilidini açmanız gerekir.

## Giriş
Operatörler değerleri karşılaştırmanıza, değiştirmenize ve birleştirmenize olanak tanır.
Aritmetik operatörler `+, -, *, /, //, %, **` sayılar üzerinde yaygın matematiksel işlemler yapmak için kullanılır.
Karşılaştırma operatörleri `==, !=, <=, >=, <, >` değerleri karşılaştırmak için kullanılır. Sonuç her zaman `True` veya `False` olur.
Mantıksal operatörler (boolean operatörler de denir) `not, and, or` doğruluk değerlerini birleştirmek için kullanılır.

## Aritmetik Operatörler
`+` ve `-` toplama ve çıkarma için kullanılır.

`2 + 3` ifadesi `5` olur
`3 - 2` ifadesi `1` olur

`*`, `/` ve `//` çarpma ve bölme için kullanılır.

`2 * 3` ifadesi `6` olur
`5 / 2` ifadesi `2.5` olur

`//`, `/` ile aynı işlemi yapar ama sonuç aşağı yuvarlanır (bir alt tam sayıya yuvarlanır).

`5 // 2` ifadesi `2` olur

`%` mod operatörüdür; kalan operatörü olarak da bilinir. İki sayıyı böler ve kalanı döndürür. Ayrıca, sağdaki sayı soldan kalan sağdan küçük olana kadar tekrar tekrar çıkarılıyormuş gibi düşünebilirsiniz.

`4 % 2` ifadesi `0` olur
`5 % 2` ifadesi `1` olur
`6 % 2` ifadesi `0` olur
`2 % 6` ifadesi `2` olur
`1.5 % 1` ifadesi `0.5` olur

`**` üs alma operatörüdür.

`2**2` ifadesi `4` olur
`(-5)**3` ifadesi `-125` olur

## Karşılaştırma Operatörleri
`==` ve `!=` iki değerin "eşit"(`==`) ya da "eşit değil"(`!=`) olup olmadığını kontrol etmek için kullanılır. Tüm değer türlerinde kullanılabilir.

`2 == 2` ifadesi `True` olur
`Entities.Bush != Entities.Bush` ifadesi `False` olur
`3 != 3 + 1` ifadesi `True` olur

`<=, >=, <, >` yalnızca sayılar üzerinde kullanılabilir. Soldaki sayının sağdaki sayıdan "küçük veya eşit"(`<=`), "büyük veya eşit"(`>=`), "küçük" (`<`) ya da "büyük" (`>`) olup olmadığını kontrol eder.

`1 <= 1` ifadesi `True` olur
`2 >= 3` ifadesi `False` olur
`-2 < -1` ifadesi `True` olur
`6 > 6` ifadesi `False` olur

## Mantıksal Operatörler
`not` değeri tersine çevirir:

`not False` ifadesi `True` olur
`not True` ifadesi `False` olur

`and`, yalnızca her iki değer de `True` ise `True` olur

`True and True` ifadesi `True` olur
`True and False` ifadesi `False` olur
`False and False` ifadesi `False` olur

`or`, değerlerden en az biri `True` ise `True` olur

`True or True` ifadesi `True` olur
`True or False` ifadesi `True` olur
`False or False` ifadesi `False` olur
