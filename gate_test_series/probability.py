# probability.py

questions = {
    "easy": [
        {"q": "The probability of an event E is P(E). What is the range of P(E)?", "options": ["-1 to 1", "0 to 1", "0 to 100", "Any real number"], "correct": "0 to 1"},
        {"q": "The sum of the probabilities of all outcomes in a sample space is:", "options": ["0", "0.5", "1", "Depends on outcomes"], "correct": "1"},
        {"q": "If P(A) = 0.4, what is the probability of the complement of A?", "options": ["0.4", "0.6", "1.4", "0"], "correct": "0.6"},
        {"q": "A fair die is rolled. What is the probability of getting a 4?", "options": ["1/2", "1/4", "1/6", "4/6"], "correct": "1/6"},
        {"q": "Two events are mutually exclusive if:", "options": ["P(A ∩ B) = 1", "P(A ∪ B) = 0", "P(A ∩ B) = 0", "P(A) = P(B)"], "correct": "P(A ∩ B) = 0"},
        {"q": "Which distribution is used for 'Success' or 'Failure' experiments?", "options": ["Normal", "Poisson", "Bernoulli", "Uniform"], "correct": "Bernoulli"},
        {"q": "The probability of an impossible event is:", "options": ["1", "0.5", "0", "-1"], "correct": "0"},
        {"q": "A fair coin is tossed twice. What is the probability of getting two heads?", "options": ["0.5", "0.25", "0.75", "1"], "correct": "0.25"},
        {"q": "If two events are independent, P(A ∩ B) is:", "options": ["P(A) + P(B)", "P(A) * P(B)", "P(A) / P(B)", "0"], "correct": "P(A) * P(B)"},
        {"q": "In a fair coin toss, the probability of getting at least one head in two tosses is:", "options": ["0.5", "0.25", "0.75", "1"], "correct": "0.75"}
    ],
    "medium": [
        {"q": "A box contains 3 red and 2 blue balls. If 2 balls are drawn without replacement, what is the probability both are red?", "options": ["3/10", "6/25", "3/5", "1/5"], "correct": "3/10"},
        {"q": "What is the probability of getting a sum of 7 when rolling two dice?", "options": ["1/6", "1/12", "1/36", "7/36"], "correct": "1/6"},
        {"q": "In a Binomial distribution, Mean = 6 and Variance = 2.4. What is the value of 'p'?", "options": ["0.4", "0.6", "0.2", "0.8"], "correct": "0.6"},
        {"q": "Bayes' Theorem is primarily used to calculate:", "options": ["Joint Probability", "Marginal Probability", "Posterior Probability", "Likelihood only"], "correct": "Posterior Probability"},
        {"q": "The variance of a Binomial distribution is given by:", "options": ["np", "npq", "n/p", "sqrt(npq)"], "correct": "npq"},
        {"q": "If P(A|B) = P(A), then events A and B are:", "options": ["Mutually Exclusive", "Independent", "Dependent", "Exhaustive"], "correct": "Independent"},
        {"q": "Expectation E[X] for a discrete random variable is calculated as:", "options": ["Σ X", "Σ P(X)", "Σ X * P(X)", "Max(X)"], "correct": "Σ X * P(X)"},
        {"q": "What is the Mean of a Poisson distribution with parameter λ?", "options": ["λ^2", "sqrt(λ)", "λ", "1/λ"], "correct": "λ"},
        {"q": "Area under the PDF curve for a continuous random variable is:", "options": ["0.5", "1", "Variable", "0"], "correct": "1"},
        {"q": "Which distribution is appropriate for modeling the 'time until the next event'?", "options": ["Normal", "Poisson", "Exponential", "Binomial"], "correct": "Exponential"}
    ],
    "hard": [
        {"q": "If X is a normal variable with mean μ and variance σ², what is E[X²]?", "options": ["μ²", "σ²", "μ² + σ²", "2μ"], "correct": "μ² + σ²"},
        {"q": "Two dice are rolled. Given the sum is 8, what is the probability that at least one die is a 3?", "options": ["2/5", "1/5", "1/6", "2/36"], "correct": "2/5"},
        {"q": "If P(A) = 0.3 and P(B) = 0.4, and A and B are independent, P(A ∪ B) is:", "options": ["0.7", "0.58", "0.12", "0.8"], "correct": "0.58"},
        {"q": "The Moment Generating Function (MGF) of a Normal distribution is related to:", "options": ["Mean only", "Variance only", "Both Mean and Variance", "Neither"], "correct": "Both Mean and Variance"},
        {"q": "A random variable X has PDF f(x) = 3x² for 0 < x < 1. What is P(X < 0.5)?", "options": ["1/2", "1/4", "1/8", "1/16"], "correct": "1/8"},
        {"q": "The variance of a Uniform distribution in the range [a, b] is:", "options": ["(b-a)/2", "(b-a)²/12", "(b+a)/2", "(b-a)/12"], "correct": "(b-a)²/12"},
        {"q": "The memoryless property is a unique characteristic of which distribution?", "options": ["Normal", "Poisson", "Exponential", "Binomial"], "correct": "Exponential"},
        {"q": "Joint PDF of X and Y is f(x,y). X and Y are independent if and only if f(x,y) equals:", "options": ["f(x) + f(y)", "f(x) * f(y)", "f(x) / f(y)", "1"], "correct": "f(x) * f(y)"},
        {"q": "Chebyshev's inequality provides a bound on:", "options": ["The Mean", "Tail probabilities", "The Median", "The Mode"], "correct": "Tail probabilities"},
        {"q": "If X ~ Poisson(λ1) and Y ~ Poisson(λ2) are independent, then X + Y follows:", "options": ["Normal Distribution", "Poisson(λ1 + λ2)", "Binomial Distribution", "Bernoulli Distribution"], "correct": "Poisson(λ1 + λ2)"}
    ]
}