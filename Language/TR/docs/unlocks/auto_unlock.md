# Otomatik Kilit Açmalar
Oyunu tamamen otomatikleştirmek için `unlock()` fonksiyonunu kullanarak özellikleri otomatik olarak açabilirsiniz.
Örneğin, hız ve genişleme özelliklerini açmak için `unlock(Unlocks.Speed)` ve `unlock(Unlocks.Expand)` kullanabilirsiniz.

Bir kilit açmanın maliyetini belirlemek için, bir bitki ya da öğe için yaptığınız gibi `get_cost()` fonksiyonunu kullanın.
Örnek:
`get_cost(Unlocks.Loops)`
`{Items.Hay:5}` döndürür.
