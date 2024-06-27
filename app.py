from flask import Flask, render_template

app = Flask(__name__)

# # Serve images from the 'uploads' directory
# @app.route('/uploads/<path:filename>')
# def download_file(filename):
#     uploads_dir = os.path.join(app.root_path, 'uploads')
#     return send_from_directory(directory=uploads_dir, filename=filename)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



    