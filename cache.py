import pylibmc
import cacheconfigparser
import hashlib
import json

"""Returns the value for the config key
Takes in the section in the ini file and the config key.
"""
def GetSectionValue(section, key):
  dict1 = cacheconfigparser.ConfigSectionMap(section)
  return dict1[key.lower()]

mem_server_port_string = GetSectionValue('memcache', 'MEM_SERVER_PORT')
MEM_TIMEOUT = int (GetSectionValue('memcache', 'MEM_TIMEOUT'))
MEM_SERVER_PORT = mem_server_port_string.split(',')

mc = pylibmc.Client(MEM_SERVER_PORT, binary=True, behaviors={"tcp_nodelay": True, "ketama": True})

"""Returns the hash key for query params.
Takes in query params as a dictionary. 
"""
def get_hashkey_for_params(params):
  hash_string = ''
  for key in params:
    hash_string += str(key) + str(params[key])
  return hashlib.md5(hash_string).hexdigest()

"""
Sets the JSON string result as JSON for the query params passed.
"""
def set_result_for_params(params, result):
  success = False
  if params:
    hash_key = get_hashkey_for_params(params)
    success = mc.set(hash_key, json.dumps(result), MEM_TIMEOUT)
  return success

"""
Gets the JSON result for the query params passed.
"""
def get_result_for_params(params):
  if params:
    hash_key = get_hashkey_for_params(params)
    result = mc.get(hash_key)
    if result:
      return result
    else:
      return False
