import nmbr
import pytest


@pytest.mark.parametrize('n', (range(1, 7)))
def test_all_simple(n):
    N = nmbr.Nmbr(nmbr.WORDS[:n])
    m = N.count(n)
    for i in range(m):
        words = N(i)
        assert len(words) == len(set(words))
        assert N(words) == i, str(words)

    err = f'Cannot represent {m} in base {n}'
    with pytest.raises(ValueError, match=err):
        N(m)