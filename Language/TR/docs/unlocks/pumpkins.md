# Kabaklar
[Kabaklar](objects/pumpkin), havuçlar gibi sürülmüş toprakta büyür. Ekilmeleri havuç gerektirir.

Bir kare içindeki tüm kabaklar tamamen büyüdüğünde, birlikte büyüyerek dev bir kabağa dönüşürler. Ne yazık ki kabakların tamamen büyüdükten sonra %20 ihtimalle ölmesi vardır; bu yüzden birleşmeleri istiyorsanız ölü olanları yeniden ekmeniz gerekir.

Bir kabak öldüğünde, hasat edildiğinde hiçbir şey düşürmeyecek ölü bir kabak bırakır. Yerine yeni bir bitki ekmek ölü kabağı otomatik olarak kaldırır; yani hasat etmenize gerek yoktur. `can_harvest()` ölü kabaklarda her zaman `False` döndürür.

Dev kabağın verimi, kabağın boyutuna bağlıdır.

1x1 kabak `1*1*1 = 1` kabak verir.
2x2 kabak `4` yerine `2*2*2 = 8` kabak verir.
3x3 kabak `9` yerine `3*3*3 = 27` kabak verir.
4x4 kabak `16` yerine `4*4*4 = 64` kabak verir.
5x5 kabak `25` yerine `5*5*5 = 125` kabak verir.
`n >= 6` için `n`x`n` kabak `n*n*6` kabak verir.

Tam çarpanı almak için en az 6x6 boyutunda kabaklar yetiştirmek iyi bir fikirdir.

Bu, bir karedeki her karoya kabak ekseniz bile, kabaklardan birinin ölüp dev kabağın büyümesini engelleyebileceği anlamına gelir.
