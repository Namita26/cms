from flask import Flask, render_template, request, url_for
from flask import current_app as app

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('templates/concept_creation.html')


@app.route('/hello/', methods=['POST'])
def hello():
    name=request.form['yourname']
    email=request.form['youremail']
    return render_template('form_action.html', name=name, email=email)

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("80")
  )
