import numpy as np
from src.sir_model import sir_derivatives

def rk4_sir(beta, gamma, S0, I0, R0, days):
    """
    Simulasi SIR menggunakan metode Runge-Kutta orde 4
    """
    S = np.zeros(days)
    I = np.zeros(days)
    R = np.zeros(days)

    S[0], I[0], R[0] = S0, I0, R0
    N = S0 + I0 + R0
    dt = 1.0

    for t in range(days - 1):
        k1 = sir_derivatives(S[t], I[t], R[t], N, beta, gamma)
        k2 = sir_derivatives(
            S[t] + dt * k1[0] / 2,
            I[t] + dt * k1[1] / 2,
            R[t] + dt * k1[2] / 2,
            N, beta, gamma
        )
        k3 = sir_derivatives(
            S[t] + dt * k2[0] / 2,
            I[t] + dt * k2[1] / 2,
            R[t] + dt * k2[2] / 2,
            N, beta, gamma
        )
        k4 = sir_derivatives(
            S[t] + dt * k3[0],
            I[t] + dt * k3[1],
            R[t] + dt * k3[2],
            N, beta, gamma
        )

        S[t + 1] = S[t] + dt * (k1[0] + 2*k2[0] + 2*k3[0] + k4[0]) / 6
        I[t + 1] = I[t] + dt * (k1[1] + 2*k2[1] + 2*k3[1] + k4[1]) / 6
        R[t + 1] = R[t] + dt * (k1[2] + 2*k2[2] + 2*k3[2] + k4[2]) / 6

    return S, I, R
