from flasgger import Swagger
from app import create_app

app = create_app()
swagger = Swagger(app)  # ініціалізує Swagger

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

