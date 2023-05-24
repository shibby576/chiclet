from flask import Flask, request, jsonify, render_template
from data_processing import *
from query import *
from dotenv import find_dotenv, load_dotenv


app = Flask(__name__)

#Get video data using function from data_processing file
video_url = "https://www.youtube.com/watch?v=Y4bq02q71R8"
db = create_db_from_youtube_video_url(video_url)

#### On load, call function in summary (will need to add docs retun from data processing). jsonify it, and display instead of current bullets. Also test the chunck size and overlap of current data processor


#default route
@app.route('/', methods=['GET'])
def index():
    print('/ route run')
    return render_template('index.html')


#form route
@app.route('/ask', methods=['POST'])
def ask():
    print('/ask route run')
    question = request.form.get('question')
    response, docs = get_response_from_query(db, question)
    answer = f"{response}'"
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)