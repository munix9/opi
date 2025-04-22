import os
import configparser

default_config = {
	'use_releasever_var': True,
	'new_repo_auto_refresh': True,
	'list_in_reverse': False,
}

class ConfigError(Exception):
	pass

config_cache = None
def get_key_from_config(key: str):
	global config_cache
	if not config_cache:
		config_cache = default_config.copy()
		path = os.environ.get('OPI_CONFIG', '/etc/opi.cfg')
		if os.path.exists(path):
			cp = configparser.ConfigParser()
			cp.read(path)
			ocfg = cp['opi']
			config_cache.update({
				'use_releasever_var': ocfg.getboolean('use_releasever_var'),
				'new_repo_auto_refresh': ocfg.getboolean('new_repo_auto_refresh'),
				'list_in_reverse': ocfg.getboolean('list_in_reverse'),
			})
	return config_cache[key]
