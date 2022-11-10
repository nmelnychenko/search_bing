from bottle import Bottle, static_file, request, run, template
from bing_search import laptop_bing_search

app = Bottle()

# OUR HOMEPAGE
@app.route('/')
def index():
    return open('index.html').read()

# OUR SEARCHRESULTS
@app.route('/search')
def index():
    query = request.query['query']
    search_results = laptop_bing_search(query)
    print(search_results)
    # query = laptop_bing_search(request.query['query'])
    # print(query)
    return template(open('search.html').read(), results=search_results)

# # OUR STATIC FILES
# @app.route('/css/<filename>')
# def server_static(filename):
#     print('CSS Served')
#     return static_file(filename, root='website/css')
#
# @app.route('/js/<filename>')
# def server_static(filename):
#     print('JS Served')
#     return static_file(filename, root='website/js')
#
# @app.route('/images/<filename>')
# def server_static(filename):
#     print('Image Served')
#     return static_file(filename, root='website/images')

# RUNNING OUR SERVER
print('Serving on http://localhost:8080')

run(app, host='localhost', port=8080, reloader=True)