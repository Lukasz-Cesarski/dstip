# QUESTION 1
mean_population = states_pop.mean()
print(f"1. Mean population per state equals {mean_population}")

# QUESTION 2
mean_population_mask = states_pop < mean_population
states_pop_below_mean = states_pop[mean_population_mask]
print("2. There is {}/{} states with the population below mean."
      .format(len(states_pop_below_mean), len(states_pop)))

# QUESTION 3
print(
"""3. Standard deviation for:
   All states                   = {:12.2f}
   states below mean population = {:12.2f}
   states above mean population = {:12.2f}""".format(
    states_pop.std(),
    states_pop[mean_population_mask].std(),
    states_pop[~mean_population_mask].std(),
))
