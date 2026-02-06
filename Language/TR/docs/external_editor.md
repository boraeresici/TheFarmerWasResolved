# Harici Editör
Oyun içindeki metin editörü bu oyunu oynamak için genellikle yeterlidir, ancak elbette Visual Studio Code gibi daha gelişmiş metin editörleriyle yarışamaz.

Oyun tüm kod dosyalarını `.py` dosyaları olarak kaydeder; bu yüzden onları Python editörleriyle düzenleyebilirsiniz.
Bunun yalnızca bir kolaylık olduğunu unutmayın. Oyun içindeki dil aslında Python değildir, fakat yeterince benzer olduğu için Python IntelliSense oldukça iyi çalışır.
Dosyaları [kayıt klasöründe](persistent_data_path/Saves) bulabilirsiniz.

Her kayıt ayrıca, oyun içi yerleşiklerle eşleşen Python yerleşik tanımlarını içeren bir `__builtins__.py` dosyası barındırır; bu da IntelliSense'i etkinleştirir.
VS Code `__builtins__.py` dosyasını otomatik olarak algılayabilir; ancak bazı editörlerde `from __builtins__ import *` yazmanız gerekebilir.

Yeniden yükleme yapmadan harici değişiklikleri oyunda görmek için "File Watcher" seçeneğini etkinleştirmelisiniz. Harici olarak dosya oluşturur veya silerseniz, bunları görmek için yine de kaydı yeniden yüklemeniz gerekir.

## VS Code Kullanımı
The Farmer Was Replaced ile kullanmak için önerilen kod editörü Visual Studio Code'dur.

Onu [buradan](https://code.visualstudio.com/download) yükleyebilirsiniz.

İndirdikten sonra VS Code'a Python eklentisini kurun.

Bunu yaptıktan sonra, `.py` dosyalarınızın bulunduğu [klasörü](persistent_data_path/Saves) VS Code'da açın. Tüm klasörü açtığınızdan emin olun; yalnızca tek tek dosyaları açarsanız `__builtins__.py` dosyası çalışmaz.

Oyunda "File Watcher" seçeneğinin açık olduğundan emin olun. Artık VS Code'da her kaydettiğinizde değişiklikler otomatik olarak oyunda görünür.

Hepsi bu! Artık kodunuzu profesyonel bir kod editöründe yazabilirsiniz!
