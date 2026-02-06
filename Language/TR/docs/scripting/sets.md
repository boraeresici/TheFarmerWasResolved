# Sets (Kümeler)
Sets (Kümeler), [dictionaries (sözlükler)](docs/scripting/dicts.md) gibidir ama değerleri yoktur. Sadece sırasız bir anahtar set (küme)'idir.

Dictionary (Sözlük) gibi oluşturulur, ancak değerler yoktur.
`set = {North, East, West}`

Boş bir set (küme) oluşturmak için `set()` kullanın. `{}`'nin boş bir dictionary (sözlük) oluşturduğunu unutmayın.

Set (Küme)'e yeni bir eleman eklemek için `set.add(elem)` kullanın.

Bir elemanı set (küme)'ten kaldırmak için `set.remove(elem)` kullanın.

Set (Küme)'in bir eleman içerip içermediğini kontrol etmek için `if elem in set:` kullanın.

Set (Küme)'teki tüm elemanları dolaşmak için `for elem in set:` kullanın.
Büyük set (küme)'lerde `in` operatörü listelerden çok daha hızlıdır.

Dictionary (Sözlük)'lerde olduğu gibi set (küme)'ler de sırasızdır; bu yüzden elemanların hangi sırayla dolaşılacağına dair garanti yoktur.

Ayrıca, set (küme)'lerdeki elemanlar benzersizdir; yani zaten set (küme)'te olan bir elemanı eklemek set (küme)'i değiştirmez.
