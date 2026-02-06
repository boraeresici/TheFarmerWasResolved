# Labirentler
[Bitkileri gübrelediğinizde](docs/unlocks/fertilizer.md) elde edilen `Items.Weird_Substance`, çalılarda garip bir etkiye sahiptir. Drone bir çalının üzerindeyken `use_item(Items.Weird_Substance, amount)` çağırırsanız çalı bir çit labirentine dönüşür.
Labirentin boyutu, kullanılan `Items.Weird_Substance` miktarına bağlıdır (`use_item()` çağrısındaki ikinci argüman).
Labirent yükseltmeleri olmadan, `n` adet `Items.Weird_Substance` kullanmak `n`x`n` boyutunda bir labirent oluşturur. Her labirent yükseltme seviyesi hazineyi iki katına çıkarır, ancak gereken `Items.Weird_Substance` miktarını da iki katına çıkarır.
Yani tam alanlık bir labirent yapmak için:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`


Nedense drone, çitler çok yüksek görünmese de üzerlerinden uçamaz.

Çitin içinde bir yerde gizli bir hazine vardır. Hazine üzerinde `harvest()` kullanarak labirentin alanı kadar altın alırsınız. (Örneğin, 5x5 bir labirent 25 altın verir.)

Başka herhangi bir yerde `harvest()` kullanırsanız labirent kaybolur.

Drone hazine üzerindeyse `get_entity_type()` değeri `Entities.Treasure` olur, labirentin diğer her yerinde ise `Entities.Hedge` olur.

Labirentler, yeniden kullanmadığınız sürece döngü içermez (labirenti nasıl yeniden kullanacağınızı aşağıda görebilirsiniz). Bu yüzden geri dönmeden drone'un tekrar aynı konuma gelmesi mümkün değildir.

Bir duvar olup olmadığını içinden geçmeye çalışarak kontrol edebilirsiniz.
`move()` başarılıysa `True`, değilse `False` döndürür.

`can_move()` hareket etmeden duvar olup olmadığını kontrol etmek için kullanılabilir.

Hazineye nasıl ulaşacağınızı hiç bilmiyorsanız, 1. ipucuna bakın. Bu, böyle bir probleme nasıl yaklaşacağınızı gösterir.

Labirentin herhangi bir yerinde `measure()` kullanmak hazine konumunu döndürür.
`x, y = measure()`

Ek bir meydan okuma olarak, hazine üzerinde aynı miktarda `Items.Weird_Substance` kullanarak labirenti yeniden kullanabilirsiniz.
Bu, hazineyi toplar ve labirentin içinde rastgele bir konumda yeni bir hazine oluşturur.

Hazine her taşındığında labirentin bazı duvarları rastgele kaldırılabilir. Böylece yeniden kullanılan labirentler döngüler içerebilir.

Labirentteki döngülerin işi çok zorlaştırdığını unutmayın; çünkü geri dönmeden aynı konuma yeniden gelebilirsiniz.
Bir labirenti yeniden kullanmak, hasat edip yeni bir labirent oluşturmaktan daha fazla altın vermez.
Bu, tamamen ekstra bir meydan okumadır ve isterseniz atlayabilirsiniz.
Yalnızca ek bilgi ve kısayollar labirenti daha hızlı çözmenize yardımcı oluyorsa değer.

Hazine en fazla 300 kez taşınabilir. Bundan sonra, hazine üzerinde weird substance kullanmak artık içindeki altını artırmaz ve hazine de yer değiştirmez.

<spoiler=show hint 1>Problemi çözmek için genel bir yaklaşım:

Bir labirent oluşturun ve kendinizi drone yerine koyun.

Labirentin içinde olsaydınız hazineyi nasıl bulmaya çalışırdınız, bunu düşünün.

Stratejinizi adım adım yazın; başka biri de düşünmeden takip edebilsin.

Şimdi bu adımları koda çevirmeyi deneyin.
</spoiler>
<spoiler=show hint 2>Döngü olmadığı sürece: Tüm duvarlar aslında tek bir büyük bağlı duvardır. Duvarı takip ederseniz sizi tüm labirentten geçirir.
Bu yaklaşım çok az kod gerektirir ve daha önce nerede olduğunuzu takip etmeniz gerekmez. Yaklaşık 10 satır kod yeterlidir.</spoiler>
<spoiler=show hint 3>Drone'u doğrudan doğu ya da batı gibi mutlak yönlerde hareket ettirmek yerine, "sağa dön" veya "sola dön" gibi göreli yönlerde hareket ettirmek çok faydalı olabilir. Bunu yapmak için drone'un şu anda hangi yönde hareket ettiğini takip etmeniz gerekir. Drone gerçekte dönmez, ama kodda "sanal" bir yön tutabilirsiniz.
Aşağıdaki index hilesi buna yardımcı olur:

`directions = [North, East, South, West]
index = 0`

`% 4` kullanarak "çemberin etrafında" dönmesini sağlayabilirsiniz; böylece `West` sonrası tekrar `North` olur.
`# sağa dön
index = (index + 1) % 4`

`# sola dön
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=show hint 4>Çözemiyorsanız her zaman hayatınızı kolaylaştırıp daha verimsiz bir yol seçebilirsiniz.
`1`x`1` bir labirenti çözmek çok kolaydır.</spoiler>
