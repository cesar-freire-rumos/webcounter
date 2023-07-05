import sys
import os

## Add root path to allow run file form inside and outside path
sys.path.insert(0, os.path.join(os.getcwd(), "."))

# import redis cache
from webcounter import redis_helper as redis


def test_get_hits_count():
    """ Just test get_hits_count """

    start_counter = redis.get_hits_count()
    result = redis.get_hits_count()
    assert result > start_counter
