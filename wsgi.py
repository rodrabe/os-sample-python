import logging
import os
import os.path


from jumpgate import api
from jumpgate import config as jumpgate_config

import ConfigParser

PROJECT = 'jumpgate'

if __name__ == "__main__":
    # Find configuration files
    conf = ConfigParser.RawConfigParser()
    config_files = conf.read()

    # Check for environmental variable config file
    env_config_loc = os.environ.get('JUMPGATE_CONFIG')
    if env_config_loc and os.path.exists(env_config_loc):
        config_files.insert(0, env_config_loc)


    # if not config_files:
    #     raise Exception('No config files for %s found.' % PROJECT)

    jumpgate_config.CONF()

    logger = logging.getLogger(PROJECT)
    logger.setLevel('INFO')
    logger.addHandler(logging.StreamHandler())
    app = api.Jumpgate()
    app.load_endpoints()
    app.load_drivers()

    app.make_api()
