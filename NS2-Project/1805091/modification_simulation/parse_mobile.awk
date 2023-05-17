BEGIN {
    received_packets = 0;
    sent_packets = 0;
    dropped_packets = 0;
    total_delay = 0;
    received_bytes = 0;
    
    start_time = 1000000;
    end_time = 0;
    nn=NN;
    nf=NF;
    speed=SPEED;
    packet_per_second=PACKET_PER_SECOND;
    # constants
    header_bytes = 8;
    for(i=0; i<nn; i++) {
		throughput[i] = 0;
	}
	
	for (i=0; i<nn; i++) {
		energy_consumption[i] = 0;	
	}
}


{
    event = $1;
    time_sec = $2;
    node = $3;
    layer = $4;
    packet_id = $6;
    packet_type = $7;
    packet_bytes = $8;
    
    energy = $13;			total_energy = $14;
	idle_energy_consumption = $16;	sleep_energy_consumption = $18; 
	transmit_energy_consumption = $20;	receive_energy_consumption = $22; 
    sub(/^_*/, "", node);
	sub(/_*$/, "", node);

    # set start time for the first line

    if (layer == "AGT" && packet_type == "cbr") {
       if(start_time > time_sec) {
        start_time = time_sec;
    }
    if(end_time< time_sec){
    end_time=time_sec;
    }
    if (energy == "[energy") {
		energy_consumption[node] = (idle_energy_consumption + sleep_energy_consumption + transmit_energy_consumption + receive_energy_consumption);
	}  
    if(event == "s") {
     sent_time[packet_id] = time_sec;
            sent_packets += 1;
        }

    else if(event == "r") {
            delay = time_sec - sent_time[packet_id];
            
            total_delay += delay;


            bytes = (packet_bytes - header_bytes);
            received_bytes += bytes;
            throughput[node] += bytes;
            
            received_packets += 1;
        }
    }

    if (packet_type == "cbr" && event == "D") {
        dropped_packets += 1;
    }
}


END {
    end_time = time_sec;
    simulation_time = end_time - start_time;
    total_energy_consumption = 0;
    for (i=0; i<nn; i++) {
        total_energy_consumption += energy_consumption[i];
    }

    energy_consumption_per_byte = total_energy_consumption / received_bytes;

    print "Number of Nodes: ", nn;
    print "Number of flows: ", nf;
    print "Speed: ", speed;
    print "Packet per second: ", packet_per_second;
    print "Sent Packets: ", sent_packets;
    print "Dropped Packets: ", dropped_packets;
    print "Received Packets: ", received_packets;
    print "Throughput: ", (received_bytes * 8) / simulation_time, ": bits/sec";
    print "Average Delay: ", (total_delay / received_packets), ": seconds";
    print "Delivery ratio: ", (received_packets / sent_packets);
    print "Drop ratio: ", (dropped_packets / sent_packets);
    print "Total Energy Consumption: ", total_energy_consumption, ": Joules";
    print "Energy Consumption per Byte: ", energy_consumption_per_byte, ": Joules";

    for (i=0; i<nn; i++) {
        print "Node: ", i, ": Per Node Throughput: ", throughput[i], ": Joules";
    }
}
