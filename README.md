# 📊 Multidimensional Data Visualization Dashboard

Interaktywna aplikacja webowa oparta na Dash, Plotly oraz Eel, umożliwiająca wizualizację wielowymiarowych danych za pomocą wykresów równoległych. Projekt został zorganizowany zgodnie z architekturą MVC (Model-View-Controller).

## 🚀 Funkcjonalności

    Przesyłanie plików danych w formatach: CSV, XLS, TSV, TXT

    Dynamiczna wizualizacja danych przy użyciu:

        Parallel Coordinates

        Parallel Categories

    Interaktywny widok tabelaryczny danych

    Przeglądarkowy interfejs użytkownika

    Integracja z JavaScript przez Eel (np. do zamykania serwera)

## 🛠 Technologie

    Python

    Dash

    Plotly

    Pandas

    Eel

    HTML/CSS/JS (frontend przez Dash)

## 🧩 Architektura

Projekt oparty jest o model MVC:

    Model: przetwarza dane i zawiera logikę aplikacji (model.py, data.py, resourceController.py)

    View: odpowiada za interfejs użytkownika (view.py)

    Controller: zarządza przepływem między modelem a widokiem (controller.py, main.py)