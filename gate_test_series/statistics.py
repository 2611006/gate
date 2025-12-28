# statistics.py

questions = {
    "easy": [
        {"q": "The sum of deviations of a set of observations from their Mean is always:", "options": ["Positive", "Negative", "Zero", "One"], "correct": "Zero"},
        {"q": "Which of the following is a measure of central tendency?", "options": ["Standard Deviation", "Range", "Mode", "Variance"], "correct": "Mode"},
        {"q": "The probability of an event lies between:", "options": ["-1 and 1", "0 and 1", "0 and 100", "None"], "correct": "0 and 1"},
        {"q": "The middle value of an ordered data set is known as:", "options": ["Mean", "Median", "Mode", "Variance"], "correct": "Median"},
        {"q": "Standard Deviation is the square root of:", "options": ["Range", "Mean Deviation", "Variance", "Mode"], "correct": "Variance"},
        {"q": "For a symmetric distribution, Mean, Median, and Mode are:", "options": ["Different", "Equal", "Reciprocals", "Zero"], "correct": "Equal"},
        {"q": "The probability of drawing an Ace from a deck of 52 cards is:", "options": ["1/52", "1/13", "4/13", "1/4"], "correct": "1/13"},
        {"q": "Which distribution is often called the 'Bell Curve'?", "options": ["Poisson", "Binomial", "Normal", "Exponential"], "correct": "Normal"},
        {"q": "The range of a dataset is the difference between:", "options": ["Mean and Median", "Max and Min", "First and Third Quartile", "Variance and SD"], "correct": "Max and Min"},
        {"q": "A collection of all possible outcomes of an experiment is called:", "options": ["Event", "Sample Space", "Population", "Frequency"], "correct": "Sample Space"}
    ],
    "medium": [
        {"q": "In a Binomial distribution, if n=10 and p=0.5, what is the Mean?", "options": ["2.5", "5", "10", "1"], "correct": "5"},
        {"q": "The relationship between Mean, Median, and Mode for a moderately skewed distribution is:", "options": ["Mode = 3 Median - 2 Mean", "Mean = 3 Median - 2 Mode", "Median = 3 Mean - 2 Mode", "Mode = 3 Mean - 2 Median"], "correct": "Mode = 3 Median - 2 Mean"},
        {"q": "Which of the following distributions is used to model the number of events in a fixed interval of time?", "options": ["Normal", "Binomial", "Poisson", "Uniform"], "correct": "Poisson"},
        {"q": "If the correlation coefficient r = 1, it indicates:", "options": ["No correlation", "Perfect negative correlation", "Perfect positive correlation", "Weak correlation"], "correct": "Perfect positive correlation"},
        {"q": "The probability of a Type I error is denoted by:", "options": ["Alpha", "Beta", "Gamma", "Delta"], "correct": "Alpha"},
        {"q": "In a Normal distribution, what percentage of data falls within 1 Standard Deviation of the Mean?", "options": ["50%", "68%", "95%", "99.7%"], "correct": "68%"},
        {"q": "The Coefficient of Variation is calculated as:", "options": ["(Mean/SD) * 100", "(SD/Mean) * 100", "(Variance/Mean) * 100", "(SD/Median) * 100"], "correct": "(SD/Mean) * 100"},
        {"q": "Which test is used to check the goodness of fit?", "options": ["t-test", "z-test", "Chi-square test", "f-test"], "correct": "Chi-square test"},
        {"q": "If P(A) = 0.3 and P(B) = 0.4, and A and B are independent, what is P(A ∩ B)?", "options": ["0.7", "0.12", "0.1", "0.5"], "correct": "0.12"},
        {"q": "The square of the standard deviation is called:", "options": ["Covariance", "Variance", "Kurtosis", "Skewness"], "correct": "Variance"}
    ],
    "hard": [
        {"q": "If the probability density function (PDF) of a random variable is f(x) = kx for 0 < x < 1, what is the value of k?", "options": ["1", "2", "0.5", "4"], "correct": "2"},
        {"q": "In hypothesis testing, the 'Power of a Test' is defined as:", "options": ["1 - Alpha", "1 - Beta", "Alpha + Beta", "Beta - Alpha"], "correct": "1 - Beta"},
        {"q": "For a Poisson distribution, if the Mean is 4, what is the Variance?", "options": ["2", "4", "16", "8"], "correct": "4"},
        {"q": "What is the skewness of a Normal distribution?", "options": ["1", "0", "-1", "Infinity"], "correct": "0"},
        {"q": "Which distribution is used for testing the equality of variances of two populations?", "options": ["t-distribution", "F-distribution", "z-distribution", "Binomial"], "correct": "F-distribution"},
        {"q": "The Central Limit Theorem states that as sample size increases, the sampling distribution of the mean approaches:", "options": ["Binomial", "Poisson", "Normal", "Uniform"], "correct": "Normal"},
        {"q": "In Simple Linear Regression, if the slope is 0.5 and the correlation is 0.8, what is the R-squared value?", "options": ["0.4", "0.25", "0.64", "0.8"], "correct": "0.64"},
        {"q": "A random variable X has Mean 10 and Variance 25. What is the Mean of Y = 2X + 5?", "options": ["20", "25", "30", "15"], "correct": "25"},
        {"q": "If X and Y are independent random variables, then Var(X - Y) is equal to:", "options": ["Var(X) - Var(Y)", "Var(X) + Var(Y)", "Var(X) + Var(Y) - 2Cov(X,Y)", "Var(X)"], "correct": "Var(X) + Var(Y)"},
        {"q": "The probability that a continuous random variable takes a specific exact value is always:", "options": ["0.5", "1", "0", "Depends on the PDF"], "correct": "0"}
    ]
}