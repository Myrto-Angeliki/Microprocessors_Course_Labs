module MCPU_Registerfiletb();
  parameter WORD_SIZE=8;
  parameter OPERAND_SIZE=4;
  parameter REGS_NUMBER_WIDTH=2;
  parameter REGISTERS_NUMBER=1<<REGS_NUMBER_WIDTH;
  
  reg clk;
  
  reg [OPERAND_SIZE-1:0] operand1;
  reg [OPERAND_SIZE-1:0] operand2;
  reg [OPERAND_SIZE-1:0] operand3;
  reg [1:0] regset_cmd;
  reg regset_wb;
  reg [WORD_SIZE-1:0] regdatatoload;
  wire [WORD_SIZE-1:0] RegOp1;
  wire [WORD_SIZE-1:0] alu_in1;
  wire [WORD_SIZE-1:0] alu_in2;

  MCPU_Registerfile #(.WORD_SIZE(WORD_SIZE), .OPERAND_SIZE(OPERAND_SIZE)) 
  regfileinst (.op1(operand1), 
              .op2(operand2), 
              .op3(operand3), 
              .RegOp1(RegOp1), 
              .alu1(alu_in1), .alu2(alu_in2), .datatoload(regdatatoload), .regsetwb(regset_wb), .regsetcmd(regset_cmd));
     
  
  task set_regfile_inputs(input [OPERAND_SIZE-1:0] oper1,
                          input [OPERAND_SIZE-1:0] oper2,
                          input [OPERAND_SIZE-1:0] oper3, 
                          input [1:0] r_cmd);
      begin
        operand1   <= oper1;
        operand2   <= oper2;
        operand3   <= oper3;
        regset_cmd <= r_cmd;
        regset_wb  <= 1'b1;
        @(posedge clk);
        regset_wb  <= 1'b0;
        @(posedge clk);
      end
    endtask
  
  initial begin
    clk <= 0;
    forever #10 clk <= !clk;
  end
  
  
  reg [8*14-1:0] R_CMD_AS_STR;
  always @(regset_cmd)
  begin : R_CMD_AS_STR_CONV
    case(regset_cmd)
      regfileinst.NORMAL_EX:
      begin
        R_CMD_AS_STR<="NORMAL_EX";
      end
      regfileinst.LOAD_FROM_DATA:
      begin
        R_CMD_AS_STR<="LOAD_FROM_DATA";
      end
      regfileinst.MOV_INTERNAL:
      begin
        R_CMD_AS_STR<="MOV_INTERNAL";
      end
      default:
      begin
        R_CMD_AS_STR<="DO_NOTHING";
      end  
    endcase
  end
  
  
  integer i;
  
  initial begin
    regset_wb <= 1'b0;
    regset_cmd <= regfileinst.DO_NOTHING;
    
    for(i=0; i<WORD_SIZE; i = i+1) begin
      regdatatoload[i] = $urandom_range(0,1);
    end
    set_regfile_inputs(2'b10,2'b01,2'b11,regfileinst.LOAD_FROM_DATA);
    
    
    set_regfile_inputs(2'b00,2'b10,2'b11,regfileinst.MOV_INTERNAL);
    
    
    regdatatoload = regfileinst.R[0] ^ regfileinst.R[2];
    set_regfile_inputs(2'b00,2'b10,2'b11,regfileinst.NORMAL_EX);
    
    set_regfile_inputs(2'b00,2'b10,2'b11,regfileinst.DO_NOTHING);
    
    #20 $stop;
  end
endmodule
