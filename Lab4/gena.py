import random
from utils import GENA_WRITE_PATH
from tqdm import tqdm

def write_results_to_file(file_path, options, parents, best_score, N, L, m, generations):
    f = open(file_path, options)
    f.write(f"N = {N}, L = {L}, m = {m}, generations = {generations}")
    f.write(f"\ntest score: {best_score}\n")
    f.write(f"- best individual workload:\n  {str(parents[0])}\n")
    f.write(f"- second best individual workload:\n  {str(parents[1])}\n\n")
    f.close()


def mutate(population, parents_indexes, N, m):
    mutated_population = []
    for indx in range(N):
        workload = population[indx]
        if indx in parents_indexes:  
            mutated_population.append(workload) 
            continue
        mutated_workload = []
        for vector in workload:
            mutated_vector = []
            for input in vector:
                rand = random.random()
                if rand >= m:  mutated_vector.append(input)
                else:       mutated_vector.append((1-input))
            mutated_workload.append(mutated_vector)
        mutated_population.append(mutated_workload)           
    return mutated_population


def crossover(parents, L):
    if L < 2: L = 2
    workload = []
    C = random.randint(0,1)
    R = random.randint(1,(L-1))
    workload += parents[C][:R]
    workload += parents[1-C][R:]
    return workload


def generate_children(population, parents, parents_indexes, m, L, N):
    new_population = []
    for i in range(N):
        if i in parents_indexes:
            new_population.append(population[i])
            continue
        new_population.append(crossover(parents, L))           
    new_population = mutate(new_population, parents_indexes, N, m)
    return new_population


def is_not_same_workload_as_best(current_workload, best_workload):
    for vector_cw, vector_bw in zip(current_workload, best_workload):
        for input_cwv, input_vbw in zip(vector_cw, vector_bw):
            if input_cwv != input_vbw:  return True
    return False


def swap_scores(new_best, best, second_best):
    second_best["score"] = best["score"]
    second_best["index"] = best["index"]
    best["score"] = new_best[0]
    best["index"] = new_best[1]


def select_parents(scores, population, N):
    best = {"score": -1, "index": -1}
    second_best = {"score": -1, "index": -1}
    for indx in range(N):
        score = scores[indx]
        if score > best["score"]:
            swap_scores([score,indx], best, second_best)
        elif score > second_best["score"]:
            if is_not_same_workload_as_best(population[indx], population[best["index"]]):
                second_best["score"] = score
                second_best["index"] = indx       
    parent1 = population[best["index"]]
    parent2 = population[second_best["index"]]
    return [parent1, parent2], [best["index"], second_best["index"]]


def apply_individual_workload_on_circuit(circuit, workload_i):
    circuit.apply_input_vector(workload_i[0])
    switches = 0
    for vector in workload_i[1:]:
        circuit.apply_input_vector(vector)
        switches += circuit.count_switches()
    return switches


def generate_random_workload(num_of_inputs, L):
    new_workload = []
    if L >= 2:
        for i in range(L):
            inputs = [random.randint(0,1) for x in range(num_of_inputs) ] 
            new_workload.append(inputs)
    return new_workload


def get_workload(circuit, L, create_new_population, population, indx=-1):
    if create_new_population: workload_i = generate_random_workload(len(circuit.top_inputs), L)
    else:                     workload_i = population[indx]
    return workload_i

def apply_individual_workloads(circuit, L, N, population):
    score = []
    create_new_population = (population == [])
    for i in range(N):
        workload_i = get_workload(circuit, L, create_new_population, population, i)
        if create_new_population: population.append(workload_i)
        switches = apply_individual_workload_on_circuit(circuit, workload_i)
        score.append(switches)
    return score, population


def genetic_algorithm(circuit, N, L, m, generations, options="a"):
    scores = []
    population = []
    for j in tqdm(range(generations)):
        if j != 0: score_i, _ = apply_individual_workloads(circuit, L, N, population) 
        else:      score_i, population = apply_individual_workloads(circuit, L, N, []) 
        parents, parentIndexes = select_parents(score_i, population, N)
        population = generate_children(population, parents, parentIndexes, m, L, N)
        scores.append(max(score_i))
    write_results_to_file(GENA_WRITE_PATH, options, parents, max(scores), N, L, m , generations)
    return scores