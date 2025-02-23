from flask import Flask, render_template, request
from exa_py import Exa

app = Flask(__name__)
exa = Exa(api_key="YOUR KEY")

@app.route('/', methods=['GET', 'POST'])
def search():
    results = []
    if request.method == 'POST':
        search_query = request.form.get('searchquery')
        response = exa.search(search_query, num_results=5, type='keyword',)
        results = response.results
    
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

