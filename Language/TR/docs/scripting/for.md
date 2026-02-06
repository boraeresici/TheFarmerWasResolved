# For Loop (Döngü)
`for` döngüsü Python'daki gibi çalışır. (Bazı dillerde foreach döngüsü denir; C tarzı for döngüsüyle karıştırılmamalıdır, o farklı bir şeydir).

`for i in sequence:
	#do something with i`

`while` loop (döngü)'a benzer şekilde, `for` loop (döngü) da bir kod bloğunu tekrar tekrar çalıştırır. Bir koşula göre dönmek yerine, bir dizideki her eleman için döngü gövdesini bir kez çalıştırır.

## Söz Dizimi
Bir for döngüsü şöyle görünür:

`for variable_name in sequence:
	#code block`

`variable_name` istediğiniz herhangi bir isim olabilir. Bu, dizideki geçerli elemanı tutan bir değişkendir. `sequence`, sayılar aralığı gibi üzerinde dolaşılabilen bir değer olmalıdır. Kod bloğu, döngü değişkeni o elemana atanarak her eleman için çalıştırılır.

## Diziler
[Aralıklar](functions/range)      <unlock=lists>[Lists (Listeler)](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuples (Demetler)](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries (Sözlükler)](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets (Kümeler)](docs/scripting/sets.md)</unlock>

## Örnek
`for i in range(5):
    harvest()`

Bu loop (döngü) gövdeyi sabit sayıda çalıştırır. Temelde şununla aynıdır:

`i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()`

Yani `harvest()` 5 kez çağrılır.

Ayrıca bkz. [Break (Döngüden Çıkış)](docs/scripting/break.md) ve [Continue (Devam)](docs/scripting/continue.md)
