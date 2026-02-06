# Mega Çiftlik
Bu inanılmaz güçlü kilit açma, birden fazla drone'a erişim sağlar.

Daha önce olduğu gibi, yine de yalnızca bir drone ile başlarsınız. Ek drone'lar önce üretilmelidir ve program bittiğinde kaybolurlar.
Her drone kendi ayrı programını çalıştırır. Yeni drone'lar `spawn_drone(function)` fonksiyonuyla üretilebilir.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

Bu, `spawn_drone(function)` komutunu çalıştıran drone ile aynı konumda yeni bir drone üretir. Yeni drone belirtilen fonksiyonu çalıştırmaya başlar. Bittiğinde otomatik olarak kaybolur.

Drone'lar birbirleriyle çarpışmaz.

Aynı anda var olabilecek maksimum drone sayısını almak için `max_drones()` kullanın.
Çiftlikte zaten bulunan drone sayısını almak için `num_drones()` kullanın.


## Örnek:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

Bu, ilk drone'un yatay hareket ederek daha fazla drone üretmesine neden olur. Üretilen drone'lar da dikey hareket ederek yollarındaki her şeyi hasat eder.

Tüm kullanılabilir drone'lar zaten üretilmişse `spawn_drone()` hiçbir şey yapmaz ve `None` döndürür.

İşte her drone'a farklı bir yön veren başka bir örnek.
`for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)`

## Tüm Drone'lar Eşittir
Özel bir "ana" drone yoktur. Tüm drone'lar başka drone'lar üretebilir ve hepsi drone limitine dahil olur. Tüm drone'lar programları bittiğinde kaybolur. İlk drone programını erken bitirirse, kod vurgularıyla görselleştirilen drone başka bir drone olur. Tüm drone'lar kesme noktalarını tetikleyebilir ve bir drone kesme noktası tetiklediğinde kod vurgulaması o drone'a geçer.

<spoiler=show hint> Oldukça faydalı paralel `for_all` fonksiyonuna göz atın; herhangi bir fonksiyonu alır ve onu çiftlikteki her karede çalıştırır. Bunu yapmak için tüm mevcut drone'ları kullanır.

`def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)`

Özellikle faydalı bir kalıp, bir drone mevcutsa onu üretmek, değilse işi kendiniz yapmaktır.

`if not spawn_drone(task):
	task()`
</spoiler>

## Başka Bir Drone'u Beklemek
Başka bir drone'un bitmesini beklemek için `wait_for(drone)` fonksiyonunu kullanın. Drone'u üretirken `drone` tutamacını alırsınız.
`wait_for(drone)` diğer drone'un çalıştırdığı fonksiyonun dönüş değerini döndürür.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)

drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

Drone üretmek zaman aldığından, her küçük şey için yeni bir drone üretmek iyi bir fikir değildir.

Beklemeden bir drone'un bitip bitmediğini kontrol etmek için `has_finished(drone)` kullanabilirsiniz.

## Paylaşılan Bellek Yok
Her drone'un kendi belleği vardır ve başka bir drone'un global değişkenlerini doğrudan okuyup yazamaz.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

Bu, `0` yazdırır; çünkü yeni drone `x`'in kendi kopyasını artırır ve bu, ilk drone'un `x` değerini etkilemez.

## Yarış Koşulları
Birden fazla drone aynı çiftlik karesiyle aynı anda etkileşebilir. İki drone aynı kareyle aynı tik sırasında etkileşirse, her iki etkileşim de gerçekleşir; fakat sonuçlar etkileşimlerin sırasına göre değişebilir.

Örneğin, `0` ve `1` drone'larının neredeyse tam büyümüş aynı ağacın üzerinde olduğunu düşünün.
Drone `0` şunu çağırır:
`use_item(Items.Fertilizer)`
Drone `1` şunu çağırır:
`harvest()`

Bu eylemler aynı anda gerçekleşirse, ağaç önce gübrelenir sonra hasat edilir. Bu durumda odun alırsınız. Ancak Drone `1` biraz daha hızlıysa, ağaç gübrelenmeden önce hasat edilir ve odun alamazsınız.
Buna "yarış koşulu" denir. Paralel programlamada yaygın bir sorundur; sonuç, işlemlerin hangi sırayla gerçekleştiğine bağlıdır.

Birden fazla drone aynı konumda aynı kodu eş zamanlı çalıştırdığında oluşabilecek başka sorunlu bir durum:
`if get_water() < 0.5:
    use_item(Items.Water)`

Birden fazla drone bunu aynı anda çalıştırırsa, hepsi ilk satırı çalıştırıp `if` bloğuna girer. Sonra hepsi su kullanır ve büyük kısmı boşa gider.
Bir drone ikinci satıra geldiğinde, bu arada başka bir drone kareyi sulamış olabileceği için `get_water()` artık `0.5`'ten küçük olmayabilir.
