from flask import Flask, request, jsonify, render_template
from data_processing import *
from query import *
from summary import *
from dotenv import find_dotenv, load_dotenv


app = Flask(__name__)

#Get video data using function from data_processing file
video_url = "https://www.youtube.com/watch?v=Q9gpg8pfyZI"
db = create_db_from_youtube_video_url(video_url)

#For summary. Currently not in use. Create DB and documents 
#db, documents = create_db_from_youtube_video_url(video_url)

#Summary: Not in use. get video summary on response
#summary = get_video_summary().run(documents)
#print('summary done')

#Summary: create HTML list out of summary. Not in use
def create_html_list(api_response):
    items = api_response.split('\n- ')
    html_list = '<ul>'

    for item in items:
        if item.strip():
            html_list += f'<li>{item.strip()}</li>'

    html_list += '</ul>'
    return html_list

#Summary: Return summary in bullet html list. Not in use
#text=create_html_list(summary)

#default route
@app.route('/', methods=['GET'])
def index():
    print('/ route run')
    
    #Summary: Return template and summary text html. Not in use
    #return render_template('index.html', text=text)
    
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