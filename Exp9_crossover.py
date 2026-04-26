import random
import math

def to_binary(chromosome):
  binary_chromosome = []
  for gene in chromosome:
    binary_gene = format(int(gene), '04b')
    binary_chromosome.append(binary_gene)
  return binary_chromosome

def crossover(popl, crossover_rate):
  parents = random.sample(popl, math.ceil((crossover_rate / 100) * len(popl)))

  # Single Point Crossover
  point = random.randint(1, len(parents[0]) - 1)

  child1 = parents[0][:point] + parents[1][point:]
  child2 = parents[1][:point] + parents[0][point:]

  return parents, point, child1, child2

population = []
n = int(input("Enter population size: "))
print("Enter Initial Population")
for i in range(n):
  genes = input(f"Enter genes for chromosome {i + 1} (comma separated): ").split(',')
  population.append(genes)

binary_population = [to_binary(chromosome) for chromosome in population]
print("Initial Binary Population:")
for chromosome in binary_population:
  print(''.join(chromosome))

crossover_rate = int(input("Enter Crossover Rate: "))
parents, point, child1, child2 = crossover(binary_population, crossover_rate)

print("Selected Parents:")
print(''.join(parents[0]))
print(''.join(parents[1]))

print("Crossover Point: ", point)

print("Children:")
print(''.join(child1))
print(''.join(child2))