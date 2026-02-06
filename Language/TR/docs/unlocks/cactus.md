# Kaktüs
Diğer bitkiler gibi [kaktüsler](objects/cactus) de toprak üzerinde yetiştirilebilir ve normal şekilde hasat edilebilir.

Ancak, farklı boyutlarda olurlar ve garip bir sıralama mantıkları vardır.

Tam büyümüş bir kaktüsü hasat ettiğinizde ve tüm komşu kaktüsler sıralı düzende ise, tüm komşu kaktüsleri de özyinelemeli olarak hasat eder.

Bir kaktüsün sıralı kabul edilmesi için `North` ve `East` yönlerindeki tüm komşu kaktüslerin tam büyümüş olması ve boyutlarının daha büyük ya da eşit olması, `South` ve `West` yönlerindeki tüm komşu kaktüslerin de tam büyümüş olması ve boyutlarının daha küçük ya da eşit olması gerekir.

Hasat yalnızca tüm bitişik kaktüsler tam büyümüş ve sıralı olduğunda yayılır.
Bu, büyümüş kaktüslerden oluşan bir kare boyuta göre sıralıysa ve bir kaktüsü hasat ederseniz, tüm kareyi hasat edeceğiniz anlamına gelir.

Tam büyümüş bir kaktüs sıralı değilse kahverengi görünür. Sıralandığında yeniden yeşile döner.

Hasat edilen kaktüs sayısının karesi kadar kaktüs elde edersiniz. Yani aynı anda `n` kaktüs hasat ederseniz `n**2` adet `Items.Cactus` alırsınız.

Bir kaktüsün boyutu `measure()` ile ölçülebilir.
Her zaman şu sayılardan biridir: `0,1,2,3,4,5,6,7,8,9`.

Ayrıca `measure(direction)` ile drone'un o yöndeki komşu karesini de ölçebilirsiniz.

`swap()` komutunu kullanarak bir kaktüsü herhangi bir yöndeki komşusuyla değiştirebilirsiniz.
`swap(direction)` komutu, drone'un altındaki nesneyi drone'un `direction` yönündeki bir karedeki nesneyle değiştirir.

## Örnekler
Bu ızgaraların her birinde tüm kaktüsler sıralı düzendedir ve hasat tüm tarlaya yayılır:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

Bu ızgarada yalnızca sol alttaki kaktüs sıralı düzendedir; bu da yayılması için yeterli değildir:
`1 5 3
4 9 7
3 3 2`

<spoiler=show hint 1>
Satırlar zaten sıralıysa, sütunları sıralamak satırları bozmaz.
</spoiler>
<spoiler=show hint 2>
Sıralama algoritmalarına aşina değilseniz, internette araştırıp bu probleme hangilerinin uyarlanabileceğini düşünebilirsiniz. Yalnızca komşu kaktüsleri yer değiştirebildiğinizi unutmayın, bu yüzden hepsi işe yaramaz.
</spoiler>
