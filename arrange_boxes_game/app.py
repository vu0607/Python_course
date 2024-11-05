from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Trạng thái của trò chơi (khởi tạo danh sách ngẫu nhiên từ 1 đến 5)
game_state = {
    "boxes": [4, 3, 1, 5, 2],
    "moves": 0
}

# Kiểm tra xem danh sách đã sắp xếp chưa
def is_sorted(boxes):
    return boxes == sorted(boxes)

@app.route('/')
def index():
    return render_template('index.html', boxes=game_state["boxes"], moves=game_state["moves"])

@app.route('/swap', methods=['POST'])
def swap():
    global game_state
    index1 = int(request.json['index1'])
    index2 = int(request.json['index2'])

    # Thực hiện hoán đổi vị trí hai hộp
    game_state["boxes"][index1], game_state["boxes"][index2] = game_state["boxes"][index2], game_state["boxes"][index1]
    game_state["moves"] += 1

    # Kiểm tra xem danh sách đã sắp xếp chưa
    sorted_status = is_sorted(game_state["boxes"])

    return jsonify({
        "boxes": game_state["boxes"],
        "moves": game_state["moves"],
        "is_sorted": sorted_status
    })

@app.route('/reset', methods=['POST'])
def reset():
    global game_state
    # Khởi tạo lại trạng thái trò chơi
    game_state["boxes"] = [4, 3, 1, 5, 2]
    game_state["moves"] = 0
    return jsonify(game_state)

if __name__ == '__main__':
    app.run(debug=True)
