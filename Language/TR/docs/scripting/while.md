# While Loop (Döngü)
`while` loop (döngü)'unu ve `True` ile `False` değerlerini açtınız. `while` loop (döngü), koşul `True` olduğu sürece loop (döngü) gövdesini çalıştırmaya devam eder.

`while condition:
	#loop body`

Sonsuz döngü oluşturmaktan endişelenmeyin. Çalıştırmadaki gecikmeler programın donmasını engeller.

## Yeni Başlayanlar İçin
Belki de art arda birkaç `harvest()` çağrısı yapmayı denediniz:

`harvest()
harvest()
harvest()`

Bu, tek bir program çalıştırmasında birkaç kez hasat etmenizi sağlar.
Ancak üç kereden fazla hasat etmek isteriz ve aynı kodu tekrar tekrar yazmak kötü bir pratiktir.
Çözüm loop (döngü)'tur.
Bir loop (döngü), aynı kodu birden fazla kez çalıştırmanıza olanak tanır.

While loop (döngü), `True` veya `False` olmak üzere iki durumdan birinde olabilen mantıksal bir değer olan koşulu alır.
Böyle bir değere boolean (mantıksal) değer denir.

Loop (Döngü), koşul `False` olana kadar içindeki kodu çalıştırır.
While loop (döngü) şöyle görünür:

`while condition:
	#loop body
	#loop body
	#...`

Burada "condition" ifadesini bir boolean değerle ve `#loop body` kısmını da döngüde yapmak istediğiniz şeylerle değiştirmelisiniz.

Kullanılabilir iki sabit boolean değer vardır. Sabitler, program boyunca değişmeyen değerlerdir.

Her zaman `True` olacak sabit bir boolean değer oluşturmak için `True` yazmanız yeterlidir. Her zaman `False` olacak sabit bir boolean değer için `False` yazın.
Yani şu şekilde yazabilirsiniz:

`while False:
	do_a_flip()`

veya

`while True:
	do_a_flip()`

İlki asla flip yapmaz, ikincisi ise sonsuza kadar flip yapar (sonsuz loop (döngü)).

Normalde sonsuz loop (döngü) oluşturmak kötü bir fikirdir çünkü programı dondurur, fakat bu oyunda loop (döngü)'un her yinelemesi arasında gecikmeler vardır, bu yüzden drone siz çalıştırma düğmesine tekrar basarak durdurana kadar flip yapmaya devam eder.

İki noktanın ardından gelen satırın girintili olduğuna dikkat edin. Böyle girintileme, kod bloklarını ayırmak için kullanılır.
Girinti eklemek için Tab'a, kaldırmak için Shift + Tab (veya Backspace) tuşlarına basın.

Loop (Döngü), iki nokta üst üste sonrasında girintili olan tüm ifadeleri tekrarlar.
Girintili bloğun dışındaki ifadeler, loop (döngü) bittikten sonra çalıştırılır.
