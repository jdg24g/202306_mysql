from app import app
from app.controllers import authors, books

if __name__ == "__main__":
    app.run(debug=True,port=5500,host='0.0.0.0')