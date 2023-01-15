from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# labeled_comments = [("Bu harika bir ürün!", "positive"), ("Bu ürünü nefret ediyorum.", "negative"), ("Orta, sanırım.", "neutral")]

labeled_comments = []

with open("yorumlar.txt", "r", encoding="utf-8") as dosya:
    belge_liste = dosya.readlines()
    dosya.close()

for mesaj in belge_liste:
    bolunmus_mesaj = mesaj.split(";;")
    if bolunmus_mesaj[1].split()[0] == "Olumlu":
        labeled_comments.append((bolunmus_mesaj[0], "positive"))
    elif bolunmus_mesaj[1].split()[0] == "Tarafsız":
        labeled_comments.append((bolunmus_mesaj[0], "neutral"))
    else:
        labeled_comments.append((bolunmus_mesaj[0], "negative"))

train_data, test_data = train_test_split(labeled_comments, test_size=0.2)

train_comments = [x[0] for x in train_data]
train_labels = [x[1] for x in train_data]
test_comments = [x[0] for x in test_data]
test_labels = [x[1] for x in test_data]

vectorizer = CountVectorizer()
train_vectors = vectorizer.fit_transform(train_comments)
test_vectors = vectorizer.transform(test_comments)

classifier = MultinomialNB()
classifier.fit(train_vectors, train_labels)

accuracy = classifier.score(train_vectors, train_labels)
print("Accuracy: {:.2f}%".format(accuracy * 100))


# Testing

new_comments = ["Ürün küçük geldi değiştirmek için 1 haftadır uğraşıyorum satıcı çok ilgisiz umursamaz böyle kötü bir firma görmedim esim için aldığım urunu değiştirmek istiyorum cevap veren yok ", "18 Ekim 2022 tarihinde Trendyol üzerinden Smartest  adlı satıcıdan aldığım Akıllı Çocuk Saati ürünü tarafıma ulaştığında sim kartını okumuyor", "GÜZEL HOSTİNG İLE ÇALIŞMAYA BAŞLAYALI KISA BİR SÜRE OLDU FAKAT DESTEK SİSTEMİNDEN ÇOK MEMNUNUM site calisanlarina cok tesekkur ederim urunumu hemen gonderdiler", "bu fiyata bu kalite, hiç kaçırmayın derim", "esi diğer süpürgelere göre çok az. oğlum süpürge sesinden korkuyor diye çok araştırarak almıştık. gerçekten oğlum bunun sesinden kokmuyor. daha sessizi de olmaz herhalde"]
new_vectors = vectorizer.transform(new_comments)
predictions = classifier.predict(new_vectors)
for comment, sentiment in zip(new_comments, predictions):
    print("Comment: {} , Sentiment: {}".format(comment, sentiment))
