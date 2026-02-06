# Yedekleri Yükleme
Bazen kayıt dosyası bozulabilir ya da bazı kod dosyalarını kaybedebilirsiniz. Böyle bir durumda bir yedek yüklemeyi deneyebilirsiniz. Bu durum sık oluyorsa Steam Cloud'u kapatmayı deneyin.

Oyun her kaydedildiğinde bir yedek oluşturulur ve gerektiğinde geri döndürebilmeniz için az sayıda yedek saklanır.
Bu yedekler [yedek dizininde](persistent_data_path/Backup) bulunur. Bunlar [kayıt dizinindeki](persistent_data_path/Saves) kayıtların kopyalarıdır.
Bir yedeği yüklemenin en kolay yolu, yüklemek istediğiniz yedeğin klasörünü kayıt dizinine kopyalamaktır.

Bir kayıt, içinde `save.json` dosyası ve bir sürü `.py` dosyası olan bir klasördür.
Eğer yalnızca birkaç kod dosyasını kaybettiyseniz ya da kod dosyaları hâlâ duruyor ama `save.json` dosyası bozulduysa, bozuk kısımları yedekteki karşılık gelen dosyalarla değiştirerek de sorunu çözebilirsiniz.
