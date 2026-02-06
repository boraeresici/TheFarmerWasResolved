# Dictionaries (Sözlükler)
Dictionaries (Sözlükler), anahtarları değerlere eşleştirmenizi sağlayan bir veri yapısıdır. Gerçek bir dictionary (sözlük)'nin kelimeleri tanımlarıyla eşleştirmesi gibi çalışır ve çok hızlı arama yapmanızı sağlar.

Bir dictionary (sözlük) şöyle oluşturulabilir:
`right_of = {North:East, East:South, South:West, West:North}`

İki noktanın önündeki ifade anahtardır, iki noktanın arkasındaki ifade ise anahtarın eşlendiği değerdir.
Yukarıdaki dictionary (sözlük), her yönü sağındaki yöne eşler.

İşte drone'un konumunu üzerindeki varlığa eşleyen başka bir örnek.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Bir anahtarın değerine erişmek, listeden elemana erişmeye benzer:
`value = dict[key]`

Örnek:
`orientation = right_of[South]`
Bu, `orientation` değişkenini `West` yapar.

Bir dictionary (sözlük)'ye yeni bir anahtar-değer çifti şöyle eklenir:
`dict[key] = value`

Örnek:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Bu, mevcut konum için saklanan varlığı günceller.

Anahtarlar benzersizdir; dictionary (sözlük)'de zaten olan bir anahtarı eklemek önceki değeri overwrite eder.

Bir anahtar-değer çiftini kaldırmak için `dict.pop(key)` kullanın.

`key in dict` ifadesi, `key` anahtarı `dict` içinde ise `True`, değilse `False` döndürür.
Bu nedenle `if key in dict:` ile `dict` içinde anahtar olup olmadığını kontrol edebilirsiniz.

Bir dictionary (sözlük)'yi `for` döngüsünde kullanmak, tüm anahtarlar üzerinde dolaşmanızı sağlar:
`for key in dict:
	value = dict[key]`

Anahtarların hangi sırayla dolaşılacağına dair garanti yoktur.

Ayrıca bkz. [Sets (Kümeler)](docs/scripting/sets.md)
