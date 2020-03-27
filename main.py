# Imports
import random
import pandas

# Constants
POPULATION_SIZE = 20
NUM_TYPES_COMP = 4
AMOUNT_IN_AID = 500000
MAX_ECO_FITNESS = 10

# Databases
amount_given = {0 : 0, 1 : 50000, 2 : 100000, 3 : 150000, 4 : 200000}
victims = pandas.read_csv('victims.csv')
victims = victims.values.tolist()
NUM_VICTIMS = len(victims)

# Auxiliary Functions for GA
def get_chromosome():
    chromosome = []
    for i in range(NUM_VICTIMS):
        chromosome.append(random.randint(0,NUM_TYPES_COMP))
    return chromosome

def cal_fitness(chromosome):
    num_beneficiary = 0
    sum_eco_fitness = 0
    num_srcitizens_kids = 0
    total_amount_given = 0
    for i in range(NUM_VICTIMS):
        if (chromosome[i] != 0):
            num_beneficiary += 1
            sum_eco_fitness += victims[i][2]
            if (victims[i][3] < 18 or victims[i][3] >= 60):
                num_srcitizens_kids += 1
            total_amount_given += amount_given[chromosome[i]]
    # Normalisation of variables
    total_amount_given = (total_amount_given * NUM_VICTIMS)/AMOUNT_IN_AID
    sum_eco_fitness = sum_eco_fitness/MAX_ECO_FITNESS
    return float((num_beneficiary + num_srcitizens_kids + total_amount_given)/(1+sum_eco_fitness))

class Individual:
    def __init__(self, chromosome=None):
        if chromosome is None:
            self.chromosome = get_chromosome()
        else :
            self.chromosome = chromosome
        self.fitness = cal_fitness(self.chromosome)
    # Operator overloading to sort according to fitness
    def __lt__(self, other):
        return self.fitness>other.fitness

def is_valid(chromosome):
    sum = 0
    for i in chromosome:
        sum += amount_given[i]
    if (sum <= AMOUNT_IN_AID):
        return True
    else :
        return False

def generate_initial_population():
    population = []
    i = 0
    while (i < POPULATION_SIZE):
        individual = Individual()
        if (is_valid(individual.chromosome)):
            population.append(individual)
            i += 1
    return population

def crossover (parent1, parent2):
    child_chromosome = []
    for i in range(NUM_VICTIMS):
        prob = random.randint(0,100)
        if (prob < 49):
            # Take gene from parent 1
            child_chromosome.append(parent1.chromosome[i])
        elif (prob <= 98):
            # Take gene from parent 2
            child_chromosome.append(parent2.chromosome[i])
        else :
            # Perform mutation
            child_chromosome.append(random.randint(0,4))
    return Individual(chromosome = child_chromosome)

def find_population_fitness(population):
    sum_fitness = 0
    for i in population:
        sum_fitness += i.fitness
    return float(sum_fitness/POPULATION_SIZE)


# Main function
def run_ga():
    generation = 0
    population = generate_initial_population()
    pvs_avg_fitness = 0
    new_avg_fitness = find_population_fitness(population)
    print("Generation: 0" + " Fitness: " + str(new_avg_fitness))
    while (abs(new_avg_fitness - pvs_avg_fitness) > 0.001):       
        population.sort()
        new_generation = []
        
        # Elitism, i.e, 10% of fittest population sent to next gen
        size = int(0.1 * POPULATION_SIZE)
        for i in range(size):
            new_generation.append(population[i])
        # Rest 90% formed by mating amongst the fittest 50%
        size = int(0.9 * POPULATION_SIZE)
        for i in range(size):
            r = random.randint(0,POPULATION_SIZE/2)
            parent1 = population[r]
            r = random.randint(0,POPULATION_SIZE/2)
            parent2 = population[r]
            new_generation.append(crossover(parent1, parent2))
        population = new_generation
        pvs_avg_fitness = new_avg_fitness
        new_avg_fitness = find_population_fitness(population)
        generation += 1
        print("Generation: " + str(generation) + " Fitness: " + str(new_avg_fitness))
    print("Solution chromosome: ")
    print(population[0].chromosome)

run_ga()





