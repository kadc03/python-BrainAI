from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from gemini import Gemini
import os
from config import cookies1, cookies2, cookies3, cookies4

app = Flask(__name__)
Bootstrap(app)

cookies = {
    "__Secure-1PSIDCC" : cookies1,
    "__Secure-1PSID" : cookies2,
    "__Secure-1PSIDTS" : cookies3,
    "NID" : cookies4,
    # Cookies may vary by account or region. Consider sending the entire cookie file.
}

GeminiClient = Gemini(cookies=cookies)

os.environ["GEMINI_LANGUAGE"] = "VN"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def generate():
    user_text = request.form['msg']
    output = response_api(user_text)
    return output

def response_api(prompt):
    message = GeminiClient.generate_content(str(prompt))
    if (message.text): return message.text
    if (message.code): return message.code
    if (message.web_images): return message.web_images
    if (message.generated_images): return message.generated_images

if __name__ == '__main__':
    app.run(debug=True, port=5000)