import os
from preadwrite import pread, pwrite


def test_readwrite(tmpdir):
    fd = os.open(os.path.join(str(tmpdir), "test"), os.O_TRUNC | os.O_CREAT | os.O_RDWR)
    written = pwrite(fd, 'a' * 4096, 0)
    assert written == 4096
    written = pwrite(fd, 'c' * 4096, 8192)
    assert written == 4096
    written = pwrite(fd, 'b' * 4096, 4096)
    assert written == 4096

    data = pread(fd, 4096 * 3, 0)
    assert data == 'a' * 4096 + 'b' * 4096 + 'c' * 4096
