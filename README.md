# Climate Challenge Week 0

## Setup Instructions

1. Clone repo:
git clone https://github.com/<hawire>/climate-challenge-week0.git

2. Create virtual environment:
python -m venv venv

3. Activate:
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

4. Install dependencies:
pip install -r requirements.txt

## CI
GitHub Actions runs automatically on every push to main.
## Project Structure

- `data/` → Raw climate datasets (ignored in git)
- `notebooks/` → EDA per country
- `src/` → Data processing functions
- `scripts/` → Pipeline execution scripts
- `tests/` → Unit tests
- `docs/` → Notes and documentation
