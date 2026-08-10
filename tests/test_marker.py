from pylogger.marker_reader import MarkerReader

def test_single_value():
    r = MarkerReader()
    out = r.feed(bytes([0xFF, 0x2A]))
    assert out == [0x2A]