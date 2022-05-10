diary - num_receive = request.form['diary-num_give']


@app.route('/diary/recommend', methods=['POST'])
def diary_recommend():
    diary-num_receive = request.form['diary-num_give']

    doc = {
        'title' : title_receive,
        'content' : content_receive
    }

    return jsonify({'msg': '추천 완료!'})


@app.route('/diary/report', methods=['POST'])
def diary_report():
    diary-num_receive = request.form['diary-num_give']

    doc = {
        'title' : title_receive
        'content' : content_receive
    }

    return jsonify({'msg': '신고 완료!'})


@app.route('/diary', methods=['GET'])
def show_diary():
    image_receive = request.form['image_give']
    name_receive = request.form['name_give']
    title_receive = request.form['title_give']
    texts_receive = request.form['texts_give']
    weather_receive = request.form['weather_give']
    diary-num_receive = request.form['diary-num_give']

    return jsonify({'msg': 'GET 연결 완료!'})