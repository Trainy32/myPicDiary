from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.kdc5v.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta_pjt_mypicDiary_test

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## 코멘트 API
@app.route('/diary/comment', methods=['GET'])
def show_comment():
    comments = list(db.comment.find({}, {'_id': False}))

    return jsonify({'all_comment': comments})

@app.route('/diary/comment', methods=['POST'])
def save_comment():
    comment_receive = request.form['comment_give']

    comment_count = list(db.comment.find({}, {'_id': False}))
    comment_num = len(comment_count) + 1

    doc = {
        'comment_num':comment_num,
        'comment': comment_receive,
        'name' : '임시이름 ',
        'comment_date' : '2022-05-10'
    }

    db.comment.insert_one(doc)

    return jsonify({'msg': '코멘트 등록 완료!'})

## 일기추천 API
@app.route('/diary/recommend', methods=['GET'])
def show_recommend():
    comments = list(db.comment.find({}, {'_id': False}))

    return jsonify({'all_comment': comments})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)