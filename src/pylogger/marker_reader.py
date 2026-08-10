
class MarkerReader:
    """Sammelt jedes Byte, das direkt auf 0xFF folgt."""

    def __init__(self):
        self.buf = bytearray()

    def feed(self, data):
        self.buf.extend(data)
        results = []
        while len(self.buf) >= 2:          # Marker + Wert = 2 Bytes minimum
            if self.buf[0] != 0xFF:        # kein Marker vorne?
                del self.buf[:1]           # ein Byte wegwerfen, weiter suchen
                continue
            value = self.buf[1]            # das Byte nach dem Marker
            results.append(value)
            del self.buf[:2]               # Marker + Wert sind verarbeitet
        return results


