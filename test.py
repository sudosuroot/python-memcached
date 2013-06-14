import cache

value = {'hello' : 'world'}
dict1 = {'x' : 1, 'y' : 2}
result = cache.get_result_for_params(dict1)
if (result):
  print "Getting from cache"
  print result
else:
  print "Cache not found, setting to cache"
  success = cache.set_result_for_params(dict1, value)
  if (success):
    print value
  else:
    print "Error in setting the cache"
