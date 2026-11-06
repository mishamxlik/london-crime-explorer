from calculations import calculate_crime_rate


def test_crime_rate_calculation():
    result = calculate_crime_rate(250, 5000)
    assert result == 50


def test_crime_rate_with_different_population():
    result = calculate_crime_rate(120, 3000)
    assert result == 40


def test_zero_population():
    try:
        calculate_crime_rate(100, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")


def test_negative_population():
    try:
        calculate_crime_rate(100, -500)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")
    
def test_crime_rate_with_pandas():
    import pandas as pd

    crimes = pd.Series([250, 120])
    population = pd.Series([5000, 3000])

    result = calculate_crime_rate(crimes, population)

    assert result.tolist() == [50, 40]