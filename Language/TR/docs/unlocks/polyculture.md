# Polikültür
Muhtemelen bitkilerin bazen birlikte ekildiğinde daha fazla verim verdiğini fark etmişsinizdir.
Çim, çalı, ağaç ve havuç, doğru bitki eşlikçisi olduğunda daha fazla verim verir. Eşlikçi tercihi her bitki için farklıdır ve önceden tahmin edilemez. Neyse ki drone'un altındaki bitkinin eşlikçi tercihi `get_companion()` ile ölçülebilir. Bu fonksiyon, ilk elemanı istediği eşlikçi bitki türü, ikinci elemanı da istediği konum olan bir tuple (demet) döndürür.

`plant_type, (x, y) = get_companion()`

Örneğin bir çalı eker ve sonra `get_companion()` çağırırsanız `(Entities.Carrot, (3, 5))` gibi bir değer döndürebilir. Bu, bu çalının `(3,5)` konumunda havuç istemesi demektir. `(3,5)` konumuna havuç eker ve sonra çalıyı hasat ederseniz daha fazla odun verir. Havuç büyüme aşaması önemli değildir.

Bir bitkinin eşlikçi tercihi `Entities.Grass`, `Entities.Bush`, `Entities.Tree` ya da `Entities.Carrot` olabilir. Her bitki bunu rastgele seçer, ancak asla kendisiyle aynı bitkiyi seçmez. Konum da bitkinin kendi konumu hariç, bitkiden 3 hamle uzaklıktaki herhangi bir konum olabilir.

Drone'un altında eşlikçi tercihi olan bir bitki yoksa `get_companion()` `None` döndürür.

Polikültür açılmadan önce verim çarpanı `5`'tir. Her yükseltmede iki katına çıkar.
