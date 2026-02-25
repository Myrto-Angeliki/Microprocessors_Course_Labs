from utils import Menu, handle_pos_integer_input, parse_prob, FILE_PATH, GENA_DEFAULT_FILE, SortedCircuit
import matplotlib.pyplot as pypl
from .gena import genetic_algorithm
import sys

GENA_MENU_OPTIONS = ["1","2","3","4","5"]
RESULTS_PATH  = "C:\\Users\\user\\Desktop\\git_projects\\micropros\\Microprocessors_Course_Labs\\Lab4\\tests_results\\workload_max_score.txt"

class GenATests():
    def __init__(self, circuit_path):
        self.circuit = SortedCircuit()
        self.circuit.load_from_file(circuit_path)


    def find_best_param_value_index(self, scores_for_various_param_values):
        best_score = -1; best_indx = -1
        scores_len = len(scores_for_various_param_values)
        for i in range(scores_len):
            max_score_for_specific_param_value = max(scores_for_various_param_values[i])
            if max_score_for_specific_param_value > best_score: 
                best_score = max_score_for_specific_param_value
                best_indx = i
        return best_indx
    

    def calculate_scores_for_various_param_values(self, parameter_values, option, circuit, N, L, m, gens, opts = "a"):
        scores = []
        str_param = "- N" if option==1 else "m"
        print(f"\n\n-- Execution of the genetic algorithm ({gens} generations), for each {str_param} = {parameter_values}")
        for parameter_value in parameter_values:
            print(f"\n{str_param} = {parameter_value}")
            if   option == 1: scores.append(genetic_algorithm(circuit, parameter_value, L, m, gens, opts))
            elif option == 2: scores.append(genetic_algorithm(circuit, N, L, parameter_value, gens, opts))
            else: pass
        return scores
    
    
    def plot_various_param_tests(self, m, N, L, scores, mutation_percentages, population_sizes, gens_for_param_optmization):
        generations_p =  [ i for i in range(1, gens_for_param_optmization+1) ]
        generations = [generations_p, generations_p, [i for i in range(1,601)]]
        figure, axis = pypl.subplots(1, 3) 
        titles = [f"Max score for different m values (N=20, L={L})", 
                  f"Max score for different N values (m={m}, L={L})",
                  f"Max score for m={m}, N={N}, L={L}"]
        for i in range(3):
            for j in range(len(scores[i])):
                if   i == 0: label = f"m = {mutation_percentages[j]}"
                elif i == 1: label = f"N = {population_sizes[j]}"   
                else:  label = f"Run {(j+1)}"       
                axis[i].plot(generations[i], scores[i][j], label = label); axis[i].legend()
            axis[i].set_title(titles[i])
            axis[i].set_xlabel("Generation"); axis[i].set_ylabel("Max Switching Activity"); 
        figure.tight_layout(pad=2.0)
        pypl.show()


    def get_optimized_results(self, N, m, L=2, generations=600, num_of_execs=10):
        optimized_results = []
        print(f"\n\n-- Execution of {num_of_execs} genetic algorithm ({generations} generations, N={N}, m={m}, L={L}) runs")
        for i in range(num_of_execs):
            print(f"\n- Run {(i+1)}")
            optimized_results.append(genetic_algorithm(self.circuit, N, L, m, generations))
        return optimized_results


    def plot_generations_to_scores(self, gens, max_scores, N, L, m):
        generations = [ i for i in range(1,gens+1) ]
        pypl.plot(generations, max_scores)
        pypl.xlabel("Generation"); pypl.ylabel("Max Switching Activity"); pypl.title(f"Genetic Algorithm for N={N}, L={L}, m={m}")
        pypl.show()


    def execute_algorithm(self, N=25, L=2, m=0.08):        
        gens = handle_pos_integer_input("number of generations", "Only a positive integer is allowed as input.")
        max_scores = genetic_algorithm(self.circuit, N, L, m, gens, options="a")
        self.plot_generations_to_scores(gens, max_scores, N, L, m)


    def handle_option_four(self):
        print("Are you sure you want to clear the contents of workload_max_score.txt?")
        print("Enter 'y' if you want to proceed: ",end="")
        inpt = input().strip().lower()
        if inpt == "y":
            with open(RESULTS_PATH, "w") as f:
                f.write("")
                print("\nThe contents of file workload_max_score.txt have been cleared\n")
        else:
            print("\nDid not clear the contents of file workload_max_score.txt\n")


    def handle_option_three(self, population_sizes = [20, 25, 30, 35], mutation_percentages = [0.04,0.06,0.08,0.1]):
        gens_for_params = 100
        L = handle_pos_integer_input("workload size L", "The workload size L must be a positive integer")

        scores_for_various_m_values = self.calculate_scores_for_various_param_values(mutation_percentages, 2, self.circuit, 20, L, "", gens_for_params)
        m = mutation_percentages[self.find_best_param_value_index(scores_for_various_m_values)]
        
        scores_for_various_N_values = self.calculate_scores_for_various_param_values(population_sizes, 1, self.circuit, "", L, m, gens_for_params)
        N = population_sizes[self.find_best_param_value_index(scores_for_various_N_values)]
        
        optimized_results = self.get_optimized_results(N, m, L)
        
        scores = [scores_for_various_m_values, scores_for_various_N_values, optimized_results]
        self.plot_various_param_tests(m, N, L, scores, mutation_percentages, population_sizes, gens_for_params)
    
    
    def handle_option_two(self):
        N = handle_pos_integer_input("population size N", "Only a positive integer is allowed as input.")
        L = handle_pos_integer_input("workload size L", "Only a positive integer is allowed as input.")
        print(" Enter the mutation probability m: ", end="")
        m = parse_prob(input().strip())
        self.execute_algorithm(N, L, m)



class GenAMenu(Menu):
    def __init__(self, menu_options,  circuit_path = f"{FILE_PATH}{GENA_DEFAULT_FILE}"):
        super().__init__(menu_options)
        self.tests_i = GenATests(circuit_path)

    def handle_menu_option(self, option): 
        try:
            if   option == "1":   self.tests_i.execute_algorithm()
            elif option == "2":   self.tests_i.handle_option_two()
            elif option == "3":   self.tests_i.handle_option_three()
            elif option == "4":   self.tests_i.handle_option_four()
        except Exception as e: print(e)

    def display_menu(self):
        print("\n-------------------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t\tGenetic Algorithm Tests")
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print("| (1) Execute default test (N=25, L=2, m=0.08)                     -> Enter the number of generations                         |")
        print("| (2) Choose values for the parameters of the test                 -> Enter N, L, m, and the number of generations            |")
        print("| (3) Run tests for various values of m and N                      -> Enter L                                                 |")
        print("|                                                                     population_sizes     N = [20, 25, 30, 35]               |")
        print("|                                                                     mutation_percentages m = [0.04, 0.06, 0.08, 0.1]        |")
        print("| (4) Delete the contents of the max score file                    -> Enter 'y' to wipe the contents of workload_max_score.txt|")
        print(f"| ({self.menu_options[-1]}) Exit                                                                                                                    |")
        print("-------------------------------------------------------------------------------------------------------------------------------")


def main(argv):
    GenAMenu(GENA_MENU_OPTIONS).start_menu()

if __name__ == "__main__":
    main(sys.argv)