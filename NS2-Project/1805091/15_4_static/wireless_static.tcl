if {$argc == 4} {
set val(nn) [lindex $argv 0]
set val(nf) [lindex $argv 1]
set tx_range [lindex $argv 2]
set packet_rate [lindex $argv 3]
} else {
set val(nn) 20
set val(nf) 10
set tx_range 200
set packet_rate 100
}
set cbr_interval  [expr {1.0 /$packet_rate }]
set area [ expr {$tx_range * 2 }]
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
set val(netif)        Phy/WirelessPhy/802_15_4        ;# network interface type
set val(mac)          Mac/802_15_4             ;# MAC type
set val(rp)           DSDV                     ;# ad-hoc routing protocol 

# =======================================================================
Mac/802_15_4 set syncFlag_ 1
Mac/802_15_4 set dataRate_ 11Mb
Mac/802_15_4 set dutyCycle_ cbr_interval

# trace file
set trace_file [open trace.tr w]
$ns trace-all $trace_file
puts "Trace file: trace.tr"
# nam file
set nam_file [open animation.nam w]
$ns namtrace-all-wireless $nam_file $area $area

# topology: to keep track of node movements
set topo [new Topography]
$topo load_flatgrid $area $area ;# 500m x 500m area


# general operation director for mobilenodes
create-god $val(nn)

#set tx range
set dist(100)  4.61444e-10
set dist(200)  1.15361e-10
set dist(300)  5.12715e-11
set dist(400)  2.88402e-11
set dist(500)  1.84577e-11

Phy/WirelessPhy set CSThresh_ $dist($tx_range)
Phy/WirelessPhy set RXThresh_ $dist($tx_range)
Phy/WirelessPhy set Pt_ 0.281838
Phy/WirelessPhy set freq_ 5.9e+9

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
                -energyModel EnergyModel\
		            -idlePower  56.4e-3 \
		            -rxPower 59.1e-3 \
		            -txPower 52.2e-3 \
                    -sleepPower 0.6e-3 \
                    -transitionPower 35.708e-3 \
		            -transitionTime 2.4e-3  \
		            -initialEnergy 1000 \
                -agentTrace ON \
                -routerTrace OFF\
                -macTrace ON\
                -movementTrace OFF


# create nodes
for {set i 0} {$i < $val(nn) } {incr i} {
    set node($i) [$ns node]
    $node($i) random-motion 0    
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
    $crb($i) set packetSize_ 64
    $crb($i) set interval_ $cbr_interval
    if { [expr {$i % 2}] == 0} {
        $ns color $i Red
    } else {
        $ns color $i Blue
    }

    # start traffic generation
    $ns at 1.0 "$crb($i) start"
    $ns at 50.0 "$crb($i) stop"
}


# End Simulation

# Stop nodes
for {set i 0} {$i < $val(nn)} {incr i} {
    $ns at 60.0 "$node($i) reset"
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

$ns at 60.0001 "finish"
$ns at 60.0002 "halt_simulation"




# Run simulation
puts "Simulation starting"
$ns run

