
# 📊 Multidimensional Data Visualization Dashboard

Interaktywna aplikacja webowa oparta na Dash, Plotly oraz Eel, umożliwiająca wizualizację wielowymiarowych danych za pomocą wykresów równoległych. Projekt został zorganizowany zgodnie z architekturą MVC (Model-View-Controller).

## 🚀 Funkcjonalności

- Przesyłanie plików danych w formatach: CSV, XLS, TSV, TXT
- Dynamiczna wizualizacja danych przy użyciu:
  - Parallel Coordinates
  - Parallel Categories
- Interaktywny widok tabelaryczny danych
- Przeglądarkowy interfejs użytkownika
- Integracja z JavaScript przez Eel (np. do zamykania serwera)

## 🛠 Technologie

- Python
- Dash
- Plotly
- Pandas
- Eel
- HTML/CSS/JS (frontend przez Dash)

## 🧩 Architektura

Projekt oparty jest o model MVC:

- Model: przetwarza dane i zawiera logikę aplikacji (model.py, data.py, resourceController.py)
- View: odpowiada za interfejs użytkownika (view.py)
- Controller: zarządza przepływem między modelem a widokiem (controller.py, main.py)

## 📂 Struktura folderów

    IMP/
    ├── controller.py
    ├── view.py
    ├── model.py
    ├── data.py
    ├── dashApp.py
    ├── resourceController.py
    ├── main.py
    └── web/
        └── main.html

## ▶️ Uruchomienie

1. Zainstaluj wymagane biblioteki:

pip install dash pandas plotly eel openpyxl

2. Uruchom aplikację:

python main.py

3. Otwórz przeglądarkę – aplikacja uruchomi się automatycznie (dzięki Eel) i będzie dostępna pod adresem http://localhost.

## ⚠️ Uwaga

- Serwer automatycznie wyłącza się przy zamykaniu przeglądarki dzięki osadzonej funkcji JavaScript (/shutdown).
- W przypadku błędów parsowania pliku, użytkownik otrzyma informację w interfejsie.


## 📄 Licencja

Projekt udostępniany na licencji MIT.
