# linear_algebra.py

questions = {
    "easy": [
        {"q": "What is the determinant of an Identity matrix of any order?", "options": ["0", "n", "1", "-1"], "correct": "1"},
        {"q": "A square matrix A is said to be singular if its determinant is:", "options": ["1", "0", "Positive", "Negative"], "correct": "0"},
        {"q": "The trace of a matrix is the sum of its:", "options": ["Rows", "Columns", "Eigenvalues", "Determinants"], "correct": "Eigenvalues"},
        {"q": "If A is a 3x3 matrix and |A| = 5, then what is |2A|?", "options": ["10", "20", "40", "30"], "correct": "40"},
        {"q": "A matrix where all elements above the main diagonal are zero is called:", "options": ["Upper Triangular", "Lower Triangular", "Diagonal", "Identity"], "correct": "Lower Triangular"},
        {"q": "What is the rank of a 3x3 identity matrix?", "options": ["1", "2", "3", "0"], "correct": "3"},
        {"q": "If A is a symmetric matrix, then:", "options": ["A = -A^T", "A = A^T", "A = A^-1", "det(A) = 0"], "correct": "A = A^T"},
        {"q": "The product of the eigenvalues of a matrix is equal to its:", "options": ["Trace", "Rank", "Determinant", "Inverse"], "correct": "Determinant"},
        {"q": "Two vectors are orthogonal if their dot product is:", "options": ["1", "0", "-1", "Infinity"], "correct": "0"},
        {"q": "If A is an orthogonal matrix, then AA^T is equal to:", "options": ["0", "A", "I", "A^-1"], "correct": "I"}
    ],
    "medium": [
        {"q": "What are the eigenvalues of the matrix [[1, 2], [0, 4]]?", "options": ["1, 0", "2, 4", "1, 4", "1, 2"], "correct": "1, 4"},
        {"q": "If a 3x3 matrix has rank 2, how many solutions does Ax=0 have?", "options": ["Unique solution", "No solution", "Infinitely many solutions", "Exactly two solutions"], "correct": "Infinitely many solutions"},
        {"q": "For which value of 'k' is the vector [1, k, 5] a linear combination of [1, 0, 0] and [0, 1, 0]?", "options": ["5", "0", "No value of k", "Any value of k"], "correct": "No value of k"},
        {"q": "If A is a 4x4 matrix and Rank(A) = 2, what is the Nullity of A?", "options": ["0", "2", "4", "6"], "correct": "2"},
        {"q": "If the eigenvalues of A are 2 and 3, what are the eigenvalues of A^2?", "options": ["2, 3", "4, 6", "4, 9", "sqrt(2), sqrt(3)"], "correct": "4, 9"},
        {"q": "The system of equations Ax=B has a unique solution if:", "options": ["Rank(A) < Rank(A|B)", "Rank(A) = Rank(A|B) = number of variables", "Rank(A) = 0", "det(A) = 0"], "correct": "Rank(A) = Rank(A|B) = number of variables"},
        {"q": "If A is a skew-symmetric matrix of order 3, its determinant is always:", "options": ["1", "-1", "0", "Non-zero"], "correct": "0"},
        {"q": "A basis of a vector space must be:", "options": ["Linearly Dependent", "Orthogonal only", "Linearly Independent and Span the space", "Unit vectors only"], "correct": "Linearly Independent and Span the space"},
        {"q": "What is the inverse of a diagonal matrix with entries 2, 4, 8?", "options": ["Diagonal with 2, 4, 8", "Diagonal with 1/2, 1/4, 1/8", "Diagonal with -2, -4, -8", "Does not exist"], "correct": "Diagonal with 1/2, 1/4, 1/8"},
        {"q": "The characteristic equation of a matrix A is |A - λI| = 0. If λ=0 is an eigenvalue, then:", "options": ["A is invertible", "A is non-singular", "A is singular", "A is an identity matrix"], "correct": "A is singular"}
    ],
    "hard": [
        {"q": "If A is a 3x3 matrix with eigenvalues 1, -1, 0, then the rank of A is:", "options": ["0", "1", "2", "3"], "correct": "2"},
        {"q": "The Cayley-Hamilton theorem states that every square matrix satisfies its own:", "options": ["Eigenvector", "Determinant", "Characteristic equation", "Rank"], "correct": "Characteristic equation"},
        {"q": "If A is an idempotent matrix (A^2 = A), what are its possible eigenvalues?", "options": ["0 or 1", "Any real number", "Only 1", "Only 0"], "correct": "0 or 1"},
        {"q": "Two matrices A and B are similar if there exists an invertible matrix P such that:", "options": ["B = PAP", "B = P^-1AP", "B = AP", "B = P^TA P"], "correct": "B = P^-1AP"},
        {"q": "The algebraic multiplicity of an eigenvalue is always:", "options": ["Equal to geometric multiplicity", "Less than or equal to geometric multiplicity", "Greater than or equal to geometric multiplicity", "One"], "correct": "Greater than or equal to geometric multiplicity"},
        {"q": "If A is a 3x3 matrix with eigenvalues 1, 2, 3, what is the trace of A^-1?", "options": ["6", "11/6", "1", "0"], "correct": "11/6"},
        {"q": "A linear transformation is represented by a 3x2 matrix. The dimension of the codomain is:", "options": ["2", "3", "6", "5"], "correct": "3"},
        {"q": "If V is a vector space of dimension n, any set of n+1 vectors in V is:", "options": ["A basis", "Linearly Independent", "Linearly Dependent", "Orthogonal"], "correct": "Linearly Dependent"},
        {"q": "What is the maximum number of linearly independent eigenvectors of an nxn matrix with n distinct eigenvalues?", "options": ["1", "n-1", "n", "Infinite"], "correct": "n"},
        {"q": "If the determinant of a 3x3 matrix is 12 and two eigenvalues are 2 and 3, the third eigenvalue is:", "options": ["7", "2", "6", "1"], "correct": "2"}
    ]
}