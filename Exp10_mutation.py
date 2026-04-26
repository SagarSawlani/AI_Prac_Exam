import random

def to_binary(popl):
  binary_popl = []
  for chromosome in popl:
    binary_chromosome = []
    for gene in chromosome:
      binary_chromosome.append(format(int(gene), '04b'))

    binary_popl.append(binary_chromosome)

  return binary_popl

def mutation(popl, rate):
  mutated_popl = []
  for chromosome in popl:
    mutated_chromosome = []
    for gene in chromosome:
      mutated_gene = ''
      for bit in gene:
        if random.random() < (rate / 100):
          mutated_gene += '1' if bit == '0' else '0'
        else:
          mutated_gene += bit
      mutated_chromosome.append(mutated_gene)
    mutated_popl.append(mutated_chromosome)
  return mutated_popl

n = int(input("Enter population size: "))
population = []
for i in range(n):
  genes = input(f"Enter genes of chromosome {i + 1} (comma separated): ").split(',')
  population.append(genes)

print("Initial Binary Population: ")
binary_population = to_binary(population)
for chromosome in binary_population:
  print(''.join(chromosome))

mutation_rate = int(input("Enter Mutation Rate: "))
print("Population after Mutation:")
mutated_population = mutation(binary_population, mutation_rate)
for chromosome in mutated_population:
  print(''.join(chromosome))