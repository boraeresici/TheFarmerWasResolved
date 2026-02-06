# Import (İçe Aktarma)
Tüm kodu tek bir dosyaya koymak hızla yönetilemez hale gelir.
`import` ifadeleri, başka bir dosyadan fonksiyonları ve global değişkenleri içe aktarmanızı sağlar.
Tek bir görselle nasıl çalıştığı:
![](ImportsInOnePicture400)

Burada `import module2`, `module2` adlı dosyayı çalıştırır ve onun tüm global değerlerine erişmenizi sağlar.
Sonra içe aktarılan modülün içindeki değişkenlere ve fonksiyonlara `.` operatörüyle erişebilirsiniz.
Bu örnekte `module2.print_x()`, `module2` içindeki `print_x()` fonksiyonunu çağırır.

### Buradan sonrası şart değil

`from` söz dizimini kullanarak içe aktarılan modülün global değerlerini, import (içe aktarma) ifadesinin çalıştığı mevcut kapsama taşıyabilirsiniz.

`from module2 import print_x
print_x()`
Sadece `module2` içindeki belirtilen global değerleri içe aktarır.

veya

`from module2 import *
print_x()`
`module2` içindeki tüm global değerleri içe aktarır.

Bu da `module2` dosyasını içe aktarır, ancak `module2` adlı bir değişken üzerinden erişmek yerine, `module2`'nin global değerlerini açar ve doğrudan yerel kapsama atar.

Bu import (içe aktarma) biçimi genellikle önerilmez; çünkü iki dosya birbirini içe aktardığında iyi çalışmaz ve isim çakışmaları nedeniyle içe aktaran dosyadaki değişkenleri yanlışlıkla ezebilirsiniz. Ne yaptığınızdan emin değilseniz `from` söz diziminden kaçınmak daha güvenlidir.

# Gerçekte Nasıl Çalışır

## Kısaca
Importlar biraz sezgisel olmayabilir, ancak çoğu sorunu `from file import` yerine `import file` söz dizimini kullanarak ve global tanım olmayan her şeyi
`if __name__ == "__main__":` içine alarak önleyebilirsiniz.

## Import (İçe Aktarma) Yan Etkileri
Bir dosyayı ilk kez içe aktardığınızda, dosyanın tamamını çalıştırır ve çalıştırma sırasında tanımlanan tüm değişkenlere erişmenizi sağlar.
Aynı dosyayı tekrar içe aktarırsanız, ilk seferden önbelleğe alınmış modül döner.

Bu, import (içe aktarma) ifadelerinin yan etkileri olabileceği anlamına gelir. `harvest()` çağıran bir dosyayı içe aktarırsanız, import (içe aktarma) sırasında gerçekten hasat edilir. Ancak tekrar içe aktarırsanız, dosya yalnızca bir kez çalıştırıldığı için tekrar hasat edilmez.

Bu tür yan etkilerden kaçınmanın bir yolu `__name__` değişkenini kullanmaktır. Bu, bir dosya doğrudan çalıştırıldığında otomatik olarak `"__main__"` değerine, bir dosya `import` ile çalıştırıldığında ise dosya adına ayarlanır.
Dosya içe aktarılırken çalışmasını istemediğiniz kodları `if __name__ == "__main__":` bloğuna koymak iyi bir uygulamadır.

Python'da yaygın bir dosya yapısı, dosya çalıştırıldığında çalışacak kodu `main()` fonksiyonuna koymaktır. Böylece yerel değişkenler (`main()` içinde tanımlananlar) ile içe aktarılabilen global değişkenler (dışarıda tanımlananlar) arasında net bir ayrım olur.

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # do things

if __name__ == "__main__":
    main()`

## Import (İçe Aktarma) Döngüleri
`a` dosyası `b` dosyasını ve `b` dosyası da `a` dosyasını içe aktarırsa ne olur?

`a` dosyası:
`import b
x = 0`

`b` dosyası:
`import a
def f():
    print(a.x)`

Bu gayet iyi çalışır. Diyelim ki iki dosyadan hiçbiri daha önce yüklenmemiş ve biri `import a` çalıştırıyor.

-`a`, `import b` satırına kadar çalışır.
-`b`, `import a` satırına kadar çalışır.
-`a` modülü zaten vardır, ama sadece `import b` satırına kadar geldiği için `x` içermez.
-`b`, yarı yüklenmiş `a` modülünün bir referansını `a` adlı değişkende saklar.
-`b` `def` ifadesini çalıştırır ve `f()` fonksiyonunu saklar.
-`a` çalışmaya devam eder ve `x`'i başlatır.

Birisi `b.f()` çağırdığında, `b`'nin referans verdiği `a` modülü artık tamamen yüklendiği için doğru şekilde `0` yazdırır.

Şimdi aynı kodu `from` söz dizimiyle düşünün.

`a` dosyası:
`from b import *
x = 0`

`b` dosyası:
`from a import *
def f():
    print(x)`

-`a`, `from b import *` satırına kadar çalışır.
-`b`, `from a import *` satırına kadar çalışır.
-`a` modülü zaten vardır ama henüz tamamen çalıştırılmamıştır.
-`b`, o anda `a` içinde olan her şeyi kendi global kapsamına açar. Bu noktada `a`, `x = 0` satırına gelmediği için hiçbir şey içermez; dolayısıyla hiçbir şey içe aktarılmaz.
-`b` `def` ifadesini çalıştırır ve `f()` fonksiyonunu saklar.
-`a` çalışmaya devam eder ve `x`'i başlatır.

Eğer biri şimdi `b.f()` çağırırsa, `x` mevcut kapsamda olmadığı için hata alır. Çünkü bu sefer `b`, hâlâ yüklenmekte olan `a`'ya referans tutmaz ve importtan sonra eklenen tanımları göremez.
