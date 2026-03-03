module MCPU_RAMControllertb();
  parameter WORD_SIZE=8;
  parameter ADDR_WIDTH=8;
  parameter RAM_SIZE=1<<ADDR_WIDTH;
  
  reg we;
  reg re;
  reg [WORD_SIZE-1:0] datawr;
  reg [ADDR_WIDTH-1:0] addr;
  reg [ADDR_WIDTH-1:0] instraddr;
  wire [WORD_SIZE-1:0] datard;
  wire [WORD_SIZE-1:0] instrrd;
  
  reg [WORD_SIZE-1:0] datawrtemp;
  
  reg clk;
  
  MCPU_RAMController #(.WORD_SIZE(WORD_SIZE), .ADDR_WIDTH(ADDR_WIDTH)) raminst(we, datawr, re, addr, datard, instraddr, instrrd);
  
  task exec_ram_operation(input reg [8*10-1:0]       operation, 
                          input reg [ADDR_WIDTH-1:0] d_addr,
                          input reg [WORD_SIZE-1:0]  data_wr,
                          input reg [ADDR_WIDTH-1:0] instr_addr);
    begin
      if(operation == "RDMEM") begin
        re   <= 1;
        addr <= d_addr;
        @(posedge clk);
        addr <= 0;
        re   <= 0;
        @(posedge clk);
      end else if(operation == "WRMEM") begin
        we     <= 1;
        addr   <= d_addr;
        datawr <= data_wr;
        @(posedge clk);
        addr   <= 0;
        datawr <= 0;
        we     <= 0;
        @(posedge clk);
      end else if(operation == "RINSTR") begin
        instraddr <= instr_addr;
        @(posedge clk);
        instraddr <= 0;
        @(posedge clk);
      end else begin
        re   <= 1;
        addr <= d_addr;
        instraddr <= instr_addr;
        @(posedge clk);
        addr <= 0;
        re   <= 0;
        instraddr <= 0;
        @(posedge clk);
      end
    end
  endtask
  
  task get_random_bit_vector(output reg [WORD_SIZE-1:0] out_vec);
    reg [WORD_SIZE-1:0] temp;
    integer i;
    begin
      for(i=0; i<WORD_SIZE; i = i+1) begin
        temp[i] = $urandom_range(0,1);
      end
      out_vec = temp;
    end
  endtask
  
  initial begin
    clk <= 0;
    forever #10 clk <= !clk;
  end
  
  
  integer i;
  initial 
  begin
    we <= 0;
    re <= 0;
    addr <= 0;
    instraddr <= 0;
    @(posedge clk);
    
    get_random_bit_vector(datawrtemp);
    exec_ram_operation("WRMEM", 100, datawrtemp, 0);
    
    
    get_random_bit_vector(datawrtemp);
    exec_ram_operation("WRMEM", 2, datawrtemp, 0);
    
    
    exec_ram_operation("RDMEM", 2, datawrtemp, 0);
    
    exec_ram_operation("RINSTR", 0, datawrtemp, 100);
    
    exec_ram_operation("RD_RINSTR", 2, datawrtemp, 100);
    #20 $stop;
  end
  
endmodule
  