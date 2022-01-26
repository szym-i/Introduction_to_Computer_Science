from laboratorium_7.zadanie_1 import sprawdz_liczbe
from laboratorium_7.zadanie_1 import operacja_zamiany
from laboratorium_7.zadanie_1 import sprawdz_systemy
import pytest

#Act
result1 = operacja_zamiany(2,8,"1111")
result2 = operacja_zamiany(2,10,"1111")
result3 = operacja_zamiany(8,16,"777")
result4 = operacja_zamiany(16,2,"AF")
#Assert
def test_operacja_zamiany():
    assert result1 == '17'
    assert result2 == '15'
    assert result3 == '1FF'
    assert result4 == '10101111'

def test_sprawdz_liczbe():
    with pytest.raises(ValueError):
        sprawdz_liczbe(2,'2')
    with pytest.raises(ValueError):
        sprawdz_liczbe(8,'8')
    with pytest.raises(ValueError):
        sprawdz_liczbe(10,'A')
    with pytest.raises(ValueError):
        sprawdz_liczbe(16,'G')

def test_sprawdz_systemy():
    with pytest.raises(Exception):
        sprawdz_systemy(1,11)
    with pytest.raises(Exception):
        sprawdz_systemy(2,4)
    with pytest.raises(Exception):
        sprawdz_systemy(5,2)
