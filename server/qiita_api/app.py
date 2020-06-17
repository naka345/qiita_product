from flask import Flask, jsonify, request, render_template
import json
from script.qiita_api import QiitaApi
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return render_template("main.html", url="https://yahoo.co.jp")

@app.route("/q_api", methods=['GET'])
def call_qiita_api():
    api = QiitaApi()
    scope = ["read_qiita", "write_qiita"]
    url = api.call_authorization_url(scope=QiitaApi.define_scope(scope))
    print(url)
    return render_template("main.html", url=url)

@app.route("/q_api", methods=['POST'])
def redirect_qiita_api
    api.access_tokens(code)
    items = api.get_item()
    pick_up_keys = ["title","url","body","private"]
    items_dict = api.adjust_item(items,pick_up_keys)
    return items_dict

@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)
    answer = "Yes, it is %s!\n" % data["keyword"]
    result = {
      "Content-Type": "application/json",
      "Answer":{"Text": answer}
    }
    # return answer
    return jsonify(result)

if __name__ == "__main__":
    app.run()
