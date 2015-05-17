from ad_mania import app
from config import Config
import logging


logger = logging.getLogger(__name__)


def application():
    config = Config().config
    app.config = config

    return app


def main():
    app = application()
    app.run(host='0.0.0.0')


if __name__ == "__main__":
    main()


