### Test for name package

from alert import script

def test_name(): 
    foo = script.add(1,2)
    assert(foo == 3)
