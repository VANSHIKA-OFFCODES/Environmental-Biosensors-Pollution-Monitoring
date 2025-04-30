import streamlit as st
from PIL import Image
import os

# Inject custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

# Optional: Set a custom icon if available
icon_path = "assets/icon.png"
if os.path.exists(icon_path):
    st.image(icon_path, width=80)

# Title
st.title("EnviroSense")
st.subheader("An intelligent biosensor interface for real-time environmental monitoring.")

# Sample interactive feature
query = st.text_input("🔍 Search")

if query:
    st.success(f"You searched for: {query}")
else:
    st.info("Type something in the box above to get started!")

# Show your skill — add some buttons
if st.button("Click here"):
    st.balloons()
    st.toast("You just clicked a button that shows off my Streamlit skills!")

# Footer
st.markdown("""<footer>Made with 💻 and ☕ by <b>Vanshika</b></footer>""", unsafe_allow_html=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the homepage (index.html)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')  # Get the search query
    results = []  # You would get actual results from your data here

    if query:
        results = search_data(query)  # Define the search logic based on your app's needs

    return render_template('search_results.html', query=query, results=results)

def search_data(query):
    # You'd implement the actual search logic to filter your environmental data
    # For now, we'll just mock the search results
    return [f"Result for {query} - Example data"]

if __name__ == '__main__':
    app.run(debug=True)
