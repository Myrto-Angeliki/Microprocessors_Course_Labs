module MCPU_Alu(cmd,in1,in2,out,CF);
parameter CMD_SIZE=3;
parameter WORD_SIZE=16;

parameter  [CMD_SIZE-1:0]  CMD_AND  = 0; //3'b000
parameter  [CMD_SIZE-1:0]  CMD_OR   = 1; //3'b001
parameter  [CMD_SIZE-1:0]  CMD_XOR  = 2; //3'b010
parameter  [CMD_SIZE-1:0]  CMD_ADD  = 3; //3'b011
parameter  [CMD_SIZE-1:0]  CMD_SUB  = 4; //3'b100


input [CMD_SIZE-1:0]  cmd;
input [WORD_SIZE-1:0] in1;
input [WORD_SIZE-1:0] in2;
output[WORD_SIZE-1:0] out;
//carry flag
output CF;

wire [CMD_SIZE-1:0] cmd;
wire [WORD_SIZE-1:0] in1;
wire [WORD_SIZE-1:0] in2;
reg  [WORD_SIZE-1:0] out;
//carry flag
reg  CF;


reg [WORD_SIZE-1:0] zero = 0;
reg [WORD_SIZE-1:0] temp;
reg temp2;

always @ (cmd, in1, in2) 
begin
  #2
case(cmd)
  CMD_AND : begin
               CF = 0;
               out = in1&in2; 
      end
  CMD_OR : begin
              CF = 0;
              out = in1|in2;
            end
  CMD_XOR : begin
              CF = 0;
              out = in1^in2;
            end
  CMD_ADD : begin
              {CF,out} = in1+in2;
            end
  CMD_SUB : begin
             	{CF,out} = in1-in2; // CF is borrow
            end
  default : begin
            end
 endcase
 end
endmodule