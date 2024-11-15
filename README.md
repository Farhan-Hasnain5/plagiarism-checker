# Plagiarism Checker

This is a simple plagiarism checker application built using Python and Tkinter. It allows users to input text and check for plagiarism by comparing the input text with content fetched from the internet using the Bing Search API. The application highlights the plagiarized parts of the text and displays the plagiarism percentage.

## Features

- Fetches content from the internet using the Bing Search API.
- Compares the input text with fetched content using TF-IDF and cosine similarity.
- Highlights the plagiarized parts of the text.
- Displays the plagiarism percentage.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `scikit-learn` library
- `tkinter` library (usually included with Python)

## Installation

1. Clone the repository or download the source code.
2. Install the required Python packages using pip:

```sh
pip install requests beautifulsoup4 scikit-learn
```
