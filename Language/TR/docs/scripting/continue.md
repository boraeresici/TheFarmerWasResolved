# Continue (Devam)
continue (devam), bir döngünün mevcut yinelemesini durdurup en içteki döngünün bir sonraki yinelemesine geçmeyi sağlar.

`for i in range(10):
	continue
    print("bu asla yazdırılmaz")`

Bu, döngünün `10` yinelemesinin tamamını çalıştırır; ancak `continue` sonrası gelen `print` ifadesi her zaman atlanır.

`while` döngülerinde de çalışır.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Bu kod, `harvest()` fonksiyonunu yalnızca `can_harvest()` `True` olduğunda çağırır.
Aşağıdakinin aynısıdır:

`while True:
	if can_harvest():
		harvest()`

İç içe döngülerde `continue` her zaman en içteki döngüyü etkiler.

`for i in range(10):
	for j in range(10):
	    print("bu 100 kez yazdırılır")
		continue
		print("bu asla yazdırılmaz")
	print("bu 10 kez yazdırılır")`
