def sir_derivatives(S, I, R, N, beta, gamma):
    """
    Persamaan diferensial model SIR
    """
    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return dS, dI, dR
