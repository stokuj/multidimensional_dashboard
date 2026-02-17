# Multidimensional Data Visualization Dashboard

Interactive dashboard for exploring multidimensional datasets with Plotly and Dash, wrapped in an Eel desktop window.

## Features

- Upload and parse `CSV`, `XLS/XLSX`, `TSV`, and `TXT` files
- Visualize data with Parallel Coordinates and Parallel Categories
- Inspect uploaded data in an interactive Dash table (filter, sort, paginate)
- Run as a desktop app (Eel window) while serving Dash locally

## Tech Stack

- Python 3.11+
- Dash
- Plotly
- Pandas
- Eel
- `uv` for dependency and environment management

## Project Structure

```text
.
|- app/
|  |- controller.py
|  |- model.py
|  |- view.py
|  |- data.py
|  |- resourceController.py
|  |- dashApp.py
|  |- assets/
|  \- web/
|     \- main.html
|- Exemplary_data/
|  \- League_of_legends_stats.csv
|- main.py
|- pyproject.toml
\- uv.lock
```

## Getting Started

1. Install dependencies and run app:

```bash
uv sync
uv run python main.py
```

## Runtime Behavior

- Dash server runs at `http://127.0.0.1:8050`.
- Eel starts a local desktop host (default `localhost:8000`, with automatic fallback if the port is busy).
- Closing the desktop window also shuts down the Dash server.

## License

MIT (see `LICENSE`).
