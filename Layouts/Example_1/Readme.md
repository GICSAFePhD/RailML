# Example_1
## Description
Name: General example used in the paper

This example was mentioned in the manuscript titled: "Automatic Railway Signalling Generation for Railways Systems Described on Railway Markup Language (railML)". Henceforth, when we refer to the manuscript, we will do it as [1].

## Analysis principles

The signalling generation process used in this work was designed following signalling principles detailed in [1] in the section "I. INTRODUCTION".

## Step by step

The following is the general methodology or "step by step" followed for analysing a railway network with the approach of this work [1].

A. Import the railway layout description.

B. Define a graph network to associate the railway elements.

C. Infrastructure analysis

D. Detect CDL zones.

E. Generate signalling.

F. Simplify signalling.

G. Export a resulting railway layout description.

Each step is explained below.

### A. Import the railway layout description

After having installed the RNA program according to the steps shown in the the section ["Usage"](https://github.com/GICSAFePhD/Layouts#usage), run the Python archive "main_GUI.py". This action produces the program output shown in Figure 1.

![Figure 1](select_example.png "Figure 1")

*Figure 1. Select example.*

The necessary information to define the graph network is distributed across several sections of the railML file, specifically inside netElements (nodes) and netRelations (edges) items found in the class Infrastructure/Topology as described in [1].

Figure 2 shows the railway network without signalling. The user will need the Design4Rail Horizon Software Suite Track Planner application and import the archive "Example_1.railml" to visualise the railway network for this example. 

For further information about the Design4Rail Horizon Software Suite and the Track Planner application, please refer to [Official web page of Design4Rail](https://design4rail.com/service/d4rhorizon/#section-downloadHorizon).

For a detailed explanation about importing railML files, go to section [G.1](#g1-obtaining-table-in-design4rail) of this document. 

![Figure 2](Figure0.jpg "Figure 2")

*Figure 2. Railway network without signalling.*

### B. Define a graph network to associate the railway elements

This step allows determining that the provided file's network connections are consistent. It also allows verifying the address, position, and interconnection of each node in the network.

In [1], in the section "II. RAILWAY NETWORK ANALYZER DESIGN" in literal B, we see Algorithm 1, which explains the network analysis process.

The result of this RNA step is show in Console Output 1:

~~~
#################### Starting Railway Network Analyzer ####################
Reading .railML file
Creating railML object
Analysing railML object
 Analysing graph
ne1 [810, 150] [1320, 150] >>
ne2 [2970, 0] [2460, 0] <<
ne8 [1320, 150] [1800, 150] >>
ne9 [1320, 150] [1530, 360] >>
ne12 [2460, 0] [1950, 0] <<
ne13 [2460, 0] [810, -180] <<
ne14 [1530, 360] [2970, 360] >>
ne15 [1530, 360] [2970, 570] >>
ne22 [1800, 150] [2970, 150] >>
ne23 [1950, 0] [810, 0] <<
ne24 [1800, 150] [1950, 0] >>
 The network is connected
~~~

*Console Output 1. Step B railway elements.*

In this example, the Console Output 1 shows that the program can identify the nodes and their directions. Consol Output 1 has, for example, this line: ne1 [810, 150] [1320, 150] >>, it indicates the name of the netElement (ne1), the position (origin [810, 150] and end point [1320, 150]) of the net element, and the direction (>>, at right in this case, but in other example it could have been at left: <<). If compare this Consol Output 1 with Figure 2, and analysing each "netElement", all elements are coincident. The same analysis for: ne14, ne15, ne17, ne18, ne19 and ne20.

### C and D. Infrastructure analysis and CDL zones detection

The process of analysing the infrastructure and detecting CDL zones produces one result: identifying the existence and position of each infrastructure element in the network: platforms, curves, level crossings,  buffer stops, derailers, lines,  operational points, signals, switches, tracks and detection elements (axle counters, rail joints and track circuits).

In section "II. RAILWAY NETWORK ANALYSER DESIGN" literal C of [1], it is shown Algorithm 2, which explains the process of analysing the network; and in the same section but in literal D, it is explained the process used to detect CDL zones.

The result of this step is shown in Console Output 2 and Figure 3.

~~~
Analysing infrastructure --> Infrastructure.RNA
 Detecting Danger --> Safe_points.RNA
  ne1 has a Middle point @ [1065.0, 150]
  ne2 has a Middle point @ [2715.0, 0]
  ne8 has a Middle point @ [1560.0, 150]
  ne12 has a Middle point @ [2205.0, 0]
  ne13 has a Platform[plf75] @ [1564, 180]
  ne13 has a LevelCrossing[lcr74] @ [1362, 180]
  ne13 has a Curve(2 lines) @ [[2280, -180]]
  ne14 has a Platform[plf68] @ [2490, -360]
  ne14 has a LevelCrossing[lcr69] @ [1945, -360]
  ne15 has a Curve(2 lines) @ [[1740, 570]]
  ne22 has a RailJoint[J15] @ [2452, 150]
  ne23 has a RailJoint[J14] @ [1284, 0]
~~~

*Console Output 2. Infraestructure analysis and CDL zone detection.*

![Figure 3](step_C_and_D_2.png "Figure 3")

*Figure 3. Infrastructure analysis and CDL zones detection: GUI Output.*

Figure 4 shows these elements.

![Figure 4](step_C_and_D_graphic.png "Figure 4")

*Figure 4. Infrastructure analysis and CDL zones detection: Layout.*

### E. Generate signalling

To obtain an analysis for each network element in the program configurations (view Figure 5), select only the options you want.

![Figure 5](config_options.png "Figure 5")

*Figure 5. Configuration options of RNA.*

Below you will find the sequence of configurations used to analyze, step by step, the railway in this example.

#### E.1. Signals generated due to line borders(L) and buffer stops(T)

Figure 6 shows the configuration of the RNA GUI application needed for this step of analysis.

![Figure 6](config_1.PNG "Figure 6")

*Figure 6. Configuring RNA to obtain signals for line borders(L) and buffer stops(T).*

Signals are enumerated since 00 with a prefix letter to indicate which element generates them. BufferStops and LineBorders signals start with T and L, respectively. In Figure 7, we can visualise the signals generated by applying algorithm 3, explained in [1] section "III. SIGNALLING GENERATION".

In red letters, automatically added signals are shown.

The RNA allocates signals close to the buffer stops:

-- Stop: *T01*, *T03*, *T05*
-- Departure: *T02*, *T04*, *T06*

The RNA allocates signals close to the line borders. RNA allocates departure signals which are: *L07, L08, L09 and L10* assigned close to every line border that belongs to a netElement whose track is longer than a configurable fixed length.

![Figure 7](Figure1.jpg "Figure 7")

*Figure 7. Signals due to line borders(L) and buffer stops(T).*

#### E.2. Signals generated due to line borders(L),buffer stops(T) and rail joints (J)

The signals for rail joints are named J and have a consecutive number of signals.

Figure 8 shows the configuration of the RNA GUI application needed for this step of analysis.

![Figure 8](config_2.PNG "Figure 8")

*Figure 8. Configuring RNA to obtain signals for line borders(L), buffer stops(T) and rail joints (J).*

The algorithm assigns signals *J11*, *J12*, *J13* and *J14* at the beginning and end of each track to indicate the rail joints as shown in Figure 9.

![Figure 9](Figure2.jpg "Figure 9")

*Figure 9. Signals due to line borders(L), buffer stops(T) and rail joints (J).*

#### E.3. Signals generated due to line borders(L),buffer stops(T),rail joints (J), platforms(P) and level crossings(X)

The signals for platforms are named P, and signals for level crossings are named X. A consecutive number of signals is assigned for each type of signalling.

Figure 10 shows the configuration of the RNA GUI application needed for this step of analysis.

![Figure 10](config_3.PNG "Figure 10")

*Figure 10. Configuring RNA to obtain signals for line borders(L),buffer stops(T),rail joints (J), platforms(P) and level crossings(X).*

Notice that RNA can be configured to avoid adding this signalling when the level crossing and the platform are close together; therefore, the signalling between them is unnecessary. However, this configuration is not accessible by the end user, since it is a special parameter in the RNA source code. 

It is necessary to introduce signals before the train reaches the level crossing as explained in Algorithm 5, explained in [1] section "III. SIGNALLING GENERATION".

A railway platform is where the passengers wait for trains to arrive and depart. Therefore, it is necessary to have a departure signal after the platform. This logic is implemented using Algorithm 6, explained in [1] section "III. SIGNALLING GENERATION".

Figure 11 shows (in red letters) the signals Generated due level crossings and platforms.

![Figure 11](Figure3.jpg "Figure 11")

*Figure 11. Signals due to line borders(L),buffer stops(T),rail joints (J), platforms(P) and level crossings(X).*

#### E.4. Signals generated due to line borders(L),buffer stops(T),rail joints (J), platforms(P),level crossings(X) and switches(S,H,C,B)

Figure 6 shows the configuration of the RNA GUI application needed for this step of analysis.

![Figure 12](config_4.PNG "Figure 12")

*Figure 12. Configuring RNA to obtain signals for line borders(L),buffer stops(T),rail joints (J), platforms(P),level crossings(X) and switches(S,H,C,B).*

The signals for switches are named based on the point they want to protect: S for Starting branch, C for the Continue branch and B for the Detour branch. However, other signals named with H are not explicitly protecting any of the three points switches have.

The Algorithm 7, explained in [1] section "III. SIGNALLING GENERATION" in literal E, a manoeuvre signal numbered with H is always added plus the corresponding numbering sequence. This manoeuvre signal that always accompanies the signal of the start branch (S) of the switch, and whose function is to protect the railway elements that are after this signal. That is, the elements that are in the detour branch and in the continue branch.

Signals generated for (in red letters, added signals are shown):

- Sw04: *S22*, *C21*, *H23*, *H24*
- Sw06: *S27*, *C25*, *B26*, *H28*
- Sw07: *C29*, *B30*
- Sw12: *S32*, *C31*, *H33*
- Sw13: *S35*, *C34*, *H36*

![Figure 13](Figure4.jpg "Figure 13")

*Figure 13. Signals due to line borders(L),buffer stops(T),rail joints (J), platforms(P),level crossings(X) and switches(S,H,C,B).*

### F. Simplify signalling

The signal simplification process used by RNA relies on two main principles: i) vertical inheritance and ii) horizontal inheritance. Both principles are explained in [1] in section "IV. SIGNALLING SIMPLIFICATION".

To simplify signals is needed that, mark the configuration option "Simplify signals", as shown in Figure 14.

![Figure 14](config_5.PNG "Figure 14")

*Figure 14. Configuring RNA to simplify signalling.*

After generating all the signalling, a simplification should be made to keep only the appropriate signals, as shown in Figure 15.

![Figure 15](Figure5.jpg "Figure 15")

*Figure 15. Signalling simplification.*

Followin, explains the simplification process.

- **Simplification by vertical inheritance**

    Vertical inheritance was applied when the B signals of the Sw12 and Sw13 were moved to the signals H33 y H36, respectably. These signals B were not created because of the RNA when analysing the switches, applying Algorithm 8 explained in section IV. SIGNALLING SIMPLIFICATION of [1], literal A. The same simplification was done for moving signals C and S from ne9 to become H23 and H24.

- **Simplification by horizontal inheritance**

    The simplified signals due to horizontal inheritance are follows: X17, P18, P19, B26, B30, C31 and C34 . Signal X17 and B26 were deleted due this was nearby of signal T02, and have the same direction and orientation. The same situation occurs between signals P18/B30 and T04; between signals P19 and T03; between C31 and J12; and between signals C34 and J13. In all cases, is applied Algorithm 9 (described in section IV. SIGNALLING SIMPLIFICATION of [1]). This algorithm was designed to avoid collisions by considering nearby objects as one single object, and generating signals according to the leftmost and rightmost railway element in the new single object. 

    The signal priority used to decide which signal remains and which is deleted is explained in section IV. SIGNALLING SIMPLIFICATION of [1], literal B. 

### G. Export a resulting railway layout description

Once the signalling is generated and simplified, it is necessary to establish the railway routes to create the railway interlocking table. A railway route is the simplest path between two consecutive signals in the same direction, using the same tracks.

<a name="G.1"></a>
#### G.1. Obtaining table in Design4Rail

To obtain the table of routes is necessary to open the archive generated for this example: "Example_1_B.railml" (if the user keeps the names provided by this repository) using Design4Rail software, as shown in Figure 16.

![Figure 16](import_rail_aid_1.png "Figure 16")
![Figure 16](import_rail_aid_2.PNG "Figure 16")

*Figure 16. Import railml file.*

Once the file is opened, it will be possible to view the network and its elements, as in Figure 17.

![Figure 17](import_rail_aid_3.PNG "Figure 17")

*Figure 17. Example 2 network in Design4Rail Track Planner.*

In the menu "View" in Design4Rail Track Planner, select "Routes", as shown in Figure 18.

![Figure 18](import_rail_aid_4.png "Figure 18")

*Figure 18. View Routes*

Then Design4Rail Track Planner will display the table of routes for this network. It is shown in Figure 19.

![Figure 19](import_rail_aid_5.PNG "Figure 19")

*Figure 19. Routes in Design4Rail*

#### G.2. Original table

Figure 20 shows the structure of the original example. The signalling and the routes were designed by experts following the RailMl standard.

![Figure 20](1_A.png "Figure 20")

*Figure 20. Original example provided by RailMl*

| Route  | Entry | Exit | Switches | Platforms | Crossings | netElements |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
| R_01 |  S01  |  S17  | Sw04_N | - | - | ne01-ne08 |
| R_02 |  S01  |  S19  | Sw04_R + Sw07_N | - | - | ne01-ne09-ne15 |
| R_03 |  S01  |  S05  | Sw04_R + Sw07_R | - | - | ne01-ne09-ne14 |
| R_04 |  S17  |  S15  | Sw12_N | - | - | ne08-ne22 |
| R_05 |  S16  |  S02  | Sw12_N | - | - | ne22-ne08 |
| R_06 |  S17  |  S12  | Sw12_R + Sw13_R | - | - | ne08-ne24-ne12 |
| R_07 |  S10  |  S02  | Sw12_R + Sw13_R | - | - | ne12-ne24-ne08 |
| R_08 |  S10  |  S14  | Sw13_N | - | - | ne12-ne23 |
| R_09 |  S13  |  S12  | Sw13_N | - | - | ne23-ne12 |
| R_10 |  S07  |  S10  | Sw06_N | - | - | ne02-ne12 |
| R_11 |  S07  |  S09  | Sw06_R | Plat13 | Lc08 | ne02-ne13 |
| R_12 |  S05  |  S06  | - | Plat11 | Lc06 | ne14 |
| R_13 |  S06  |  S20  | - | - | - | ne14 |
| R_14 |  S09  |  S18  | - | - | - | ne13 |

#### G.3. Generated table

The example analysed by RNA and the approach of this work has the following structure, signalling and routes, which are the result of an automatic process and also follow the RailMl standard.

![Figure 21](1_B.png "Figure 21")

*Figure 21. Generate table through RNA railway generate signalling*

| Route  | Entry | Exit | Switches | Platforms | Crossings | netElements |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
| R_01 |  S22  |  S32  | Sw04_N  | - | - | ne01-ne08 |
| R_02 |  S22  |  T05  | Sw04_R + Sw07_N | - | - | ne01-ne09-ne15 |
| R_03 |  S32  |  X15  | Sw04_R + Sw07_R | - | - | ne01-ne09-ne14 |
| R_04 |  S32  |  J11  | Sw12_N | - | - | ne08-ne22 |
| R_05 |  J12  |  C21  | Sw12_N | - | - | ne22-ne08 |
| R_06 |  S32  |  C25  | Sw12_R + Sw13_R | - | - | ne08-ne24-ne12 |
| R_07 |  S35  |  C21  | Sw12_R + Sw13_R | - | - | ne12-ne24-ne08 |
| R_08 |  S35  |  J14  | Sw13_N | - | - | ne12-ne23 |
| R_09 |  J13  |  C25  | Sw13_N | - | - | ne23-ne12 |
| R_10 |  S27  |  S35  | Sw06_N | - | - | ne02-ne12 |
| R_11 |  S27  |  T01  | Sw06_R | Plat13 | Lc08 | ne02-ne13 |
| R_12 |  X15  |  T03  | - | Plat11 | Lc06 | ne14 |
| R_13 |  T04  |  X16  | - | Plat11 | - | ne14 |
| R_14 |  T02  |  P20  | - | Plat13 | Lc08 | ne13 |

Extra routes considering bidirectional tracks:

| Route  | Entry | Exit | Switches | Platforms | Crossings | netElements |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
| R_15 |  T06  |  C29  | - | - | - | ne15 |
| R_16 |  J11  |  L09  | - | - | - | ne22 |
| R_17 |  J14  |  L10  | - | - | - | ne23 |
| R_18 |  X16  |  L07  | Sw04_R + Sw07_R | - | Lc06 | ne14-ne09-ne01 |
| R_19 |  C29  |  L07  | Sw04_N + Sw07_R | - | - | ne15-ne09-ne01 |
| R_20 |  C21  |  L07  | Sw04_N  | - | - | ne08-ne01 |
| R_21 |  P20  |  L08  | Sw06_R  | - | - | ne13-ne02 |
| R_22 |  C25  |  L08  | Sw06_N  | - | - | nex12-ne02 |

Routes 1 to 11 are the same in both interlocking tables.

Routes 12 and 13 in the original interlocking table were combined in Route Routet 12 because signals S06 and S20 were replaced by T03 due to proximity.

Route 14 was deleted because signal S09 was very close S18 and, therefore, unuseful as signal. Routes 11 and 14 in the original signalling were combined in Route 11 in the new signalling.

Routes 15 to 22 are created because RNA added signals T01,T02,T03,T04,T05 and T06 to protectt buffer stops and signals L07,L08,L09 and L10 to protect line borders. These new signals created new routes to stop prior the (relative or absolute) end of the network, increasing safety, and to add opposite routes than the originals, increasing mobility.

For obtaining an analysis which only includes a one direction of a railway operation, should be mismark the option in the program. Like Figure 21 and Figure 22. To obtain the tables, you have to follow the steps explained in [G.1](#g1-obtaining-table-in-design4rail).

![Figure 21](config_6.png "Figure 21")

*Figure 21. Produce routes considering one directional tracks*

![Figure 22](config_5.png "Figure 22")

*Figure 22. Produce routes considering bidirectional tracks*

## References

[1] M. N. Menendez, S. Germino, L. Díaz-Charris, and A. Lutenberg, Automatic Railway Signalling Generation for Railways Systems Described on Railway Markup Language (railML).
