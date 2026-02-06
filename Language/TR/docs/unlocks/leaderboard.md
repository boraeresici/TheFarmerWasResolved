# Lider Tablosu
Buraya kadar geldiyseniz birçok zorluğu aştınız. Peki bunları verimli bir şekilde çözdünüz mü?
En verimli çiftçilik yöntemleri için diğer oyuncularla çeşitli lider tablolarında yarışabilirsiniz.

Bir lider tablosu koşusunu `leaderboard_run(leaderboard, filename, speedup)` çağırarak başlatabilirsiniz.
Bu, başlangıç koşulları sabit olan, `simulate()` benzeri bir [simülasyon](docs/unlocks/simulation.md) başlatır. Her lider tablosu kategorisinin farklı başlangıç ve başarı koşulları vardır.

Simülasyon bittiğinde başarı koşulu `True` ise koşu başarılıdır.

Hedefe ulaşıldığında simülasyon otomatik olarak bitmez. Programın sona erdiğinden emin olmalısınız.
Koşu başarılı olursa süreniz lider tablosuna eklenir.

Varyansı azaltmak için tüm koşuların en az 2 saat sürmesi gerekir (hızlandırabilirsiniz, bu yüzden o kadar uzun sürmez). Bir koşu daha erken tamamlanırsa toplam süre 2 saate ulaşana kadar tekrar edilir. Tüm koşuların ortalaması skorunuz olarak yüklenir.

Aşağıda sizi saman lider tablosuna sokacak örnek bir kurulum var.
![](LeaderboardSetup400)

## En Hızlı Sıfırlama
En Hızlı Sıfırlama en prestijli kategoridir. Tek bir çiftlik parselinden başlayarak oyunu tamamen otomatikleştirin ve lider tablolarını yeniden açın.

Her şeyi açmanız gerekmez; yalnızca `Unlocks.Leaderboard` kilidini mümkün olduğunca hızlı açmaya çalışın.

Bir şeyin açık olup olmadığını kontrol etmek için `num_unlocked(unlock) > 0` kullanabileceğinizi ve gerekli öğeleri otomatik olarak çiftlemek için kilit açmaların maliyetini görmek üzere `get_cost()` kullanabileceğinizi unutmayın.

Fonksiyon Çağrısı:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Eşdeğer Simülasyon:
`unlocks = {}
items = {}
globals = {}
#a negative seed value means a random seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Başarı Koşulu:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirent
Her şey açık şekilde başlayın ve `9863168` altını mümkün olduğunca hızlı çiftleyin. Bu, 32x32 bir labirenti `300` kez yeniden kullanarak kazanacağınız altının tam miktarıdır.

Fonksiyon Çağrısı:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Eşdeğer Simülasyon:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Başarı Koşulu:
`num_items(Items.Gold) >= 9863168`

## Dinozor
Her şey açık şekilde başlayın ve `33488928` kemiği mümkün olduğunca hızlı çiftleyin. Bu, 32x32 bir alanı dinozor kuyruğuyla doldurduğunuzda elde edeceğiniz kemik sayısının tam karşılığıdır.

Fonksiyon Çağrısı:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Eşdeğer Simülasyon:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Başarı Koşulu:
`num_items(Items.Bone) >= 33488928`

## Diğer Kaynak Lider Tabloları
Her bitkinin, o bitkiyi mümkün olduğunca hızlı çiftlemek için kendi lider tablosu vardır. Tüm kilit açmalarla, bitkiyi yetiştirmek için gereken kaynaklarla ve bolca güçle başlarsınız. Amaç, bitkinin ürettiği kaynaktan belirli bir miktarı çiftlemektir.

Her zaman olduğu gibi, hedefe ulaştığınızda programınızın sona erdiğinden emin olmanız gerekir. Hedefe ulaşılmış olsa bile program bitmeden koşu tamamlanmış sayılmaz.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Başarı Koşulu: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Başarı Koşulu: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Başarı Koşulu: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Başarı Koşulu: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Başarı Koşulu: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Başarı Koşulu: `num_items(Items.Hay) >= 2000000000`

## Tek Drone Lider Tabloları
Tek bir drone ile çiftçilik yapmak için de lider tabloları vardır. Yalnızca bir drone ve 8x8 bir çiftliğiniz vardır; belirli miktarda kaynağı mümkün olduğunca hızlı çiftlemeniz gerekir.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Hay) >= 100000000`
