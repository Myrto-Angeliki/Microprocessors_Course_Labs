from utils.spNGate import evaluate_sp_function
from utils.MCFunctions import MCGate
from utils.Element import Element

def display_outputs(signals_table, element, input_vector, circuit_outputs, display_all_outputs):
    wire_names = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f"}
    if (element.output in circuit_outputs) or display_all_outputs:
        output_name = wire_names[element.output]
        print(f"[a,b,c] = {input_vector}, {output_name} = {signals_table[element.output]: .3f}")


def process(element, signals_table):
    signal_probabilities_of_inputs = []
    for input in element.inputs:
        signal_probabilities_of_inputs.append(signals_table[input])
    signals_table[element.output] = evaluate_sp_function(element.element_type, signal_probabilities_of_inputs, 0)


def init_top_inputs(signals_table, top_inputs, input_vector):
    for j in range(len(top_inputs)):
        signals_table[top_inputs[j]] = input_vector[j]


def apply_inputs_to_circuit(signals_table, top_inputs, input_vector, elements, circuit_outputs, display_all_outputs=False):
    init_top_inputs(signals_table, top_inputs, input_vector)
    for element in elements:
        process(element, signals_table)
        display_outputs(signals_table, element, input_vector, circuit_outputs, display_all_outputs)      


def get_circuit_outputs(elements):
    elements_inputs = [input for element in elements for input in element.inputs]
    circuit_outputs = []
    for element in elements:
        if element.output not in elements_inputs: circuit_outputs.append(element.output)
    return circuit_outputs


def get_top_inputs(elements):
    elementsOutput = [x.output for x in elements]
    top_inputs = [x for x in range(6) if x not in elementsOutput]
    return top_inputs


def main():
    signals_table = [0.0 for i in range(6)]
    e1 = Element("AND",[0,1],4)
    e2 = Element("NOT",[2],5)
    e3 = Element("AND",[4,5],3)
    elements = [e1,e2,e3]
    top_inputs = get_top_inputs(elements)
    circuit_outputs = get_circuit_outputs(elements)
    input_vectors =[[0,0,0],
                    [0,0,1],
                    [0,1,0],
                    [0,1,1],
                    [1,0,0],
                    [1,0,1],
                    [1,1,0],
                    [1,1,1]]
    
    for vector in input_vectors:
        apply_inputs_to_circuit(signals_table, top_inputs, vector, elements, circuit_outputs)

    print()
    apply_inputs_to_circuit(signals_table, top_inputs, [0.5,0.5,0.5], elements, circuit_outputs, True)
    print()

    sample_sizes = [10,100,1000,10000,100000,1000000]
    for sample_size in sample_sizes:
        switcing_activity_of_AND1  = MCGate("AND", 2, sample_size)
        switcing_activity_of_NOT   = MCGate("NOT", 1, sample_size)
        switcing_activity_of_AND2  = MCGate("AND", 2, sample_size, 1, [signals_table[4], signals_table[5]])
        print(f"Sample size = {sample_size}")
        print(f"Switching Activity Estimation of first AND gate: {switcing_activity_of_AND1: .5f}")
        print(f"Switching Activity Estimation of NOT gate: {switcing_activity_of_NOT: .5f}")
        print(f"Switching Activity Estimation of second AND gate: {switcing_activity_of_AND2: .5f}\n")


if __name__ == "__main__":
    main()