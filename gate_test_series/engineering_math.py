#engineering_math.py

questions = {
    "easy": [
        {
            "id": 1,
            "q": "What is the derivative of f(x) = x^n?",
            "options": ["nx^(n-1)", "n^x", "x^(n+1)/(n+1)", "nx^n"],
            "correct": "nx^(n-1)"
        },
        {
            "id": 2,
            "q": "What is the value of log(1) for any base b > 0?",
            "options": ["1", "e", "0", "Infinity"],
            "correct": "0"
        },
        {
            "id": 3,
            "q": "A matrix A is called symmetric if:",
            "options": ["A = -A", "A = A^T", "det(A) = 0", "A is a identity matrix"],
            "correct": "A = A^T"
        },
        {
            "id": 4,
            "q": "The mean of the numbers 5, 10, 15, 20 is:",
            "options": ["10", "12.5", "15", "11.5"],
            "correct": "12.5"
        },
        {
            "id": 5,
            "q": "What is the value of cos(0°)?",
            "options": ["0", "0.5", "1", "-1"],
            "correct": "1"
        },
        {
            "id": 6,
            "q": "If two events A and B are independent, P(A ∩ B) is equal to:",
            "options": ["P(A) + P(B)", "P(A) / P(B)", "P(A) * P(B)", "P(A) - P(B)"],
            "correct": "P(A) * P(B)"
        },
        {
            "id": 7,
            "q": "What is the integral of 1/x dx?",
            "options": ["x", "ln|x| + C", "e^x", "-1/x^2"],
            "correct": "ln|x| + C"
        },
        {
            "id": 8,
            "q": "The Rank of an Identity Matrix of order n is:",
            "options": ["0", "1", "n-1", "n"],
            "correct": "n"
        },
        {
            "id": 9,
            "q": "Which of the following is a unit vector?",
            "options": ["[1, 1]", "[0.5, 0.5]", "[1, 0]", "[1, -1]"],
            "correct": "[1, 0]"
        },
        {
            "id": 10,
            "q": "The value of the determinant of a matrix with two identical rows is:",
            "options": ["1", "The value of the row", "0", "Undefined"],
            "correct": "0"
        }
    ],
    "medium": [
        {
            "id": 11,
            "q": "What is the Eigenvalue of the matrix [[1, 0], [0, 2]]?",
            "options": ["0 and 1", "1 and 2", "1 and 1", "2 and 2"],
            "correct": "1 and 2"
        },
        {
            "id": 12,
            "q": "The Central Limit Theorem states that the distribution of sample means approaches:",
            "options": ["Binomial Distribution", "Poisson Distribution", "Normal Distribution", "Uniform Distribution"],
            "correct": "Normal Distribution"
        },
        {
            "id": 13,
            "q": "Which of these is the formula for the Taylor Series of f(x) centered at a?",
            "options": ["Σ f'(a)(x-a)", "Σ f(n)(a)/n! * (x-a)^n", "Σ f(n)(x)/n!", "Σ (x-a)^n"],
            "correct": "Σ f(n)(a)/n! * (x-a)^n"
        },
        {
            "id": 14,
            "q": "In a Normal Distribution, approximately what percentage of data falls within 1 standard deviation?",
            "options": ["50%", "95%", "68%", "99.7%"],
            "correct": "68%"
        },
        {
            "id": 15,
            "q": "The dot product of two perpendicular vectors is:",
            "options": ["1", "-1", "Infinity", "0"],
            "correct": "0"
        },
        {
            "id": 16,
            "q": "What is the result of the Laplace transform of 1?",
            "options": ["s", "1/s", "s^2", "1/s^2"],
            "correct": "1/s"
        },
        {
            "id": 17,
            "q": "If A is a 3x3 matrix and det(A) = 5, what is det(2A)?",
            "options": ["10", "30", "40", "80"],
            "correct": "40"
        },
        {
            "id": 18,
            "q": "What is the Gradient of the function f(x, y) = x^2 + y^2?",
            "options": ["[2x, 2y]", "[x, y]", "[2, 2]", "[x^2, y^2]"],
            "correct": "[2x, 2y]"
        },
        {
            "id": 19,
            "q": "The probability of getting exactly 2 heads in 3 tosses of a fair coin is:",
            "options": ["1/8", "3/8", "1/2", "3/4"],
            "correct": "3/8"
        },
        {
            "id": 20,
            "q": "The Divergence of a curl of any vector field is always:",
            "options": ["1", "The vector field itself", "0", "Infinity"],
            "correct": "0"
        }
    ],
    "hard": [
        {
            "id": 21,
            "q": "In SVD (Singular Value Decomposition) A = UΣV^T, the columns of U are:",
            "options": ["Eigenvectors of A", "Left singular vectors", "Right singular vectors", "Eigenvalues"],
            "correct": "Left singular vectors"
        },
        {
            "id": 22,
            "q": "Which method is used to find the maximum or minimum of a function subject to equality constraints?",
            "options": ["Newton-Raphson", "Lagrange Multipliers", "Simplex Method", "Least Squares"],
            "correct": "Lagrange Multipliers"
        },
        {
            "id": 23,
            "q": "The Hessian matrix is a square matrix of:",
            "options": ["First-order partial derivatives", "Second-order partial derivatives", "Eigenvalues", "Singular values"],
            "correct": "Second-order partial derivatives"
        },
        {
            "id": 24,
            "q": "What is the probability that a standard normal variable Z is greater than 0?",
            "options": ["0.25", "0.5", "1.0", "0.95"],
            "correct": "0.5"
        },
        {
            "id": 25,
            "q": "In the context of optimization, if the Hessian is positive definite, the point is a:",
            "options": ["Local Maximum", "Local Minimum", "Saddle Point", "Inflexion Point"],
            "correct": "Local Minimum"
        },
        {
            "id": 26,
            "q": "What is the Jacobian of the transformation from Cartesian (x, y) to Polar (r, θ)?",
            "options": ["1", "r", "r^2", "sin(θ)"],
            "correct": "r"
        },
        {
            "id": 27,
            "q": "Which of these represents the Cauchy-Schwarz Inequality?",
            "options": ["|a·b| ≤ ||a|| ||b||", "|a+b| ≤ |a| + |b|", "a^2 + b^2 = c^2", "det(AB) = det(A)det(B)"],
            "correct": "|a·b| ≤ ||a|| ||b||"
        },
        {
            "id": 28,
            "q": "A Markov chain is called 'Ergodic' if it is:",
            "options": ["Absorbing", "Periodic", "Irreducible and Aperiodic", "Finite"],
            "correct": "Irreducible and Aperiodic"
        },
        {
            "id": 29,
            "q": "What is the value of the Gamma function Γ(1/2)?",
            "options": ["1", "√π", "π", "1/2"],
            "correct": "√π"
        },
        {
            "id": 30,
            "q": "The Power of a Statistical Test is defined as:",
            "options": ["1 - Alpha", "1 - Beta", "Alpha + Beta", "Beta - Alpha"],
            "correct": "1 - Beta"
        }
    ]
}