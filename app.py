from flask import Flask, render_template, request
from firecrawl_utils import scrape_website
import markdown

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    scrape_result = scrape_website(url)
    html_content = markdown.markdown(scrape_result)
    return render_template('index.html', url=url, result=html_content)

if __name__ == "__main__":
    app.run(debug=True)
