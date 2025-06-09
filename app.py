from flask import Flask, render_template, request, jsonify
app = Flask(__name__)



# Home Page Route
@app.route('/')
def index():
    return render_template('index.html')

# Overview Page Route
@app.route('/music')
def music():
    return render_template('music.html')    
@app.route('/analysis')
def analysis():
    return render_template('analysis.html')
# Tools Used Page Route
@app.route('/tools_used')
def tools():
    return render_template('tools.html')
if __name__ == '__main__':
    app.run(debug=True)