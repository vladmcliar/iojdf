from flask import Flask, send_from_directory
import os
app = Flask(__name__, static_folder='public')

@app.route('/')
def serve_index():
    return send_from_directory('public', 'index.html')

# Если у вас есть другие статические страницы или пути
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('public', filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)