from utils import Element, CircuitParser
from utils import process_circuit_with_truth_table_vectors, process_circuit_with_input_vector
from utils import compute_switching_acitivities_with_mc

def main():
    e1 = Element("AND",['a','b'],'c')
    e2 = Element("NOT",['e'],'f')
    e3 = Element("AND",['c','f'],'d')

    elements_table   = [e1, e2, e3]
    signals_table    = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0}
    elements_outputs = CircuitParser().get_elements_outputs(elements_table)
    tpl_inputs       = CircuitParser().find_top_inputs(elements_table, elements_outputs)
    elements_inputs  = CircuitParser().get_elements_inputs(elements_table)
    circuit_outputs  = CircuitParser().get_circuit_outputs(elements_outputs, elements_inputs)

    input_vector = [0.5 for input in tpl_inputs]
    process_circuit_with_truth_table_vectors(elements_table, tpl_inputs, signals_table, circuit_outputs)
    process_circuit_with_input_vector(elements_table, tpl_inputs, signals_table, input_vector, circuit_outputs, True)
    mc_sample_size = 200000
    compute_switching_acitivities_with_mc(elements_table, signals_table, mc_sample_size)


if __name__ == "__main__":
    main()