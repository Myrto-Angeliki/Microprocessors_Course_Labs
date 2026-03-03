onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate -label clk /MCPU_Registerfiletb/clk
add wave -noupdate -label operand1 -radix binary /MCPU_Registerfiletb/operand1
add wave -noupdate -label operand2 -radix binary /MCPU_Registerfiletb/operand2
add wave -noupdate -label operand3 /MCPU_Registerfiletb/operand3
add wave -noupdate -label regset_cmd /MCPU_Registerfiletb/regset_cmd
add wave -noupdate -label R_CMD_AS_STR -radix ascii /MCPU_Registerfiletb/R_CMD_AS_STR
add wave -noupdate -label regset_wb /MCPU_Registerfiletb/regset_wb
add wave -noupdate -label regdatatoload /MCPU_Registerfiletb/regdatatoload
add wave -noupdate -label RegOp1 /MCPU_Registerfiletb/RegOp1
add wave -noupdate -label alu_in1 /MCPU_Registerfiletb/alu_in1
add wave -noupdate -label alu_in2 /MCPU_Registerfiletb/alu_in2
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {261 ps} 0}
quietly wave cursor active 1
configure wave -namecolwidth 127
configure wave -valuecolwidth 72
configure wave -justifyvalue left
configure wave -signalnamewidth 0
configure wave -snapdistance 10
configure wave -datasetprefix 0
configure wave -rowmargin 4
configure wave -childrowmargin 2
configure wave -gridoffset 0
configure wave -gridperiod 1
configure wave -griddelta 40
configure wave -timeline 0
configure wave -timelineunits ns
update
WaveRestoreZoom {0 ps} {179 ps}
