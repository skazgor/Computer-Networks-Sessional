# vary area
ns wireless.tcl 40 20 250
awk -v NN=40 -v NF=20 -v AREA=250 -f parse.awk trace.tr > area.txt
ns wireless.tcl 40 20 500
awk -v NN=40 -v NF=20 -v AREA=500 -f parse.awk trace.tr >> area.txt
ns wireless.tcl 40 20 750
awk -v NN=40 -v NF=20 -v AREA=750 -f parse.awk trace.tr >> area.txt
# nam animation.nam 
ns wireless.tcl 40 20 1000
awk -v NN=40 -v NF=20 -v AREA=1000 -f parse.awk trace.tr >> area.txt
ns wireless.tcl 40 20 1250
awk -v NN=40 -v NF=20 -v AREA=1250 -f parse.awk trace.tr >> area.txt
# vary flow
ns wireless.tcl 40 10 500
awk -v NN=40 -v NF=10 -v AREA=500 -f parse.awk trace.tr > flow.txt
ns wireless.tcl 40 20 500
awk -v NN=40 -v NF=20 -v AREA=500 -f parse.awk trace.tr >> flow.txt
ns wireless.tcl 40 30 500
awk -v NN=40 -v NF=30 -v AREA=500 -f parse.awk trace.tr >> flow.txt
ns wireless.tcl 40 40 500
awk -v NN=40 -v NF=40 -v AREA=500 -f parse.awk trace.tr >> flow.txt
ns wireless.tcl 40 50 500
awk -v NN=40 -v NF=50 -v AREA=500 -f parse.awk trace.tr >> flow.txt
# vary node
ns wireless.tcl 20 20 500
awk -v NN=20 -v NF=20 -v AREA=500 -f parse.awk trace.tr > node.txt
ns wireless.tcl 40 20 500
awk -v NN=40 -v NF=20 -v AREA=500 -f parse.awk trace.tr >> node.txt
ns wireless.tcl 60 20 500
awk -v NN=60 -v NF=20 -v AREA=500 -f parse.awk trace.tr >> node.txt
# nam animation.nam
ns wireless.tcl 80 20 500
awk -v NN=80 -v NF=20 -v AREA=500 -f parse.awk trace.tr >> node.txt
ns wireless.tcl 100 20 500
awk -v NN=100 -v NF=20 -v AREA=500 -f parse.awk trace.tr >> node.txt
# plot
python3 graph.py