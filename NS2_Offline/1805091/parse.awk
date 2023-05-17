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
    area=AREA;

    # constants
    header_bytes = 8;
}


{
    event = $1;
    time_sec = $2;
    node = $3;
    layer = $4;
    packet_id = $6;
    packet_type = $7;
    packet_bytes = $8;


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
        
    if(event == "s") {
     sent_time[packet_id] = time_sec;
            sent_packets += 1;
        }

        else if(event == "r") {
            delay = time_sec - sent_time[packet_id];
            
            total_delay += delay;


            bytes = (packet_bytes - header_bytes);
            received_bytes += bytes;

            
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

    print "Number o fNodes: ", nn;
    print "Number off lows: ", nf;
    print "Area: ", area;
    print "Sent Packets: ", sent_packets;
    print "Dropped Packets: ", dropped_packets;
    print "Received Packets: ", received_packets;
    print "Throughput: ", (received_bytes * 8) / simulation_time, ": bits/sec";
    print "Average Delay: ", (total_delay / received_packets), ": seconds";
    print "Delivery ratio: ", (received_packets / sent_packets);
    print "Drop ratio: ", (dropped_packets / sent_packets);
}
