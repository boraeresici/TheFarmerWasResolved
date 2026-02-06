# Listeler
Listeler, birden fazla değeri tek bir değişkende saklamanın kolay bir yoludur.
Yeni listeleri şöyle oluşturabilirsiniz:

`list = [2, True, Items.Hay]`

Liste artık `2`, `True` ve `Items.Hay` değerlerini içerir.
Bir liste boş da olabilir:

`empty_list = []`

Bir listenin elemanına indeksle erişebilirsiniz. İlk elemanın indeksi `0`, ikinci elemanın `1`, üçüncünün `2`'dir...

bitkiler: havuçlar
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

Bir liste üzerinde `for` döngüsü ile dolaşabilirsiniz. Aşağıdaki örnek, listedeki tüm elemanları toplar.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` artık `18`'dir

Aşağıdaki liste metotları eleman ekleyip çıkarmanızı sağlar:

`list.append(elem)` liste sonuna eleman ekler:

`list = [2, 6, 12]
list.append(7)`
`list` artık `[2, 6, 12, 7]`

`list.remove(elem)` listeden elemanın ilk geçtiği yeri kaldırır:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` artık `[1, 4, 2]`

`list.insert(index, elem)` belirtilen indekse eleman ekler:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` artık `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` belirtilen indeksteki elemanı kaldırır.
İndeks verilmezse son eleman kaldırılır.

`list = [3, 5, 8, 25]
list.pop()`
`list` artık `[3, 5, 8]`
`list.pop(1)`
`list` artık `[3, 8]`

`len()` fonksiyonu listenin uzunluğunu döndürür.
`list = [3, 2, 1]
x = len(list)`
`x` artık `3`

Listeler referans semantiğine sahiptir. Bu, bir listeyi bir değişkene atamanın, listenin bir kopyasını oluşturmak yerine aynı liste nesnesini o değişkene atadığı anlamına gelir.
İki değişken aynı listeye referans veriyorsa, listedeki değişiklikler her ikisinde de görülür.

`a = [1,2]
b = a
b.pop()`
`a` ve `b` artık ikisi de `[1]`
