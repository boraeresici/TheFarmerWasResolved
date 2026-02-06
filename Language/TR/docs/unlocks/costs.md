# Maliyetler
Her maliyet, öğeleri sayılarla eşleştiren bir dictionary (sözlük) olarak temsil edilebilir.

`get_cost()` fonksiyonu böyle bir dictionary (sözlük) döndürür. Bir bitkinin ya da bir kilit açmanın maliyetini verir.

`get_cost(Entities.Pumpkin)`
`{Items.Carrot:1}` döndürür

Kilit açmalarda, maliyetini almak istediğiniz kilit açma seviyesi için isteğe bağlı ikinci bir argüman verilebilir. Varsayılan olarak mevcut kilit açma seviyesi kullanılır.

`get_cost(Unlocks.Loops, 0)`
`{Items.Hay:5}` döndürür

Zaten en yüksek seviyede olan kilit açmalar için `get_cost()` `None` döndürür.

Şöyle kullanılabilir:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`
