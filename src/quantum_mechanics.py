"""
Quantum mechanics calculations and state representations.
"""

import numpy as np
from typing import List, Tuple
from .angular_momentum import AngularMomentum, clebsch_gordan_coefficient

class CoupledState:
    """Represents a coupled angular momentum state of two particles."""
    
    def __init__(self, particle1: AngularMomentum, particle2: AngularMomentum,
                 total_l: int, total_m: int):
        """
        Initialize coupled state.
        
        Args:
            particle1: First particle's angular momentum
            particle2: Second particle's angular momentum
            total_l: Total angular momentum quantum number
            total_m: Total magnetic quantum number
        """
        self.l1 = particle1.l
        self.l2 = particle2.l
        self.L = total_l
        self.M = total_m
        
        # Validate coupling rules
        if abs(self.l1 - self.l2) > self.L or self.L > self.l1 + self.l2:
            raise ValueError(f"Invalid coupling: L={self.L} not allowed for l1={self.l1}, l2={self.l2}")
    
    def expansion_coefficients(self) -> List[Tuple[int, int, float]]:
        """
        Get expansion coefficients in uncoupled basis.
        
        Returns:
            List of (m1, m2, coefficient) tuples
        """
        coefficients = []
        
        for m1 in range(-self.l1, self.l1 + 1):
            for m2 in range(-self.l2, self.l2 + 1):
                coeff = clebsch_gordan_coefficient(
                    self.l1, m1, self.l2, m2, self.L, self.M
                )
                if abs(coeff) > 1e-10:  # Only include non-zero coefficients
                    coefficients.append((m1, m2, coeff))
        
        return coefficients
    
    def measurement_probability(self, m1_measured: int, m2_measured: int) -> float:
        """
        Calculate probability of measuring specific m1 and m2 values.
        
        Args:
            m1_measured: Measured m1 value
            m2_measured: Measured m2 value
        
        Returns:
            Probability (between 0 and 1)
        """
        coeff = clebsch_gordan_coefficient(
            self.l1, m1_measured, self.l2, m2_measured, self.L, self.M
        )
        return abs(coeff) ** 2
    
    def __repr__(self) -> str:
        return f"CoupledState(l1={self.l1}, l2={self.l2}, L={self.L}, M={self.M})"
