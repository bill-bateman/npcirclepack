import pytest

from npcirclepack import pack_enclose_hierarchy

def test_basic():
    root = {
        'children': [
            {'r': 1},
            {'r': 2},
            {'r': 3},
        ]
    }
    pack_enclose_hierarchy(root)
    assert 'r' in root
    assert root['r']==1
    #check radii of children were properly scaled
    assert root['pos'][0][2]==pytest.approx(0.2)
    assert root['pos'][1][2]==pytest.approx(0.4)
    assert root['pos'][2][2]==pytest.approx(0.6)

def test_nested():
    root = {
        'children': [
            {'r': 1, 'children': [{'r':1},{'r':2}]},
            {'r': 2},
            {'r': 3},
        ]
    }
    pack_enclose_hierarchy(root)
    assert 'r' in root
    assert root['r']==1