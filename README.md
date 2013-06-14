python-memcached
================

python implementation of memcached using pylibmc library.

Installation Instructions:
1. sudo apt-get install memcached

2. sudo apt-get install libmemcached-dev

3. sudo pip install pylibmc

4. Memcache setting file resides in /etc/memcached.conf, use default or change the memory settings. 

5. Start the memcached server: sudo service memcached start

6. Check for stats: nc localhost 11211, key in stats to get all stats.

7. Cache module for piQto server uses pylibmc (A python wrapper over memcache) and contains the following files.

	a. cachesettings.ini – server list, timeout settings. Can add more if required.
	
	b. cacheconfigparser.py – config parser for the ini file.
	
	c. cache.py – module for setting and getting the cache values. 
	
	d. test.py – test script for the above code.

