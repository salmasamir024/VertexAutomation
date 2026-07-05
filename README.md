# Vertex Automation

Automation system for processing cadastral survey requests.

## Features

- Scan Vertex project folders
- Read Excel database
- Link requests with Excel
- Update shapefiles
- Export result folders
- AI pipeline for National ID extraction (Work in Progress)
- Desktop UI

## Project Structure

```
app/
ai/
ui/
tests/
output/
result/
```

## Installation

```bash
git clone https://github.com/salmasamir024/VertexAutomation.git
cd VertexAutomation

python -m venv .venv

source .venv/Scripts/activate

pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Current Status

✅ Scanner

✅ Excel Integration

✅ SHP Update

✅ Export Result

🟡 AI OCR (In Progress)

🟡 UI Dashboard