from flask import Flask
from requests import requests
app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600}
]
@app.route('/')
def hello_code():
    return 'Hello World!'

#GET /menus | 자료를 가지고 온다
#GEP 메서드는 생략
@app.route('/menus')
def get_menus():
    return jsonify({"menus":menus})

#POST /menus | 자료를 자원에 추가한다
@app.route('/menus',methods=['POST'])
def create_menu(): #request가 json이라고 가정
    #전달 받은 자료를 menus 자원에 추가
    request_data = request.get_json()
    new_menus = {
        "id":4, "name":request_data['name'], "price":request_data['price']
    }
    menus.append(new_menus)
    return jsonify(new_menus)



# PUT /menus/<int:id> : 해당하는 id에 해당하는 데이터를 갱신합니다. (HTTPRequest의 Body에 갱신할 내용이 json으로 전달됩니다.)
@app.route('/menus/<int:id>', methods=['PUT']) # URL에 <>를 붙임으로서 이를 함수의 인자로 대입할 수 있습니다.
def update_menu(id):
    request_data = request.get_json()
    for menu in menus:
        if menu.get("id", -1) == id:
            menu["name"] = request_data["name"]
            menu["price"] = request_data["price"]
    return jsonify({"menus": menus})


# DELETE /menus/<int:id> : 해당하는 id에 해당하는 데이터를 삭제합니다.
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    request_data = request.get_json()
    for i in range(len(menus)):
        if menus[i].get("id", -1) == id:
            menus.pop(i)
            break
    return jsonify({"menus": menus})


if __name__ == '__main__':
    app.run()
