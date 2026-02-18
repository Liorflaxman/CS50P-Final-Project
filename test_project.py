import pytest
from project import Movie

def test_movie_init():
    m = Movie("Interstellar", "US")
    assert m.movie == "Interstellar"
    assert m.country == "US"
    assert m.id is None

def test_empty_movie_and_country_format():
    m = Movie()
    with pytest.raises(ValueError):
        m.movie = ""

    with pytest.raises(ValueError):
        m.country = ""
    with pytest.raises(ValueError):
        m.country = "USA"
    with pytest.raises(ValueError):
        m.country = "B"
    m.country = "US"
    assert m.country == "US"

def test_string():
    m = Movie("Moneyball", "US")
    assert str(m) == "You want to watch Moneyball in US (ID couldnt be found)"

    m.id = 5000
    assert "ID is 5000" in str(m)
