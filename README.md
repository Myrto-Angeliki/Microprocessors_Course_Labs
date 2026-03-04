
## Microprocessors course Lab projects

Each folder contains a program that is based on one of lab projects that I had to complete for my Microprocessors course. These projects are:

- **Lab1**: <br>
*gate\_sp\_eval.py*         ->  Signal probability evaluation of a gate. <br>
*monte\_carlo\_sims.py*     ->  Use of Monte Carlo simulation to estimate π or the switching activity of a gate.
<br><br>
- **Lab2**: <br>
*circuit\_tests.py*         ->  Signal probability evaluation of a simple circuit, switching activity estimation of the circuit by:<br>
a) using Monte Carlo simulation, b) using signal probabilities.
 <br><br>
- **Lab3**:<br>
*sorted\_circuit\_tests.py* ->  Signal probability evaluation for each circuit defined in one of the three files inside **/circuit\_files**. 
<br><br>
- **Lab4**: <br>
*gena.py*                   ->  AN implementation of the Genetic Algorithm that aims to find the max number of switches possible for a circuit and the workload (set of inputs) that maximizes that number.<br>
*gena\_tests.py*            ->  Uses the the Genetic Algorithm, as described in *gena.py*, to run various switching activity stress tests.

- **Lab5** : <br>
  *cpu.v* ->  A 3-stage pipelined processor that consists of the _ramcontroller_, _registerfile_, and _alu_ components found inside **/Lab5/src**.

---

## Requirements

- **Python 3.10 | Other Python versions could also work but 3.10 was used for the Python projects**
- **ModelSim or other HDL simulation software**
- **Verilog (all versions) or SystemVerilog**

## To run the project
  1. Clone the repository:<br>
    ```
    git clone https://github.com/Myrto-Angeliki/Microprocessors_Course_Labs.git
    ```<br><br>
  2. For **Lab1-4**, change directory to **/Microprocessors_Course_Labs**, open a terminal and then type the following command:<br>
    ```
    python -m LabX.module_name (for example python -m Lab4.gena_tests )
    ``` <br><br>
  3. For **Lab5**, open the .v files with your HDL simulator, compile them, and start a simulation for one of the testbench files that can be found in
     **/Lab5/src**. If you are using *Modelsim* or *QuestaSim*, you can load the *.do* files found inside **Lab5/sim** by selecting **File > Load > Macro File**        and choosing one of *.do* files, or by typing ```do macro_file_name.do``` inside the Transcript console.


                                     
