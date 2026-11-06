import numpy as np


def calculate_crime_rate(crimes, population):
    """Calculate recorded crimes per 1,000 residents."""

    if np.any(np.asarray(population) <= 0):
        raise ValueError("Population must be greater than zero.")

    return (crimes / population) * 1000