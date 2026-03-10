from ping_sweep import sweep

def test_sweep_returns_list():
    alive = sweep("127.0.0.0/30")
    assert isinstance(alive, list)