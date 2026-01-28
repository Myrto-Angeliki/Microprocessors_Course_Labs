from .spNGate import evaluate_sp_function
from .file_reader import FileReader
from .file_parser import FileParser

class SortedCircuit:
    def __init__(self):
        self.elements_table= []
        self.top_inputs = []
        self.element_outputs = []
        self.previous_signals = []
        self.signals = {}


    def sort_elements_table(self):
        sorted_elements_table = []; unsorted_elements_table = self.elements_table[:]
        marked_inputs = self.top_inputs[:]
        length_of_ET = len(self.elements_table); length_of_SET = 0
        while length_of_SET != length_of_ET:   
            for element in unsorted_elements_table:
                count = 0
                for input in element.inputs:
                    if input in marked_inputs: count += 1      
                if count == len(element.inputs):
                    sorted_elements_table.append(element) 
                    marked_inputs.append(element.output) 
                    length_of_SET += 1  
            unsorted_elements_table = [element for element in self.elements_table if element not in sorted_elements_table]
        self.elements_table = sorted_elements_table[:]


    def initialize_signals(self): 
        self.previous_signals = []
        for signal in (self.top_inputs+self.element_outputs):
            self.signals[signal] = 0.0
            self.previous_signals.append(0.0)


    def load_from_file(self,file_path):
        lines, first_line = FileReader(file_path).read_circuit_file()
        self.elements_table, self.element_outputs, self.top_inputs = FileParser(lines, first_line).parse_circuit_file()
        self.initialize_signals()
        self.sort_elements_table()


    def apply_tpl_inputs(self, input_vector):
        for input, input_sp in zip(self.top_inputs, input_vector):
            self.signals[input] = input_sp


    def process(self):
        self.previous_signals = self.signals.values()
        for element in self.elements_table:
            input_SPs = [self.signals[input_name] for input_name in element.inputs]
            signal_probability = evaluate_sp_function(element.element_type, input_SPs, display_mode=False)
            self.signals[element.output] = signal_probability


    def apply_input_vector(self, input_vector):
        self.apply_tpl_inputs(input_vector)
        self.process()


    def count_switches(self):
        switches = 0
        for previous_output, current_output in zip(self.previous_signals, self.signals.values):
            if previous_output != current_output: switches += 1
        return switches