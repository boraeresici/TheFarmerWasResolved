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

Güncel sürümler:
- `main.py` `0.3.0`
- `state.py` `0.3.2`
- `config.py` `0.6.10`
- `economy.py` `0.7.15`
- `pumpkin.py` `0.4.6`
- `actions.py` `0.5.4`
- `grid.py` `0.3.4`

Son güncelleme notu:
- `Sunflowers` unlock sonrası düşük `Items.Power` durumunda sunflower üretim modu devreye girer.
- Uyum için entity adı `Entities.Sunflower` (tekil) olarak kullanılır.
- `Trees` unlock sonrası odun hızlandırma penceresi aktiftir (`TREE_WOOD_HEADROOM`).
- `Timing` unlock sonrası `get_time()` okunur ve erken oyun fazı uygulanır.
- Erken fazda istenirse `Sunflower/Pumpkin` geçici olarak kapatılır (`EARLY_DISABLE_*`).
- `Utilities (random)` unlock sonrası polyculture dağılımı kontrollü rastgeleleşir.
- Sunflower/Pumpkin kararları zaman penceresi (time cycle) ile duty-cycle modunda çalışabilir.
- `Cactus` unlock sonrası ekonomi güvenliyse ve stok düşükse cactus üretim modu devreye girer.

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
