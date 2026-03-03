
## Requirements

- **Python 3.10 | Other Python versions could also work but 3.10 was used for these projects**
- **ModelSim or other HDL simulation software**
- **Verilog (all versions) or SystemVerilog**

---

## Microprocessors course Lab projects

Each folder contains a program that is based on one of lab projects that I had to complete for my Microprocessors course. These projects are:

- **Lab1**:  *gate\_sp\_eval.py*         ->  Signal probability evaluation of a gate. <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*monte\_carlo\_sims.py*     ->  Use of Monte Carlo simulation to estimate π or the 
                                        switching activity of a gate.
<br><br>
- **Lab2**: *circuit\_tests.py*         ->  Signal probability evaluation of a simple circuit, 
                                        switching activity estimation of the circuit by: <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a) using Monte Carlo simulation, b) using signal probabilities.
 <br><br>
- **Lab3**: *sorted\_circuit\_tests.py* ->  Signal probability evaluation for each circuit defined in one of
                                        the three files in the **circuit files** folder. 
<br><br>
- **Lab4**: *gena.py*                   ->  The implementation of the Genetic Algorithm that aims to find the 
                                        max number of switches possible for a circuit &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                        and the workload (set of inputs) that maximizes that number.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        *gena\_tests.py*            ->  Uses the the Genetic Algorithm as described in *gena.py*, to run 
                                        various switching activity stress tests.

- **Lab5** : *src\_cpu.v*               ->  A 3-stage pipelined processor that uses the _ramcontroller_, 
                                        _registerfile_, and _alu_ components found in the **src** folder.
                                        

                                     
