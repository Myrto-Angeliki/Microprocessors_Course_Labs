onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate -label cmd /MCPU_Alutb/cmd
add wave -noupdate -label ALU_CMD_AS_STR -radix ascii /MCPU_Alutb/ALU_CMD_AS_STR
add wave -noupdate -label r1 -radix binary /MCPU_Alutb/r1
add wave -noupdate -label r2 -radix binary /MCPU_Alutb/r2
add wave -noupdate -label out -radix binary /MCPU_Alutb/out
add wave -noupdate -label CARRY_BORROW -radix binary /MCPU_Alutb/CARRY_BORROW
add wave -noupdate -label iscorrect /MCPU_Alutb/iscorrect
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
WaveRestoreZoom {0 ps} {19 ps}
