# Genişletme 1
<unlock=for>Ayrıca bkz. [Genişletme_2](docs/unlocks/expand_2.md)

</unlock>Çiftliğiniz büyüdü! Drone'u hareket ettiremezseniz bu alanın pek faydası olmaz; bu nedenle drone'u hareket ettiren yeni bir `move()` fonksiyonu var. `move()` fonksiyonu, drone'u hangi yönde hareket ettirmek istediğinizi belirtmenizi ister. Bunun için dört yeni sabit vardır: `North, East, South, West`

Örneğin, `move(North)` drone'u bir kare kuzeye taşır.

Çiftliğin kenarından geçerseniz drone çiftliğin diğer tarafına taşınır.
Aşağıdaki örnek kod, drone'u sürekli kuzeye hareket ettirir ve çiftliğin kenarına ulaştığında başlangıca sarar:

`while True:
	move(North)`
