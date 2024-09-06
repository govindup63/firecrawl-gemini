# Content Analyzer

## Overview

The Content Analyzer is a web application that leverages Firecrawl, a powerful web scraping tool, and Gemini to analyze and summarize the content of web pages. It allows users to input a URL, scrape the content of the page, and generate a summary along with key points, which can be useful for quickly understanding large amounts of information.

## Demo

https://github.com/user-attachments/assets/80f6fd1a-9ba0-4152-a6a8-fbee1dbf0f90


## Features

- **URL Input**: Users can input any URL to analyze.
- **Content Scraping**: Utilizes Firecrawl SDK to scrape the content of the given web page.
- **Content Summary**: Generates a concise summary of the scraped content use Gemini.
- **Key Points Extraction**: Extracts important points from the content for quick insights.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8+
- Flask
- Firecrawl SDK
- Gemini API

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/content-analyzer.git
    cd content-analyzer
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Set Up Environment Variables:**

    Create a `.env` file in the root directory and add your Firecrawl and Gemini API credentials:

    ```
    FIRECRAWL_API_KEY=your_firecrawl_api_key
    GEMINI_API_KEY=your_gemini_api_key
    ```

## Usage

1. **Run the Application:**

    ```bash
    flask run
    ```

2. **Access the Application:**

    Open your web browser and go to `http://127.0.0.1:5000`.

3. **Input a URL:**

    Enter the URL of the web page you want to analyze and click "Analyze."

4. **View Results:**

    The application will display a summary and key points extracted from the content of the page.

