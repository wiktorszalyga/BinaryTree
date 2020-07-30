# BinaryTree

## Wykorzystane narzędzia

Aplikacja internetowa napiasana w pythonie za pośrednictwem framework'u Django. Wykorzystuję baze danych PostgreSQL 11.4. W projekcie użyta została biblioteka plotly służąca do generowania graficznej reprezentacji grafu drzewa binarnego.

## Działanie aplikacji

Strona umożliwia zarządzanie strukturą drzewiastą typu zrównoważone drzewo binarne, w którym gdy jest posortowane to węzły wyższe mają zawsze większą wartość od lewego i prawego dziecka. Węzły określane są dwoma parametrami: nazwą i wartością. Hierarchia organizowana jest na bazie parametru wartości. Dane każdego węzła są unikalne i nie ma możłiwości stworzenia nowego węzła z takimi samymi parametrami.

## Dodawanie węzłów

Dodawanie węzłow polega na stworzeniu nowego elementu w bazie danych, który dołączany jest do istniejącego węzła w taki sposób aby zachowana została zrównoważona konstrukcja drzewa. Przy dodawaniu nie wykonuję się operacja sortowania, więc jeśli element dodany jest większy niż jego rodzic stan drzewa pozostaje nie uporządkowany.

## Usuwanie węzłów

Usuwanie węzłów polega na usunięciu z bazy danych dowolnego węzła i zastąpienie go węzłem z najmniejszym indeksem znajdującego się na samym dole drzewa.

## Sortowanie węzłów

Wykorzystywane jest lekko zmodyfikowane sortowanie drzewiaste dzięki któremu możliwym jest posortowanie całego drzewa w każdym układzie nawet po modyfikacji. Działa on w ten sposób, że zaczyna sortowanie od elementów najniższych porównując je z ich rodzicami i tak rekurencyjnie z każdym jego nowym rodzicem. Modyfikacja polega na tym, że w momencie wymiany węzłów w pętli wywoływana jest następna rekurencja, która ma na celu wykonanie procesu odwrotnego na elemencie zamienionym. Proces bombelkowania wykonywany wówczas jest w dół aby sprawdzić czy może niższe elementy nie są większe od nowo pojawionego się wezła. Gdy skończy się ta weryfikacja z powrotem wykonywane jest sortowanie do góry.

## Edycja węzłów

Umożliwia modyfikacje nazwy i wartości dowolnie wybranego elementu pod tym warunkiem, że nie mogą to być parametry już istniejące w innych węzłach. Tak samo jak w przypadku dodawania i usuwania stan drzewa po takiej opcji jest nie posortowany, więc jeśli chcemy usyskać drzewo zrównoważone i częściowo posortowane należy użyć opcji sortowania. 

# Informacje dodatkowe

tree/models.py - Klasa generująca w bazie danych tablice dotyczącą węzłów
tree/functions.py - Wszystkie funkcje dotyczące operacji na węzłach
tree/forms.py - Formularze odpowiadające za generownie wszystkich inputów dla użytkownika i jednocześnie walidujące dane
tree/view.py - Funkcja renderująca obraz główny strony

Adres strony postawionej przy użyciu platformy Heroku: https://wiktorbinarytree.herokuapp.com

