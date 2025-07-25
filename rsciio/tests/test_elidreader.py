import numpy as np
from rsciio.phenom._api import ElidReader

def test_elidreader():
    height = 10
    width = 10
    bins = 10

    reader = ElidReader("tests/data/elid/test.elid")

    # 1) read the data bytes via read_varuint32 (reliable but slow)
    data = np.empty([height, width, bins], dtype=np.uint32)
    for y in range(height):
        for x in range(width):
            for bin in range(bins):
                data[y, x, bin] = self._read_varuint32()

    # 2) read the data bytes the new-fashioned way