class FrameParser:
    def __init__(self):
        self.buf = bytearray()   # dein interner Puffer, lebt zwischen Aufrufen

    def feed(self, data):
        self.buf.extend(data)    # Neues hinten anhängen
        frames = []              # hier sammelst du fertige Payloads


        if self.buf[0] == 0xAA:  
        return frames