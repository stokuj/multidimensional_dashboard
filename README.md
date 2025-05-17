
# 📊 Multidimensional Data Visualization Dashboard

Interactive web application based on Dash, Plotly, and Eel, enabling visualization of multidimensional data using parallel plots. The project is organized according to the MVC (Model-View-Controller) architecture.

[Polski](#-multidimensional-data-visualization-dashboard-pl) | [English](#-multidimensional-data-visualization-dashboard)

## 🚀 Features

- Upload data files in formats: CSV, XLS, TSV, TXT
- Dynamic data visualization using:
  - Parallel Coordinates - visualizes numerical data across multiple dimensions
  - Parallel Categories - visualizes categorical data across multiple dimensions
- Interactive tabular data view with filtering and sorting capabilities
- Browser-based user interface with tabbed navigation
- JavaScript integration via Eel (e.g., for server shutdown)
- Color-coded data visualization for better pattern recognition

## 🛠 Technologies

- **Python** - Core programming language
- **Dash** - Web application framework for building analytical web applications
- **Plotly** - Interactive visualization library
- **Pandas** - Data manipulation and analysis library
- **Eel** - Library for creating simple Electron-like offline HTML/JS GUI apps
- **HTML/CSS/JS** - Frontend (via Dash)
- **Bootstrap Components** - For responsive UI elements

## 🧩 Architecture

The project follows the MVC (Model-View-Controller) pattern:

- **Model**: Processes data and contains application logic
  - `model.py` - Main model class that integrates other components
  - `data.py` - Manages data structures and visualization settings
  - `resourceController.py` - Handles file parsing and data processing
  - `dashApp.py` - Manages Dash application creation
- **View**: Responsible for the user interface
  - `view.py` - Defines UI components and layout
  - `web/main.html` - Entry point for the Eel application
- **Controller**: Manages flow between model and view
  - `controller.py` - Contains callback functions and application logic
  - `main.py` - Application entry point

## 📂 Project Structure

    IMP/
    ├── controller.py      # Controller component with callback functions
    ├── view.py            # View component defining UI layout
    ├── model.py           # Model component integrating other components
    ├── data.py            # Data structures and visualization settings
    ├── dashApp.py         # Dash application creation
    ├── resourceController.py # File parsing and data processing
    ├── main.py            # Application entry point
    ├── requirements.txt   # Project dependencies
    ├── assets/            # Static assets for Dash
    └── web/
        └── main.html      # Entry point for Eel application

    Exemplary_data/
    └── League_of_legends_stats.csv # Sample data file

## 🔄 Data Flow

1. User uploads a data file through the UI
2. The file is parsed by `resourceController.py`
3. The data is processed and a COLOR_ID column is added for visualization
4. The visualization is updated based on the selected graph type
5. The data is displayed in both graphical and tabular formats

## ▶️ Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/multidimensional_dashboard.git
cd multidimensional_dashboard
```

2. Install required libraries:
```
pip install -r requirements.txt
```

### Running the Application

1. Run the application:
```
python main.py
```

2. The application will automatically open in your default web browser at http://127.0.0.1:8050/

## 💡 Usage

1. **Upload Data**: Use the drag-and-drop area or click to select files (CSV, XLS, TSV, TXT)
2. **Visualize Data**: The data will be automatically visualized using Parallel Coordinates by default
3. **Change Visualization**: Go to the Settings tab to switch between Parallel Coordinates and Parallel Categories
4. **Interact with Data**: Use the interactive table to filter, sort, and explore your data

## ⚠️ Troubleshooting

- If file parsing errors occur, the user will receive a notification in the interface
- Make sure your data file has proper formatting and column headers
- For optimal visualization, numerical data works best with Parallel Coordinates, while categorical data works best with Parallel Categories

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📄 License

This project is licensed under the MIT License.

---

# 📊 Multidimensional Data Visualization Dashboard [PL]

Interaktywna aplikacja webowa oparta na Dash, Plotly oraz Eel, umożliwiająca wizualizację wielowymiarowych danych za pomocą wykresów równoległych. Projekt został zorganizowany zgodnie z architekturą MVC (Model-View-Controller).

## 🚀 Funkcjonalności

- Przesyłanie plików danych w formatach: CSV, XLS, TSV, TXT
- Dynamiczna wizualizacja danych przy użyciu:
  - Parallel Coordinates (Współrzędne równoległe) - wizualizacja danych numerycznych w wielu wymiarach
  - Parallel Categories (Kategorie równoległe) - wizualizacja danych kategorycznych w wielu wymiarach
- Interaktywny widok tabelaryczny danych z możliwością filtrowania i sortowania
- Przeglądarkowy interfejs użytkownika z nawigacją opartą na zakładkach
- Integracja z JavaScript przez Eel (np. do zamykania serwera)
- Kolorowanie danych dla lepszego rozpoznawania wzorców

## 🛠 Technologie

- **Python** - Główny język programowania
- **Dash** - Framework do tworzenia aplikacji webowych do analizy danych
- **Plotly** - Biblioteka do interaktywnych wizualizacji
- **Pandas** - Biblioteka do manipulacji i analizy danych
- **Eel** - Biblioteka do tworzenia prostych aplikacji GUI offline w HTML/JS
- **HTML/CSS/JS** - Frontend (przez Dash)
- **Bootstrap Components** - Dla responsywnych elementów UI

## 🧩 Architektura

Projekt oparty jest o model MVC:

- **Model**: Przetwarza dane i zawiera logikę aplikacji
  - `model.py` - Główna klasa modelu integrująca inne komponenty
  - `data.py` - Zarządza strukturami danych i ustawieniami wizualizacji
  - `resourceController.py` - Obsługuje parsowanie plików i przetwarzanie danych
  - `dashApp.py` - Zarządza tworzeniem aplikacji Dash
- **View**: Odpowiada za interfejs użytkownika
  - `view.py` - Definiuje komponenty UI i układ
  - `web/main.html` - Punkt wejścia dla aplikacji Eel
- **Controller**: Zarządza przepływem między modelem a widokiem
  - `controller.py` - Zawiera funkcje callback i logikę aplikacji
  - `main.py` - Punkt wejścia aplikacji

## 📂 Struktura projektu

    IMP/
    ├── controller.py      # Komponent kontrolera z funkcjami callback
    ├── view.py            # Komponent widoku definiujący układ UI
    ├── model.py           # Komponent modelu integrujący inne komponenty
    ├── data.py            # Struktury danych i ustawienia wizualizacji
    ├── dashApp.py         # Tworzenie aplikacji Dash
    ├── resourceController.py # Parsowanie plików i przetwarzanie danych
    ├── main.py            # Punkt wejścia aplikacji
    ├── requirements.txt   # Zależności projektu
    ├── assets/            # Statyczne zasoby dla Dash
    └── web/
        └── main.html      # Punkt wejścia dla aplikacji Eel

    Exemplary_data/
    └── League_of_legends_stats.csv # Przykładowy plik danych

## 🔄 Przepływ danych

1. Użytkownik przesyła plik danych przez UI
2. Plik jest parsowany przez `resourceController.py`
3. Dane są przetwarzane i dodawana jest kolumna COLOR_ID dla wizualizacji
4. Wizualizacja jest aktualizowana na podstawie wybranego typu wykresu
5. Dane są wyświetlane zarówno w formacie graficznym, jak i tabelarycznym

## ▶️ Rozpoczęcie pracy

### Wymagania wstępne

- Python 3.6 lub wyższy
- pip (instalator pakietów Python)

### Instalacja

1. Sklonuj repozytorium:
```
git clone https://github.com/yourusername/multidimensional_dashboard.git
cd multidimensional_dashboard
```

2. Zainstaluj wymagane biblioteki:
```
pip install -r requirements.txt
```

### Uruchamianie aplikacji

1. Uruchom aplikację:
```
python main.py
```

2. Aplikacja automatycznie otworzy się w domyślnej przeglądarce pod adresem http://127.0.0.1:8050/

## 💡 Użytkowanie

1. **Przesyłanie danych**: Użyj obszaru przeciągnij i upuść lub kliknij, aby wybrać pliki (CSV, XLS, TSV, TXT)
2. **Wizualizacja danych**: Dane zostaną automatycznie zwizualizowane za pomocą Współrzędnych równoległych domyślnie
3. **Zmiana wizualizacji**: Przejdź do zakładki Ustawienia, aby przełączać między Współrzędnymi równoległymi a Kategoriami równoległymi
4. **Interakcja z danymi**: Użyj interaktywnej tabeli do filtrowania, sortowania i eksploracji danych

## ⚠️ Rozwiązywanie problemów

- W przypadku błędów parsowania pliku, użytkownik otrzyma powiadomienie w interfejsie
- Upewnij się, że plik danych ma odpowiedni format i nagłówki kolumn
- Dla optymalnej wizualizacji, dane numeryczne najlepiej działają ze Współrzędnymi równoległymi, a dane kategoryczne najlepiej działają z Kategoriami równoległymi

## 🤝 Współpraca

Wkłady, zgłoszenia problemów i prośby o funkcje są mile widziane!

## 📄 Licencja

Projekt udostępniany na licencji MIT.
