from flask import Flask, render_template, request
import vsearch
import os

FACES_FOLDER = os.path.join('static')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FACES_FOLDER

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results : '
    results = str(vsearch.search4letters(phrase,letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results)

@app.route('/') 
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')

@app.route('/facedetector')
def face_detector() -> 'html':
    title = 'Input image URL for image detection : '
    return render_template('face.html',
                           the_title=title)

@app.route('/detector', methods=['POST'])
def image_recognition() -> 'html':
    imageurl = request.form['imageurl']
    image = vsearch.facedetector(imageurl)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], image)
    title = 'Here are your results : '
    return render_template('faceresults.html',
                           the_title=title,
                           the_imageurl=imageurl,
                           the_results=full_filename)

if __name__ == '__main__':
    app.run(debug=True)
