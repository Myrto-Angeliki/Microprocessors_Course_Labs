onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate -label clk /MCPUtb/clk
add wave -noupdate /MCPUtb/reset
add wave -noupdate -label {mem[20]} -radix unsigned {/MCPUtb/cpuinst/raminst/mem[20]}
add wave -noupdate -label current_fib_index -radix decimal /MCPUtb/current_fib_index
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {0 ps} 0}
quietly wave cursor active 1
configure wave -namecolwidth 150
configure wave -valuecolwidth 100
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
WaveRestoreZoom {0 ps} {4693 ps}
