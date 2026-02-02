class Element:
    ELEMENT_TYPES = ["NOT","AND","OR","XOR","NAND","NOR"]

    def __init__(self,element_type,inputs,output):
        self.element_type = element_type
        self.inputs= inputs
        self.output = output

    def __str__(self):
        return f"Element {self.element_type} with inputs {self.inputs} and output {self.output}"
