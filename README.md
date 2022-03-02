# ua_2022
Projekt mapowania okolic przygranicznych dla pomocy humanitarnej, będą tutaj umieszczane wszytkie dane które otrzymamy do integracji z OSM

* Zgodnie z zastosowaną nomenklaturą w pierwszych plikach, które zostały zweryfikowane (np. pliki JSON w katalogu 'Robocze') proszę o dodawanie do nich prefiksu '**zw_**'. Dzięki temu inni wolontariusze będą wiedzieli, których plików nie trzeba analizować.
* Obecnie aktualizacja aptek jest oznaczana w zewnętrznym dokumencie, w kórym znajduje się bieżący status weryfikacji poszczególnych plików geojson. W związku z tym nie ma potrzeby dokonywania zmian nazwy plików w repozytorium Roboczy/apteki. Adres pliku z arkuszem: https://docs.google.com/spreadsheets/d/1M9Q3A6HfmyU3TecackvJ6x8Z0KDtiFTovdpb77gpCrU/

Tagowanie poszczególnych danych (zalecany minimalny zestaw):
* Apteka:
```
amenity=pharmacy
name=nazwa_apteki
```

* Szpital:
```
amenity=hospital
healthcare=hospital
name=nazwa_szpitala
emergency=no / gdy szpital nie posiada oddziału ratunkowego lub
emergency=yes
```

* SOR<br>
węzeł w obszarze budynku szpitala z tagami:
```
emergency=yes
healthcare=emergency_ward
operator=nazwa_szpitala
```
Jeżeli jest możliwe wskazanie wejścia do SOR, to węzeł dodatkowo można otagować:
```
emergency=emergency_ward_entrance
entrance=yes
emergency_ward_entrance=walk-in lub
emergency_ward_entrance=rescue_service
```
jeżeli wejście jest jedno zarówno dla służb ratunkowych jak i dla przychodzących pacjentów, to tag emergency_ward_entrance można pominąć, gdyż domyślna wartość tego tagu to: ```emergency_ward_entrance=all```

* nocna pomoc<br>
dodać do obiektu tag:
```
emergency=yes
```
