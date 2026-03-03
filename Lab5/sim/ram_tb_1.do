onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate -label clk /MCPU_RAMControllertb/clk
add wave -noupdate -label we /MCPU_RAMControllertb/we
add wave -noupdate -label re /MCPU_RAMControllertb/re
add wave -noupdate -label addr -radix hexadecimal /MCPU_RAMControllertb/addr
add wave -noupdate -label datard -radix hexadecimal /MCPU_RAMControllertb/datard
add wave -noupdate -label datawrtemp -radix hexadecimal /MCPU_RAMControllertb/datawrtemp
add wave -noupdate -label datawr -radix hexadecimal /MCPU_RAMControllertb/datawr
add wave -noupdate -label instraddr -radix hexadecimal /MCPU_RAMControllertb/instraddr
add wave -noupdate -label instrrd -radix hexadecimal /MCPU_RAMControllertb/instrrd
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {0 ps} 0}
quietly wave cursor active 0
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
WaveRestoreZoom {0 ps} {242 ps}
