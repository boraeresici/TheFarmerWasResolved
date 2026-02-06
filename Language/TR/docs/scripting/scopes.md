# İsim Kapsamları
Kapsamlar, hangi değişkenlere nereden erişilebileceğini belirler. Bir kapsam, temelde isimlerden değerlere bir eşlemedir.
Python'dakiyle aynı şekilde çalışır.

Global bir kapsam vardır ve her fonksiyonun yerel bir kapsamı vardır.
Bir değişken tanımladığınızda, mevcut kapsama eklenir.
Bir fonksiyon tanımının dışındaki her şey global kapsamın parçası kabul edilir.

`x = 1`
Global kapsamda `x` adına `1` değerini atar.

Bu `def` ifadesi, global kapsamda `f` adına bir fonksiyon atar.
`def f():
    # f fonksiyonunun yerel kapsamında y adına 1 değerini atar.
    y = 1

    # f fonksiyonunun yerel kapsamında g adına bir fonksiyon atar.
    def g():
        pass`

`f()`
Global kapsamdaki `f` içinde saklanan fonksiyonu alır ve çağırır.

`print(y)`
Global kapsamdaki bu `print` ifadesi hata verir; çünkü `y` global kapsamda hiç tanımlanmadı, bu yüzden burada okunamaz.
`y` sadece `f`'nin yerel kapsamında vardı.

## global Anahtar Kelimesi
Varsayılan olarak, fonksiyonlardaki tüm değişkenler yerel kapsama bağlanır; global kapsamda aynı isimde bir değişken olsa bile.

`x = 0

def f():
    x = 1
f()
print(x)`

Bu kod `0` yazdırır; çünkü `f` içindeki yerel `x`, global `x` ile aynı değişken değildir, bu yüzden global `x` değişmeden kalır. Bu önemlidir; çünkü aksi halde bir fonksiyon çağrısı, sadece aynı ismi taşıdığı için global bir değişkeni yanlışlıkla ezebilir.

Global bir değişkene yazmak istiyorsanız bunu `global` anahtar kelimesiyle açıkça yapmanız gerekir.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

Bu örnekte `global x`, `x`'i yukarıda tanımlanan global `x` değişkenine bağlar. Bu artık `1` yazdırır.
Global değişkenleri değiştirmek genellikle spagetti koda giden ilk adımdır; programın her parçası diğer her parçayı etkiler. Bu yüzden aşırı kullanmayın.

## Döngüler ve Dallar
Döngüler ve dallar kendi kapsamlarını oluşturmaz; bu yüzden içlerinde tanımlanan şeyler dışarıda da kullanılabilir.

`for i in range(3):
    pass
print(i)`

Bu `2` yazdırır; çünkü `for` döngüsünün son yinelemesi `i` değişkenine `2` atadı.
