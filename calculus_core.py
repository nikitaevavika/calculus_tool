import sympy as sp


def derivative(expression: str, variable: str) -> str:
    """
    Calculate the derivative of a mathematical expression with respect to a given variable.
    
    Parameters:
        expression: mathematical expression as a string
        variable: variable of differentiation
    
    Returns:
        String representation of the derivative or error message
    
    Examples:
        >>> derivative("x**2", "x")
        '2*x'
        
        >>> derivative("sin(x)", "x")
        'cos(x)'
        
        >>> derivative("x**2 + y**2", "x")
        '2*x'
        
        >>> derivative("invalid expression", "x")
        'Error: Invalid mathematical expression'
    """
    try:
        var = sp.Symbol(variable)
        
        expr = sp.sympify(expression)
        
        deriv = sp.diff(expr, var)
        
        return str(deriv)
        
    except Exception as e:
        return f"ошибка! неверное математическое выражение"
    

def partial_derivative(expression: str, variables: str) -> str:
    try:
        expr = sp.sympify(expression)
        result = []
        for var in variables.split():
            symbol = sp.Symbol(var)
            deriv = sp.diff(expr, symbol)
            result.append(f"d/d{var}: {deriv}")
        return "; ".join(result)
    except Exception:
        return "ошибка! неверное математическое выражение"
    

def integrate(expression: str, variable: str) -> str:
    try:
        var = sp.Symbol(variable)
        expr = sp.sympify(expression)
        integral = sp.integrate(expr, var)
        return str(integral)
    except Exception:
        return "ошибка! неверное математическое выражение"
    


def limit(expression: str, variable: str, point: str) -> str:
    try:
        var = sp.Symbol(variable)
        expr = sp.sympify(expression)
        lim = sp.limit(expr, var, point)
        return str(lim)
    except Exception:
        return "ошибка! неверное математическое выражениее"
    

def solve_equation(equation: str, variable: str) -> str:
    try:
        var = sp.Symbol(variable)
        eq = sp.sympify(equation)
        solutions = sp.solve(eq, var)
        return str(solutions)
    except Exception:
        return "ошибка! неверное математическое выражение"
    

if __name__ == "__main__":
    test_cases = [
        ("x**2", "x"),
        ("sin(x)", "x"),
        ("x**3 + 2*x**2 - 5*x + 1", "x"),
        ("cos(x)", "x"),
        ("exp(x)", "x"),
        ("log(x)", "x"),
        ("x*y + y**2", "x"),  
        ("x**2 + y**2", "y"),  
        ("invalid expression", "x"),  
        ("1/(x+1)", "x"),  
    ]

    print("Тестирование модуля calculus_core")
    print("=" * 50)
    
    for expr, var in test_cases:
        result = derivative(expr, var)
        print(f"Производная {expr} по {var}: {result}")