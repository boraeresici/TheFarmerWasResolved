# Oyun İçi Unlock Hedef Listesi

Bu liste, otomasyon odaklı ve ekonomi-dengeli ilerleme için önerilen sıradır.  
Öncelik: üretimi kilitlemeden ilerlemek, `Wood >= 3200` tabanını korumak ve expand sonrası hiçbir tile'ı boş bırakmamak.

## Erken Oyun (Temel Otomasyon)

1. `Unlocks.Plant`
2. `Unlocks.Speed` (ilk hız artışı)
3. `Unlocks.Loops` (`while True` için)
4. `Unlocks.Senses` (`num_items`, `get_pos_x/y`, `num_unlocked`)
5. `Unlocks.Expand` (hareket)
6. `Unlocks.Operators` (koşul ve hesap mantığı)
7. `Unlocks.Variables`
8. `Unlocks.Functions`
9. `Unlocks.Expand` (2. seviye / kare grid dönemi)
10. `Unlocks.Carrots`
11. `Unlocks.Trees`
12. `Unlocks.Costs`
13. `Unlocks.Auto_Unlock`

Erken oyun hedefi:
- Grid traversal'ı `get_world_size()` ile tamamen dinamik yapmak.
- Hay/Wood/Carrot üretimini kilitlemeden sürdürülebilir hale getirmek.

## Orta Oyun (Verim ve Büyüme)

1. `Unlocks.Watering`
2. `Unlocks.Pumpkins`
3. `Unlocks.Pumpkins` (upgrade seviyeleri, ekonomi izin verdiğinde)
4. `Unlocks.Fertilizer`
5. `Unlocks.Polyculture`
6. `Unlocks.Sunflowers`
7. `Unlocks.Trees` (upgrade seviyeleri)
8. `Unlocks.Carrots` (upgrade seviyeleri)
9. `Unlocks.Expand` (mevcutsa sonraki seviyeler)

Orta oyun hedefi:
- Pumpkin'ı ana strateji değil, “ekonomi uygunsa aktif” modda kullanmak.
- Water/Fertilizer kullanımını yüksek getirili alanlara odaklamak.
- Wood tabanını düşürmeden carrot maliyet zincirini beslemek.

## Geç Oyun (İleri İçerik ve Skorlama)

1. `Unlocks.Mazes`
2. `Unlocks.Cactus`
3. `Unlocks.Dinosaurs`
4. `Unlocks.Megafarm`
5. `Unlocks.Simulation`
6. `Unlocks.Timing`
7. `Unlocks.Import`
8. `Unlocks.Leaderboard`
9. `Unlocks.Debug` / `Unlocks.Debug_2` (gerekirse test ve teşhis için)

Geç oyun hedefi:
- İleri içerik kaynaklarını (gold/cactus/bone) ayrı pipeline'lara ayırmak.
- Simülasyonla strateji denemek, timing ile darboğaz ölçmek.
- Leaderboard koşullarına göre görev odaklı script akışları yazmak.

## Operasyon Kuralları (Her Fazda Geçerli)

- `Wood >= 3200` hard hedef; bunun altına düşmeyecek ekonomi önceliği korunur.
- Her döngüde tüm tile'lar işlenir (`size * size` garanti traversal).
- Unlock kararları mümkün olduğunca `get_cost()` + mevcut stok ile dinamik verilir.
- Yeni dünya boyutu geldiğinde sabit koordinat/alan varsayımları kullanılmaz.
