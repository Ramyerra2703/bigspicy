# Spice Simulation and STA using BIGSPICY

bigspicy is a tool for merging circuit descriptions (netlists), generating Spice decks modeling those circuits, generating Spice tests to measure those models, and analyzing the results of running Spice on those tests.My part of the project is to create the circuit protobuf.
# Tools Required

- ``` Icarius Verilog ```
- ``` Python3 ```
- ``` Xdm ``` tool for converting the spice files to ``` xyce ``` format.
- ``` bigspicy ``` for making a single circuit protobuf
- ``` xyce ``` for performing test

# Pre-requesites
## Converting SPICE files 

The spice files should be in xyce format.The convertion was done in the following [repository](https://github.com/LokeshMaji).

## Compiling Protobufs

We have to compile the protobufs into the python file.
```
git submodule update --init   
protoc --proto_path vlsir vlsir/*.proto vlsir/*/*.proto --python_out=.
protoc proto/*.proto --python_out=.

```
# Merging files into Circuit protobuf

The files are now merged into circuit protobuf.This (final.pb) can be used to generate whole module spice models.
We can use that to conduct various tests using xyce.Type the following (after cloning this directory) to merge the files.

```
./bigspicy.py \
    --import \
    --spef example_inputs/iiitb_counter.spef \
    --spice lib/sky130_fd_sc_hd.spice \
    --verilog example_inputs/iiitb_counter/iiitb_counter.v \
    --spice_header lib/sky130_fd_pr__pfet_01v8_hvt.pm3.spice\
    --spice_header lib/sky130_fd_pr__pfet_01v8.pm3.spice \
    --spice_header lib/sky130_fd_pr__nfet_01v8.pm3.spice \
    --spice_header lib/sky130_ef_sc_hd__decap_12.spice \
    --top iiitb_counter\
    --save final.pb \
    --working_dir /tmp/bigspicy

```

# Generating whole module Spice model

```
  
    ./bigspicy.py \
    --verilog example_inputs/iiitb_counter/iiitb_counter.v \
    --spice lib/sky130_fd_sc_hd.spice \
    --spice_header lib/sky130_fd_pr__pfet_01v8_hvt.pm3.spice\
    --spice_header lib/sky130_fd_pr__pfet_01v8.pm3.spice \
    --spice_header lib/sky130_fd_pr__nfet_01v8.pm3.spice \
    --spice_header lib/sky130_ef_sc_hd__decap_12.spice \
    --save final.pb \
    --top iiitb_counter\
    --flatten_spice --dump_spice spice.sp


```
# Future Works
The spice file and circuit protobuf was generated successfully.The use of bigspicy tool is done.Now,we can perform timing analysis on the created
spice file(.sp file) using xyce tool.
# Contributors 

- **Ram Yerra** 
- **Kunal Ghosh** 



# Acknowledgments


- Kunal Ghosh, Director, VSD Corp. Pvt. Ltd.
- Arya Raeis-Parsi

# Contact Information

- Ram Yerra, IMT2020558, International Institute of Information Technology, Bangalore  ,Ram.Yerra@iiitb.ac.in
- Kunal Ghosh, Director, VSD Corp. Pvt. Ltd. kunalghosh@gmail.com

# References

- [Bigspicy github](https://github.com/google/bigspicy)




