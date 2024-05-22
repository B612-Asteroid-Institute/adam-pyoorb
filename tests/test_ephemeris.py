"""
Test ephemeris generation of pyoorb
"""
from adam_core.observers.observers import Observers
from adam_core.orbits import Ephemeris
from adam_core.orbits.query import query_sbdb
from adam_core.time import Timestamp

from src.adam_core.propagator.adam_pyoorb import PYOORB


def test_pyoorb_generate_ephemeris():
    prop = PYOORB()

    edlu = query_sbdb(["Edlu"])
    
    # Create ephemeris for several observers
    times = Timestamp.from_iso8601(["2020-01-01T00:00:00", "2020-01-01T00:00:01"])

    have = prop.propagate_orbits(edlu, times, max_processes=1)

    observers = Observers.from_code("X05", times)
    have = prop.generate_ephemeris(edlu, observers)
    assert len(have) == len(edlu) * len(times)