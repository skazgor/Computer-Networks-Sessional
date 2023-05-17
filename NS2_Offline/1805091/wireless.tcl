if {$argc == 3} {
set val(nn) [lindex $argv 0]
set val(nf) [lindex $argv 1]
set area [lindex $argv 2]
} else {
set val(nn) 20
set val(nf) 10
set area 500
}

expr { srand(7) }

# simulator
set ns [new Simulator]

# ======================================================================
# Define options

set val(chan)         Channel/WirelessChannel  ;# channel type
set val(prop)         Propagation/TwoRayGround ;# radio-propagation model
set val(ant)          Antenna/OmniAntenna      ;# Antenna type
set val(ll)           LL                       ;# Link layer type
set val(ifq)          Queue/DropTail/PriQueue  ;# Interface queue type
set val(ifqlen)       50                       ;# max packet in ifq
set val(netif)        Phy/WirelessPhy          ;# network interface type
set val(mac)          Mac/802_11               ;# MAC type
set val(rp)           AODV                     ;# ad-hoc routing protocol 
# set val(nn)           20                       ;# number of mobilenodes
# =======================================================================

# trace file
set trace_file [open trace.tr w]
$ns trace-all $trace_file

# nam file
set nam_file [open animation.nam w]
$ns namtrace-all-wireless $nam_file $area $area

# topology: to keep track of node movements
set topo [new Topography]
$topo load_flatgrid $area $area ;# 500m x 500m area


# general operation director for mobilenodes
create-god $val(nn)


# node configs
# ======================================================================

# $ns node-config -addressingType flat or hierarchical or expanded
#                  -adhocRouting   DSDV or DSR or TORA
#                  -llType	   LL
#                  -macType	   Mac/802_11
#                  -propType	   "Propagation/TwoRayGround"
#                  -ifqType	   "Queue/DropTail/PriQueue"
#                  -ifqLen	   50
#                  -phyType	   "Phy/WirelessPhy"
#                  -antType	   "Antenna/OmniAntenna"
#                  -channelType    "Channel/WirelessChannel"
#                  -topoInstance   $topo
#                  -energyModel    "EnergyModel"
#                  -initialEnergy  (in Joules)
#                  -rxPower        (in W)
#                  -txPower        (in W)
#                  -agentTrace     ON or OFF
#                  -routerTrace    ON or OFF
#                  -macTrace       ON or OFF
#                  -movementTrace  ON or OFF

# ======================================================================

$ns node-config -adhocRouting $val(rp) \
                -llType $val(ll) \
                -macType $val(mac) \
                -ifqType $val(ifq) \
                -ifqLen $val(ifqlen) \
                -antType $val(ant) \
                -propType $val(prop) \
                -phyType $val(netif) \
                -topoInstance $topo \
                -channelType $val(chan) \
                -agentTrace ON \
                -routerTrace ON \
                -macTrace OFF \
                -movementTrace OFF

# create nodes
for {set i 0} {$i < $val(nn) } {incr i} {
    set node($i) [$ns node]
    $node($i) random-motion 0      ;# enable random motion
    
    #set node possition
    #grid
    set  nodes_per_row [expr {int(sqrt($val(nn)))}]
    set  x [expr {int($i % $nodes_per_row) * ($area / $nodes_per_row) +($area / $nodes_per_row / 2)}]
    set  y [expr {int($i / $nodes_per_row) *  ($area / $nodes_per_row)+ 10}]
    $node($i) set X_ $x
    $node($i) set Y_ $y
    $node($i) set Z_ 0
    $ns initial_node_pos $node($i)  20
} 




for {set i 0} {$i < $val(nf)} {incr i} {
    set src [expr {int(rand() * $val(nn))}]
    set dest [expr { int(rand() * $val(nn))}]
    while {$src == $dest} {
        set dest [expr {int(rand() * $val(nn))}]
    }
    # Traffic config
    # create agent
    set udp [new Agent/UDP]
    set udp_sink [new Agent/Null]
    # attach to nodes
    $ns attach-agent $node($src)  $udp
    $ns attach-agent $node($dest) $udp_sink
    # connect agents
    $ns connect $udp $udp_sink
    $udp set fid_ $i

    # Traffic generator
    set crb($i) [ new Application/Traffic/CBR ]
    # attach to agent
    $crb($i) attach-agent $udp
    # set traffic parameters
    $crb($i) set packetSize_ 1024
    $crb($i) set interval_ 0.1

    # start traffic generation
    $ns at 1.0 "$crb($i) start"
}

# Define a list of color values
# set colorList {red blue green yellow orange pink purple brown}

# # Use a for loop to iterate over each flow
# for {set i 0} {$i < $val(nf)} {incr i} {
#   # Use the modulo operator to determine the color for this flow
#   set colorIndex [expr {$i % [llength $colorList]}]
#   set color [lindex $colorList $colorIndex]

#   # Set the color for this flow
#     $ns color $i $color
# }
$ns color 0 red
$ns color 1 blue
$ns color 2 green
$ns color 3 yellow
$ns color 4 orange
$ns color 5 pink
$ns color 6 purple
$ns color 7 brown

expr { srand(72) }
#start movement
for {set i 0} {$i < $val(nn) } {incr i} {
    set speed [expr {int(rand() * 5)+1}]
    set x [expr {int(rand() * ($area-3))+1}]
    set y [expr {int(rand() * ($area-3))+1}]
    $ns at 4.0 "$node($i) setdest $x $y $speed"
}

# End Simulation

# Stop nodes
for {set i 0} {$i < $val(nn)} {incr i} {
    $ns at 50.0 "$node($i) reset"
}

# call final function
proc finish {} {
    global ns trace_file nam_file
    $ns flush-trace
    close $trace_file
    close $nam_file
}

proc halt_simulation {} {
    global ns
    puts "Simulation ending"
    $ns halt
}

$ns at 50.0001 "finish"
$ns at 50.0002 "halt_simulation"




# Run simulation
puts "Simulation starting"
$ns run

