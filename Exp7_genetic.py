import random

# Create Initial Population
def create_chromosome():
  chromosomes = []
  for i in range(4):
    chromosomes.append(random.randint(0,10))

  return chromosomes

population = [create_chromosome() for i in range(6)]

print("Initial Population:", population)

# Calculate Fitness
def fitness(chromosome):
  a, b, c, d = chromosome
  return abs((a + 2*b + 3*c + 4*d) - 30)

# Selection
population = sorted(population, key=fitness)
print(population)

parents = population[:2] # best 2

# Crossover
def crossover(p1, p2):
  point = random.randint(1, 3) # 1 to 3 to avoid cutting at ends
  child = p1[:point] + p2[point:]
  return child

# Mutation
def mutation(chromosome):
  index = random.randint(0, 3) # pick a random gene
  chromosome[index] = random.randint(0, 10)
  return chromosome

# New Population
new_population = []
for parent in parents:
  new_population.append(parent)

while len(new_population) < 6:
  child = crossover(parents[0], parents[1])
  child = mutation(child)
  new_population.append(child)

print("Final Population:", new_population)

# Best Chromosome 
new_population = sorted(new_population, key=fitness)
print("Best Chromosome: ", new_population[0])
print("Fitness: ", fitness(new_population[0]))