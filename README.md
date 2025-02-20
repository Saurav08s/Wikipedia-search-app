# Wikipedia Search API

## Project Overview
The **Wikipedia Search API** project is a Flask-based web application that allows users to search for Wikipedia articles and retrieve relevant summaries. The project integrates with Wikipedia's API and provides a user-friendly interface to explore content efficiently.

---

## Features
- **Search Wikipedia Articles** by keywords.
- **Retrieve Summaries** of articles.
- **Display Results** in a structured format.
- **JSON Response Support** for easy integration.
- **Simple HTML Interface** for user interaction.

---

## Technologies Used

### Programming Language:
- **Python** (Flask Framework)

### Libraries:
- **Flask** - For building the web application
- **Requests** - For making API calls to Wikipedia
- **JSON** - For handling responses

---

## Project Structure
- **app.py**: The main Flask application file.
- **templates/index.html**: The frontend HTML interface.
- **static/**: (Optional) Directory for static assets.

---

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/wikipedia-search-api.git
   cd wikipedia-search-api
   ```
2. Install dependencies:
   ```bash
   pip install flask requests
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## Usage
1. Enter a search term in the input field.
2. Click the search button.
3. The app fetches relevant Wikipedia articles and displays summaries.

---

## Future Improvements
- **Implementing Caching** to reduce API requests.
- **Enhancing UI/UX** for better user experience.
- **Adding More API Features** such as fetching article sections or related topics.

---

## Contribution
Feel free to fork the repository and submit pull requests for enhancements!

---

## License
This project is open-source and available under the **MIT License**.
