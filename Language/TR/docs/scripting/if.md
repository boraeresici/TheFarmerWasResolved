# If (Koşul)
Koşullu çalıştırma için if (koşul), elif (aksiysa) ve else (aksi) kullanabilirsiniz.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Söz Dizimi
`if`, bazı koşullar `True` ise kod çalıştırmanızı sağlar. Döngü yapmayan bir `while` gibidir.
`if`, `while` gibi bir koşul alır ve koşul `True` olarak değerlendirilirse if (koşul) bloğunu çalıştırır:

`#koşul True ise flip yap
if condition:
	do_a_flip()`

Koşul `False` olursa çalışacak kodu tanımlamak için `if`'ten sonra `else` de ekleyebilirsiniz.

Koşul `True` ise flip yap, değilse hasat et.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif`, else (aksi) if (koşul)'in kısaltmasıdır.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

Şuna kısaltılabilir:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
