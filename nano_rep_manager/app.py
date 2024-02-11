from quart import Quart
from views import main
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def create_app():
    app = Quart(__name__)
    app.register_blueprint(main)
    return app


# Create an app instance for Hypercorn to use
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
