import pytest

import numpy as np
from npcirclepack import pack_enclose

def test_basic():
    radii = np.array([1,2,3])
    pos = np.zeros((3,3),dtype=np.float32)
    pos[:,2]=radii
    enclose_radius = pack_enclose(pos)
    assert enclose_radius==5.0

def test_array_shape():
    pos = np.zeros((3,2), dtype=np.float32)
    with pytest.raises(Exception): #wrong shape, should raise exception
        _ = pack_enclose(pos)
    
def test_array_dtype():
    pos = np.zeros((3,3), dtype=np.int64)
    with pytest.raises(Exception): #wrong dtype, should raise exception
        a = pack_enclose(pos)

def test_zeros():
    pos = np.zeros((3,3), dtype=np.float32)
    enclose_radius = pack_enclose(pos)
    assert enclose_radius==0

