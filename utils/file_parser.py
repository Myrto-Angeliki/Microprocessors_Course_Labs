import sys
from .element import Element

VALID_GATE_NAMES = ["AND", "NAND", "OR", "NOR", "XOR", "XNOR", "NOT"]

class FileParser():
    def __init__(self, file_contents, first_line):
        self.file_contents = file_contents
        self.first_line = first_line

    def find_top_inputs(self, elements_table, element_outputs, tlp_included=False):
        top_inputs = []
        if not tlp_included:
            for element in elements_table:
                for input in element.inputs:
                    if (input not in element_outputs) and (input not in top_inputs):
                        top_inputs.append(input)      
        else:  
            for top_input in self.first_line[1:]:
                top_inputs.append(top_input.strip())
        return top_inputs
    

    def check_num_of_inputs(self, element_name, inputs_sp, line_no):
        num_of_inputs = len(inputs_sp)
        no_inputs = num_of_inputs == 0
        not_with_too_many_inputs = element_name == "NOT" and num_of_inputs > 1
        element_with_too_few_inputs = element_name != "NOT" and num_of_inputs < 2
        if element_with_too_few_inputs or not_with_too_many_inputs or no_inputs:
            correct_num_of_inputs = "2 or more inputs" if element_name != "NOT" else "one input"
            print(f"Error: Element {element_name} in line {line_no} has the wrong number of inputs")
            print(f"       An {element_name} element must have {correct_num_of_inputs} but found {num_of_inputs}")
            sys.exit(2)


    def get_element_name(self, element_definitions, line_no):
        element_name  = element_definitions[0].strip().upper()
        if element_name in VALID_GATE_NAMES: 
            return element_name
        else:
            print(f"\n Error: The name of the element {element_name} in line {line_no} is not valid")
            print(f"           Correct definition of an element:   {VALID_GATE_NAMES} output inputs")
            print("            For example:                         AND d a b c")
            sys.exit(2)


    def create_elements(self, start):
        elements_table= []
        for line, line_no in zip(self.file_contents[start:], range(1,(len(self.file_contents)+1))):
            element_definition = line.split() 
            element_name = self.get_element_name(element_definition, line_no)         
            inputs = []       
            for input in element_definition[2:]:
                inputs.append(input.strip())
            self.check_num_of_inputs(element_name, inputs, line_no)
            elem = Element(element_name, inputs, element_definition[1])
            elements_table.append(elem)
        return elements_table

    def parse_circuit_file(self):
        start = 1 if self.first_line[0].strip() == "TPLINPUTS" else 0
        elements_table = self.create_elements(start)
        element_outputs = [x.output for x in elements_table]
        top_inputs= self.find_top_inputs(elements_table, element_outputs, (start==1))
        return elements_table, element_outputs, top_inputs