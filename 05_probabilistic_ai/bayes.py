# Simple Bayesian Probability Example
# P(A|B) = P(B|A)*P(A)/P(B)

def bayes(prior_a, prob_b_given_a, prob_b):
    return (prob_b_given_a * prior_a) / prob_b

# Example: Disease testing
# P(Disease) = 0.01, P(Test+|Disease) = 0.9, P(Test+) = 0.05
posterior = bayes(0.01, 0.9, 0.05)
print("Probability of having disease given positive test:", round(posterior, 2))
