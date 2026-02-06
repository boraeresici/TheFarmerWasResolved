# Dinozorlar
Dinozorlar, kadim kemikler elde edebileceğiniz eski ve görkemli yaratıklardır.

Ne yazık ki dinozorlar çok uzun zaman önce yok oldular, bu yüzden yapabileceğimiz en iyi şey dinozor gibi giyinmektir.
Bu amaçla size yeni bir dinozor şapkası verildi.

Şapka şu şekilde takılabilir:
`change_hat(Hats.Dinosaur_Hat)`

Ne yazık ki reklamda göründüğü gibi değil...

Dinozor şapkasını takar ve yeterli kaktüsünüz olursa, otomatik olarak bir [elma](objects/apple) satın alınır ve drone'un altına yerleştirilir.
Drone bir elmanın üzerindeyken tekrar hareket ederse elmayı yer ve kuyruğunu bir birim uzatır. Yetecek kadar paranız varsa yeni bir elma satın alınır ve rastgele bir konuma yerleştirilir.
Elma, istediği yerde başka bir şey ekiliyse doğamaz.

Dinozorun kuyruğu drone'un arkasından sürüklenir ve drone'un geçtiği önceki kareleri doldurur. Bir drone kuyruğun üstüne hareket etmeye çalışırsa `move()` başarısız olur ve `False` döndürür.
Kuyruğun son parçası hareket sırasında yerinden çıkar, bu yüzden onun üstüne hareket edebilirsiniz. Ancak yılan tüm çiftliği doldurursa artık hareket edemezsiniz. Yani artık hareket edemiyorsanız yılanın tamamen büyüdüğünü anlayabilirsiniz.
Dinozor şapkası takılıyken drone, çiftlik sınırının dışına çıkıp karşı tarafa geçemez.

Bir elma üzerinde `measure()` kullanmak, bir sonraki elmanın konumunu bir tuple (demet) olarak döndürür.

`next_x, next_y = measure()`

Şapka başka bir şapka takılarak çıkarıldığında kuyruk hasat edilir.
Kuyruk uzunluğunun karesi kadar kemik alırsınız. Yani uzunluğu `n` olan bir kuyruk için `n**2` adet `Items.Bone` elde edersiniz.
Örnek:
uzunluk 1 => 1 kemik
uzunluk 2 => 4 kemik
uzunluk 3 => 9 kemik
uzunluk 4 => 16 kemik
uzunluk 16 => 256 kemik
uzunluk 100 => 10000 kemik

Dinozor Şapkası çok ağırdır, bu yüzden onu takarsanız `move()` 200 yerine 400 tik sürer. Ancak her elma topladığınızda, daha uzun bir kuyruğun hareketi kolaylaştırması nedeniyle `move()` tarafından kullanılan tik sayısı %3 (aşağı yuvarlanarak) azalır.

Aşağıdaki döngü, herhangi bir sayıda elma toplandıktan sonra `move()` için kullanılan tik sayısını yazdırır:

`ticks = 400
for i in range(100):
    print("ticks after ", i, " apples: ", ticks)
    ticks -= ticks * 0.03 // 1`

Sadece bir dinozor şapkanız var, bu yüzden yalnızca bir drone takabilir.

<spoiler=show hint 1>Aynı yolu tüm tarlayı kaplayacak şekilde sürekli takip ederseniz, her seferinde tüm tarlayı kaplayan bir yılan elde etmek kolaydır. Çok verimli değil ama işe yarar.
Çok büyük bir çiftliği tamamen dolaşmak uzun sürebilir ve aslında o kadar çok kemiğe ihtiyacınız olmayabilir. Çiftlik boyutunu daha uygun bir şeye değiştirmek için `set_world_size()` kullanabilirsiniz.</spoiler>
