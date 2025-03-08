# Web Scraping Project

## Overview
This project is a Python-based web scraping tool that extracts and processes data from websites. It includes scripts to scrape images efficiently, focusing on Nepal's historical places, monuments and temples.

## Features
- Extract text and image data from web pages
- Save scraped content in a structured format
- Modular Python scripts for easy customization

## Installation
To use this project, ensure you have Python installed. Then, install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage
### Running the Main Script
To start scraping, run:

```sh
python main.py
```

### Image Scraping
If you want to scrape images separately, execute:

```sh
python img.py
```

## Project Structure
```
web_scrapping/
│── main.py              # Main script for web scraping
│── img.py               # Script for scraping images
│── tempCodeRunnerFile.py # Temporary execution file (can be ignored)
│── __pycache__/         # Cached Python files
│── .gitignore           # Ignore unnecessary files
```

## Notes
- Ensure the target website allows web scraping (check `robots.txt` of the site).
- Modify `main.py` and `img.py` as needed for different scraping tasks.

## License
This project is open-source. Feel free to modify and use it as needed.

## Contributions
Contributions are welcome! Feel free to submit issues or pull requests.

