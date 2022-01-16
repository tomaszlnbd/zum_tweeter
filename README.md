# zum_tweeter

Dane zostały pozyskane zgodnie z wytycznymi przy użyciu pliku z id tweetów dla języka polskiego.
Wykorzystane zostało API Twittera w wersji v2 (z powodu ograniczeń dla stworzonego konta musieliśmy użyć nieco innej metody niż na zajęciach oraz klasy Client https://docs.tweepy.org/en/stable/client.html, a także użyć Tweepy w wersji 4.4.0 z powodu problemów z kompatybilnością z nową wersją API).
Dzięki temu mogliśmy też wykorzystać parametr wait_on_rate_limit przy pobieraniu tweedów - co pozwoliło automatycznie czekać na odnowienie się 15 minutowego limitu zapytań. 

Zmaksymalizowaliśmy też ilość pobieranych danych przekazując do metody get_tweets https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets paczki po 100 id, przez co całość pobierania zajęła około 5 godzin. 
Z powodu wcześniej prowadzonych testów pobierania i kilku nieudanych prób, ostatecznie udało się pobrać około 400 000 tweetów. Po wyczyszczeniu danych z tweetów które już nie istnieją/są prywatne/lub z powodu innych błędów które zwracało api, uzyskaliśmy 307692 tweety. 

Preprocessing danych - oprócz standardowych zabiegów odszumiających dane, wykonaliśmy również takie zabiegi jak pozbycie się emotikon usunięcie słów kluczowych (które zaburzały klastrowanie) np. Koronawirus albo Wuhan czy usunięcie wyrażeń typowych dla tweetera np. Nazw użytkowników.

Następnie przeprowadziliśmy lematyzację oraz tokenizację danych oraz zamieniliśmy je na wektory.

Kmeans - zgodnie z wymaganiami projektu podzieliliśmy dane na 3 klasy. Wyniki poddaliśmy ponownej wektoryzacji.

Modele - wytrenowaliśmy 3 modele: svm, logistic regression oraz random forest. Oraz przedstawiliśmy wyniki, które prezentują się dosyć dobrze. Przyczyną może być wykorzystanie tych samych wektorów do podziału na klasy oraz do trenowania i testowania modelu.
