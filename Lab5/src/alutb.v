module MCPU_Alutb();

parameter CMD_SIZE=3;
parameter WORD_SIZE=8;

reg [CMD_SIZE-1:0] cmd;
reg [WORD_SIZE-1:0] r1;
reg [WORD_SIZE-1:0] r2;
wire [WORD_SIZE-1:0] out;
wire CARRY_BORROW;

reg iscorrect;

MCPU_Alu #(.CMD_SIZE(CMD_SIZE), .WORD_SIZE(WORD_SIZE)) aluinst (cmd, r1, r2, out, CARRY_BORROW);

initial begin
  r1 = 4; 
  r2 = 7;
  #3 ;
  r1 = 6; 
  r2 = 1;
  #3 ;
  r1 = 11; 
  r2 = 6;
  #3 ;
  r1 = 128;
  r2 = 128;
  #3 ;
  r1 = 32;
  r2 = 34;
end

initial begin
  cmd = 0;
  #3 cmd = 1;
  #3 cmd = 2;
  #3 cmd = 3;
  #3 cmd = 4;
  #6 $stop;
end

reg [8*7-1:0] ALU_CMD_AS_STR;
always @(cmd) begin
  case(cmd)
    aluinst.CMD_AND : begin
      ALU_CMD_AS_STR <= "CMD_AND";
    end
    aluinst.CMD_OR : begin
      ALU_CMD_AS_STR <= "CMD_OR";
    end
    aluinst.CMD_XOR : begin
      ALU_CMD_AS_STR <= "CMD_XOR";
    end
    aluinst.CMD_ADD : begin
      ALU_CMD_AS_STR <= "CMD_ADD";
    end
    aluinst.CMD_SUB : begin
      ALU_CMD_AS_STR <= "CMD_SUB";
    end
    default : begin
    end
  endcase
end
always @(out) begin
  case(cmd)
    aluinst.CMD_AND : begin
      if((out)==(r1&r2)) begin
        iscorrect = 1;
      end 
      else begin
        iscorrect = 0;
      end
    end
    aluinst.CMD_OR : begin
      if((out) == (r1|r2)) begin
        iscorrect = 1;
      end 
      else begin
        iscorrect = 0;
      end
    end
    aluinst.CMD_XOR : begin
      if((out) == (r1^r2)) begin
        iscorrect = 1;
      end 
      else begin
        iscorrect = 0;
      end
    end
    aluinst.CMD_ADD : begin
      if({CARRY_BORROW,out} == (r1+r2)) begin
        iscorrect = 1;
      end 
      else begin
        iscorrect = 0;
      end
    end
    aluinst.CMD_SUB : begin
      if({CARRY_BORROW,out} == (r1-r2)) begin
        iscorrect = 1;
      end 
      else begin
        iscorrect = 0;
      end
    end
    default : begin
    end
  endcase
end
endmodule

  
  


