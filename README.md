# The Farmer Was Resolved - Türkçe Yama

Bu repo, *The Farmer Was Replaced* oyununun metinlerini Türkçeye çevirmek ve iyileştirmek için hazırlanmıştır. Topluluk katkılarıyla çeviri düzeltmeleri yapılır.

## Klasör Yapısı
- `EN/` orijinal metinler
- `TR/` Türkçe çeviriler
- `Language/TR/` oyun içine kopyalanmaya hazır Türkçe paket
- `files/` oyun içi otomasyon script dosyaları (farm controller modülleri)

## Farm Script Durumu (`files/`)
Bu klasördeki modüller, akıllı farm yönetimi için ayrılmıştır.

- Hard hedef: `Wood >= 3200`
- Kademeli uyum: Expand 0 / Expand 1 / Expand 2+ traversal desteği
- Pumpkin modu: ekonomi uygunken aktif (carrot ve wood tampon kontrolü)
- Geriye dönük uyumluluk: eski `actions.py` çağrılarına karşı alias/fallback desteği

Akış diyagramı:
- `flows/game_flow.mmd` (oyun akış kurgusu, değiştikçe güncellenecek)

Güncel sürümler:
- `main.py` `0.3.0`
- `state.py` `0.3.9`
- `config.py` `0.6.23`
- `economy.py` `0.7.27`
- `locked.py` `0.1.0`
- `pumpkin.py` `0.4.6`
- `actions.py` `0.5.9`
- `grid.py` `0.3.4`

Son güncelleme notu:
- `Locked Module`: hedef unlock sırası (`Dinosaurs -> Mazes -> Megafarm`) için maliyet analizi yapar ve eksik item odaklar.
- `Locked Bonus`: scheduler skorlarına hedefe göre dinamik bonus ekler (`LOCKED_PRIORITY_BONUS`).
- `Locked State`: aktif hedef, odak item ve eksik miktar state içinde tutulur.
- `Priority Scheduler`: base crop kararı artık puanlı mod seçimiyle yapılır (`ENABLE_PRIORITY_SCHEDULER`).
- `Mode Lock`: seçilen mod minimum loop boyunca korunur (`ENABLE_MODE_LOCK`, `MODE_MIN_HOLD_LOOPS`).
- `Loop Snapshot`: aynı loop içinde kaynak okumaları tek snapshot'tan yapılır; tile bazlı karar sapması azalır.
- `Hysteresis`: Hay/Carrot recovery ile Pumpkin/Sunflower/Cactus modlarında giriş-çıkış eşikleri kullanılır.
- `Sunflowers` unlock sonrası düşük `Items.Power` durumunda sunflower üretim modu devreye girer.
- Uyum için entity adı `Entities.Sunflower` (tekil) olarak kullanılır.
- `Trees` unlock sonrası odun hızlandırma penceresi aktiftir (`TREE_WOOD_HEADROOM`).
- `Timing` unlock sonrası `get_time()` okunur ve erken oyun fazı uygulanır.
- Erken fazda istenirse `Sunflower/Pumpkin` geçici olarak kapatılır (`EARLY_DISABLE_*`).
- `Utilities (random)` unlock sonrası polyculture dağılımı kontrollü rastgeleleşir.
- Sunflower/Pumpkin kararları zaman penceresi (time cycle) ile duty-cycle modunda çalışabilir.
- `Cactus` unlock sonrası ekonomi güvenliyse ve stok düşükse cactus üretim modu devreye girer.
- `Dinosaurs` unlock sonrası cactus hedef stoğu otomatik yükselir (`DINOSAUR_CACTUS_BUFFER`).
- `Maze Prep Mode`: `Weird_Substance < 1000` hedefiyle çalışır; prep sırasında Pumpkin/Cactus modları opsiyonel durdurulur ve gübre harcaması config ile yönetilir.
- `Hat Rotation`: Hats unlock sonrası belirli loop aralıklarında (utilities varsa rastgele) şapka değiştirilir.

## Çeviri Kuralları (Özet)
- Kod blokları **çevrilmez**.
- Kodlamaya ait jargonlar İngilizce bırakılır ve **parantez içinde Türkçesi** yazılır. Örnek: `loop (döngü)`, `dictionary (sözlük)`.
- `Items.*`, `Entities.*`, `Grounds.*`, `Unlocks.*`, `Leaderboards.*` gibi isimler **değiştirilmez**.
- `{0}`, `{{...}}` gibi placeholder’lar **asla değiştirilmez**.

## Oyunda Test Etme
Oyunda görmek için `Language/` klasörünü oyun kurulum dizinindeki `Languages` klasörüyle değiştirin.

### Languages Klasörünü Bulma
**Steam (Windows/macOS/Linux):**
1. Steam Library → sağ tık *The Farmer Was Replaced* → **Manage** → **Browse local files**
2. Açılan klasörde `Languages` dizinine girin.

## Katkı
Değişikliklerinizi commit edip PR açabilirsiniz. PR açıklamasına görünmesini istediğiniz ismi ekleyin.

## Not
Orijinal metinler güncellenebilir; güncellenen metinler, topluluk çevirilerinin üzerine yazabilir.
