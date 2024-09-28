# Import necessary libraries 
from flask import Flask, request, render_template 
import wikipediaapi 

app = Flask(__name__) 

# Initialize the Wikipedia API with a user agent
user_agent = "MyWikipediaApp/1.0 (https://example.com)"  # Replace with your app's user agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent=user_agent
)

# Create HOME View 
@app.route("/", methods=["POST", "GET"]) 
def home(): 
    if request.method == "GET": 
        return render_template("index.html") 
    else: 
        search = request.form["search"] 

        # Fetch data from Wikipedia
        page = wiki_wiki.page(search)

        if page.exists():
            result = page.summary[:2500]  # Get the first 500 characters of the summary
            return f"<h3>{result}</h3>"
        else:
            return f"<h2>No page found for '{search}'</h2>"

if __name__ == '__main__': 
    app.run(debug=True) 
