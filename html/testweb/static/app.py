from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

app.static_folder = 'static'

# Папка для сохранения загруженных файлов
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return redirect(url_for('index'))

    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
