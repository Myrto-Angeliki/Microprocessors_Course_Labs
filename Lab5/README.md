# MicroCPU Architecture

## Features
- **3-stage pipeline**
- **16-bit Data Registers and Memory**
- **8-bit Program Counter (PC)**
- **16 different Registers**
- **ALU Operations** (Addition, Subtraction, Logical Operations)
- **Memory Operations** (LW, SW)
<br>

## Instruction Set
The processor supports the following instruction types:

### R-Type Instructions (Register-Register Operations)
| Instruction                      | Opcode | Function                         |
|----------------------------------|--------|----------------------------------|
| AND operand1, operand2, operand3 |  0000  | operand1 = operand2 AND operand3 |
| OR  operand1, operand2, operand3 |  0001  | operand1 = operand2 OR operand3  |
| XOR operand1, operand2, operand3 |  0010  | operand1 = operand2 XOR operand3 |
| ADD operand1, operand2, operand3 |  0011  | operand1 = operand2 + operand3   |
| SUB operand1, operand2, operand3 |  0100  | operand1 = operand2 - operand3   |
| MOV operand1, operand2           |  0101  | operand1 = operand2              |
<br>

### I-Type Instructions (Immediate and Memory Operations)
| Instruction                     | Opcode | Function                |
|---------------------------------|--------|-------------------------|
| LOAD_FROM_MEM operand1, address |  0110  | operand1 = mem[address] |
| STORE_TO_MEM operand1,  address |  0111  | mem[address] = operand1 |
| SHORT_TO_REG operand1,  value   |  1000  | operand1 = value        |
<br>

### J-Type Instructions (Jump Operations)
| Instruction           | Opcode | Function                             |
|-----------------------|--------|--------------------------------------|
| BNZ operand1, address |  1001  | PC = PC + address (if operand1 != 0) |

---

# MCPU simulation

## Simulation Instructions

1. **Create Project**
<br/>Open your HDL simulator and create a new project.

2. **Add source files**
<br/>Add all .v files from the **/Lab5/src/** directory into your project.

3. **Run the simulation**
<br/> Start a simulation for one of the testbench files found in the **/Lab5/src/** directory (e.g. *cputb.v*).
<br/>If you are using *Modelsim* or *QuestaSim*, you can load one of the *.do* files found inside **Lab5/sim** by selecting
**File > Load > Macro File** and choosing the *file_name.do* file, or by typing ```do file_name.do``` inside the Transcript console.
Run the simulation by typing the command ```run -all``` in the Transcript window or by pressing the *Run -All* button.

---
## Simulation Results
   The wave produced after running a simulation for the *cputb.v* testbench is the one shown in Figure 1, which you can also find in the **/Lab5/doc** directory 
   along with the waves for the simulation of the other components.
<br/>
<figure>
    <img src="/Lab5/doc/mcpu_fib_tb_wave.png" alt="mcpu fibonacci sim wave" width="850" height="950">
    <figcaption>Figure 1. The waveform produced after running a simulation of the cputb.v testbench</figcaption>
</figure>

### Description of the *cputb.v* testbench
The testbench *cputb.v* executes the following operations: <br>
1. Sets the contents of the memory and registers R1-R3 to '0'.
2. Writes (in binary) the instructions of the fibonnaci program in the memory.
3. Writes the contents of the memory in "program.list".
4. Executes the program until (*MAX_FIB_INDEX* + 1) fibonacci numbers have been computed.

A fibonacci number is stored in mem[20] and R3 after computation. <br>
*current_fib_index* is the index of the fibonnaci number stored in mem[20].
