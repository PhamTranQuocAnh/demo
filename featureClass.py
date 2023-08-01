from flask import Flask, jsonify, request

app = Flask(__name__)

# Danh sách các lớp học mẫu
lophocs = [
    {"class": "C101", "name": "Cong Nghe Thong Tin", "ss": 30},
    {"class": "D102", "name": "Quan Tri Kinh Doanh", "ss": 25},
    {"class": "E207", "name": "Dong Phuong Hoc", "ss": 20}
]

# API lấy thông tin tất cả lớp học
@app.route('/lophocs', methods=['GET'])
def get_lophocs():
    return jsonify(lophocs)

# API lấy thông tin của một lớp học cụ thể theo id
@app.route('/lophocs/<string:class_id>', methods=['GET'])
def get_lophoc(class_id: str):
    lophoc = next((lophoc for lophoc in lophocs if lophoc["class"] == class_id), None)
    if lophoc:
        return jsonify(lophoc)
    else:
        return jsonify({"message": "Lophoc not found"}), 404

# API tạo mới lớp học
@app.route('/lophocs', methods=['POST'])
def create_lophoc():
    data = request.get_json()
    if "name" in data and "class" in data:
        new_lophoc = {"class": data["class"], "name": data["name"]}
        lophocs.append(new_lophoc)
        return jsonify(new_lophoc), 201
    else:
        return jsonify({"message": "Class and Name are required"}), 400

# API cập nhật thông tin lớp học
@app.route('/lophocs/<string:class_id>', methods=['PUT'])
def update_lophoc(class_id: str):
    lophoc = next((lophoc for lophoc in lophocs if lophoc["class"] == class_id), None)
    if lophoc:
        data = request.get_json()
        lophoc["name"] = data["name"]
        return jsonify(lophoc)
    else:
        return jsonify({"message": "Lophoc not found"}), 404

# API xóa lớp học
@app.route('/lophocs/<string:class_id>', methods=['DELETE'])
def delete_lophoc(class_id: str):
    global lophocs
    lophocs = [lophoc for lophoc in lophocs if lophoc["class"] != class_id]
    return jsonify({"message": "Lophoc deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
