import yaml
from yaml.loader import SafeLoader
import os
from utilities.network import network
from utilities.logger import logger
from utilities.game import game

logger.setup_applevel_logger()
LOGGER = logger.get_logger(__name__)
project_path = os.path.dirname(os.path.abspath(__file__))


def main():
    LOGGER.debug("Enter main()")
    with open("config.yaml") as config:
        try:
            LOGGER.debug("Reading config file")
            config = yaml.load(config, Loader=SafeLoader)
        except yaml.YAMLError as exception:
            LOGGER.exception("Failed to parse config.yaml, please ensure the file is in the correct format")
    LOGGER.info("Starting Client to connect at %(config['address'])s")
    instance = game.Game(config, project_path)
    instance.run()
    # client = network.Client(config)
    # client.run()
    LOGGER.debug("Exit main()")


if __name__ == "__main__":
    LOGGER.info("Starting Application")
    main()
    LOGGER.info("Closing Application")
