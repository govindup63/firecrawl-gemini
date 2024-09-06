from firecrawl import FirecrawlApp
import google.generativeai as genai
import os

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")
# Initialize Firecrawl SDK with API key
app = FirecrawlApp(api_key="YOUR_FIRECRAWL_API_KEY")

def scrape_website(url):
    """Scrape the given URL and return markdown and HTML content."""
    scrape_result = app.scrape_url(url, params={'formats': ['markdown', 'html']})
    print(scrape_result['markdown'])
    response = model.generate_content("the text given below is a markdown scrapping of a url summarise that text and return a detailed results of entire page without adding any extra text on top jus the summary of the website"+scrape_result['markdown'])
    return response.text

