from flask import Flask, render_template

app = Flask(__name__)

# Serve images from the 'uploads' directory
@app.route('/uploads/<path:filename>')
def download_file(fil