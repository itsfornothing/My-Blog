My Blog

This Flask application fetches blog posts from an external API (https://api.npoint.io/c790b4d5cab58020d391) and displays them on a simple website.

Features

Fetches blog data from an external API
Renders a homepage listing two blog posts
Displays a dedicated page for each individual blog post
Requirements

Python 3.x (with Flask installed)
A code editor or IDE
Installation

Clone this repository or download the files.

Install Flask using pip:

Bash
pip install Flask
Use code with caution.

Usage

Run the application:

Bash
python server.py
Use code with caution.

Open your web browser and navigate to http://localhost:5001/ to view the homepage.

Structure

server.py: Main Flask application file, handling routing and rendering.
index.html: Homepage template, displaying a list of two blog posts.
posts.html: Template for individual blog posts.
static/style.css: Stylesheet for the website's appearance.
Customization

Modify the style.css file to change the website's visual style.
Update the API URL in server.py if you want to use a different data source.
You can add more logic to server.py to handle additional blog posts or features.
Contributing

Feel free to fork the repository and submit pull requests with your improvements.
