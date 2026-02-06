# Break (Döngüden Çıkış)
`break`, bir döngüyü erken durdurmayı sağlar. `break` ifadesine gelindiğinde en içteki döngüden hemen çıkılır ve döngüden sonraki kod çalıştırılmaya başlanır.

`for i in range(10):
	break
print(i)`
Bu, `0` yazdırır; çünkü döngünün ilk yinelemesinde `i` `0` değerindedir ve `break` ifadesi döngüyü bitirir.

`while` döngülerinde de çalışır.

`while True:
	if can_harvest():
		break`

Bu kod, `can_harvest()` `True` olana kadar `while` döngüsünü çalıştırır.
Aşağıdakinin aynısıdır:

`while not can_harvest():
	pass`

İç içe döngülerde `break` her zaman en içteki döngüden çıkar.

`for i in range(10):
	for j in range(10):
		break
		print("bu asla yazdırılmaz")
	print("bu 10 kez yazdırılır")`
