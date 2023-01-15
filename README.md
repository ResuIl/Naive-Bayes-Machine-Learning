# Sentiment Analizi İçin Python

Bu kod, "olumlu", "tarafsız" ve "olumsuz" olarak etiketlenmiş yorumları içeren "yorumlar.txt" dosyasını okur. Dosyadaki her yorum ve etiket, "labeled_comments" listesine eklenir. Daha sonra, bu liste eğitim ve test verisi olarak ayırılır. Eğitim verisi, sınıflandırıcıyı eğitmek için kullanılırken, test verisi sınıflandırıcının performansını değerlendirmek için kullanılır.

Sonra, CountVectorizer sınıfı kullanılır ve yorumlar metin verileri sayısal özellik vektörlerine dönüştürülür. Bu vektörler, sınıflandırıcı için girdi olarak kullanılır. Sınıflandırıcı, MultinomialNB sınıfı kullanılarak eğitilir ve performansı accuracy değeri ile ölçülür.

En sonunda, yeni yorumlar için tahminler yapılır ve yorumlar ve tahmin edilen duygu (olumlu, tarafsız veya olumsuz) ekrana yazdırılır.

Eğitilip yorumları okudukta sonra çıkan çıktı.

![alt text](https://cdn.discordapp.com/attachments/1063876459766226965/1064178390283858020/image.png)
