from flask import Flask, request, jsonify, render_template
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import find_dotenv, load_dotenv

app = Flask(__name__)

#Get video data
embeddings = OpenAIEmbeddings()
def create_db_from_youtube_video_url(video_url):
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db
video_url = "https://www.youtube.com/watch?v=m04_yk-Y7Is"
create_db_from_youtube_video_url(video_url)

#default route
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


#form route
@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get('question')
    answer = f"This is a sample answer to your question: '{question}'"
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)