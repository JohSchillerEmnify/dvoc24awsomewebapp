from flask import Flask, render_template_string, request, redirect, url_for
import random

app = Flask(__name__)

def is_valid_input(input_str):
    return len(input_str) <= 5 and input_str[4] == '😊'

@app.route('/', methods=['GET', 'POST'])
def captcha():
    if request.method == 'POST':
        captcha_solution = request.form.get('captcha_solution')
        if captcha_solution == '5':
            return redirect(url_for('home'))
    return render_template_string('''<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Captcha</title><style>
body{font-family:Arial,sans-serif;display:flex;justify-content:center;align-items:center;height:100vh;background-color:#f0f0f0;margin:0}
.container{text-align:center;background:white;padding:20px;border-radius:10px;box-shadow:0 0 10px rgba(0,0,0,0.1)}
button{background-color:#4CAF50;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;font-size:16px}
button:hover{background-color:#45a049}
#loading-screen{display:flex;justify-content:center;align-items:center;position:fixed;top:0;left:0;width:100%;height:100%;background-color:white;z-index:1000;flex-direction:column}
#loading-screen .spinner{border:16px solid #f3f3f3;border-top:16px solid #3498db;border-radius:50%;width:120px;height:120px;animation:spin 2s linear infinite}
@keyframes spin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
#loading-bar-container{width:80%;background-color:#f3f3f3;border-radius:25px;margin-top:20px}
#loading-bar{width:0%;height:30px;background-color:#3498db;border-radius:25px;text-align:center;line-height:30px;color:white}
#ad{margin-top:20px;font-size:18px;color:#333}
</style></head><body>
<div id="loading-screen">
    <div class="spinner"></div>
    <div id="loading-bar-container">
        <div id="loading-bar">0%</div>
    </div>
    <div id="ad">
        <img src="{{ url_for('static', filename='emnify_logo.png') }}" alt="emnify logo" style="width: 150px;">
        <div>emnify, best mobile iot</div>
    </div>
    <div id="cat-shrimp">
        <svg width="100" height="100" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2C10.8954 2 10 2.89543 10 4V5H8V4C8 2.89543 7.10457 2 6 2C4.89543 2 4 2.89543 4 4V5H2V4C2 2.89543 1.10457 2 0 2V4C1.10457 4 2 4.89543 2 6V7H4V6C4 4.89543 4.89543 4 6 4C7.10457 4 8 4.89543 8 6V7H10V6C10 4.89543 10.8954 4 12 4C13.1046 4 14 4.89543 14 6V7H16V6C16 4.89543 16.8954 4 18 4C19.1046 4 20 4.89543 20 6V7H22V6C22 4.89543 22.8954 4 24 4V2C22.8954 2 22 2.89543 22 4V5H20V4C20 2.89543 19.1046 2 18 2C16.8954 2 16 2.89543 16 4V5H14V4C14 2.89543 13.1046 2 12 2Z" fill="#000"/>
        </svg>
    </div>
</div>
<div class="container" style="display:none;">
<h1>Captcha</h1>
<form method="post">
<label for="captcha_solution">What is 2 + 3? <script>alert('Include a smiley emoji 😊 as the fifth character');</script></label>
<input type="text" id="captcha_solution" name="captcha_solution" required>
<button type="submit">Submit</button>
</form>
</div>
<script>
function updateLoadingBar() {
    var loadingBar = document.getElementById('loading-bar');
    var width = 0;
    var interval = setInterval(function() {
        if (width >= 100) {
            clearInterval(interval);
            document.getElementById('loading-screen').style.display = 'none';
            document.querySelector('.container').style.display = 'block';
        } else {
            width += Math.random() * 5; // Randomly increase the width
            if (width > 100) width = 100;
            loadingBar.style.width = width + '%';
            loadingBar.innerHTML = Math.floor(width) + '%';
        }
    }, Math.random() * 200 + 50); // Randomly change the interval time
}

window.onload = function() {
    updateLoadingBar();
};
</script>
</body></html>''')
result = None
@app.route('/home', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST' and is_valid_input(request.form.get('roll_input')):
        
        for _ in range(1000000):
            result = random.randint(1, 6)
            
    return render_template_string('''<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Dice Roller</title><style>
body{font-family:Arial,sans-serif;display:flex;justify-content:center;align-items:center;height:100vh;background-color:#f0f0f0;margin:0}
.container{text-align:center;background:white;padding:20px;border-radius:10px;box-shadow:0 0 10px rgba(0,0,0,0.1)}
button{background-color:#4CAF50;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;font-size:16px}
button:hover{background-color:#45a049}
#loading-screen{display:flex;justify-content:center;align-items:center;position:fixed;top:0;left:0;width:100%;height:100%;background-color:white;z-index:1000;flex-direction:column}
#loading-screen .spinner{border:16px solid #f3f3f3;border-top:16px solid #3498db;border-radius:50%;width:120px;height:120px;animation:spin 2s linear infinite}
@keyframes spin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
#loading-bar-container{width:80%;background-color:#f3f3f3;border-radius:25px;margin-top:20px}
#loading-bar{width:0%;height:30px;background-color:#3498db;border-radius:25px;text-align:center;line-height:30px;color:white}
#ad{margin-top:20px;font-size:18px;color:#333}
</style></head><body>
<div id="loading-screen">
    <div class="spinner"></div>
    <div id="loading-bar-container">
        <div id="loading-bar">0%</div>
    </div>
    <div id="ad">
        <img src="{{ url_for('static', filename='emnify_logo.png') }}" alt="emnify logo" style="width: 150px;">
        <div>emnify, best mobile iot</div>
    </div>
    <div id="cat-shrimp">
        <svg width="100" height="100" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2C10.8954 2 10 2.89543 10 4V5H8V4C8 2.89543 7.10457 2 6 2C4.89543 2 4 2.89543 4 4V5H2V4C2 2.89543 1.10457 2 0 2V4C1.10457 4 2 4.89543 2 6V7H4V6C4 4.89543 4.89543 4 6 4C7.10457 4 8 4.89543 8 6V7H10V6C10 4.89543 10.8954 4 12 4C13.1046 4 14 4.89543 14 6V7H16V6C16 4.89543 16.8954 4 18 4C19.1046 4 20 4.89543 20 6V7H22V6C22 4.89543 22.8954 4 24 4V2C22.8954 2 22 2.89543 22 4V5H20V4C20 2.89543 19.1046 2 18 2C16.8954 2 16 2.89543 16 4V5H14V4C14 2.89543 13.1046 2 12 2Z" fill="#000"/>
        </svg>
    </div>
</div>
<div class="container" style="display:none;">
<h1>Dice Roller</h1>
<form method="post">
<label for="roll_input"></label>
<input type="password" id="roll_input" name="roll_input" required>
<button type="submit">Roll the Dice</button>
</form>
{% if result is not none %}
<script>alert('You rolled a {{ result }}');</script>
{% endif %}
</div>
<script>
function updateLoadingBar() {
    var loadingBar = document.getElementById('loading-bar');
    var width = 0;
    var interval = setInterval(function() {
        if (width >= 100) {
            clearInterval(interval);
            document.getElementById('loading-screen').style.display = 'none';
            document.querySelector('.container').style.display = 'block';
        } else {
            width += Math.random() * 5; // Randomly increase the width
            if (width > 100) width = 100;
            loadingBar.style.width = width + '%';
            loadingBar.innerHTML = Math.floor(width) + '%';
        }
    }, Math.random() * 200 + 50); // Randomly change the interval time
}

window.onload = function() {
    updateLoadingBar();
};
</script>
</body></html>''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
