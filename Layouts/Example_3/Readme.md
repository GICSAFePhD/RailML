# Example_3
## Description
Name: AdvancedExample.RailAID

This example is mentioned in the manuscript titled: "Automatic Railway Signalling Generation for Railways Systems Described on Railway Markup Language (railML)". Henceforth, when we refer to the manuscript, we will do it as [[1]](#references).

## Analysis principles

The signalling generation process used in this work was designed following signalling principles detailed in [[1]](#references) in the section "I. INTRODUCTION".

## Step by step

The following is the general methodology or "step by step" followed for analysing a railway network with the approach of this work [[1]](#references).

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

![Figure 1](select_example.jpg "Figure 1")

*Figure 1. Select example.*

The necessary information to define the graph network is distributed across several sections of the railML file, specifically inside netElements (nodes) and netRelations (edges) items found in the class Infrastructure/Topology as described in [[1]](#references).

Figure 2 shows the railway network without signalling. The user will need the Design4Rail Horizon Software Suite Track Planner application and import the archive "Example_3.railml" to visualise the railway network used in this example. 

For further information about the Design4Rail Horizon Software Suite and the Track Planner application, please refer to [Official web page of Design4Rail](https://design4rail.com/service/d4rhorizon/#section-downloadHorizon).

For a detailed explanation about importing railML files, go to section [G.1](#g1-obtaining-the-interlocking-table-in-design4rail) of this document. 

![Figure 2](Figure0.jpg "Figure 2")

*Figure 2. Railway network without signalling.*

### B. Define a graph network to associate the railway elements

This step allows us to evaluate the consistency of the network connections provided in the RailML file, through the determination of the direction, position, and interconnection of each of the nodes of the given railway network.

In [[1]](#references), in the section "II. RAILWAY NETWORK ANALYZER DESIGN" in literal B, we see Algorithm 1, which explains the network analysis process.

The result of this RNA step is show in Console Output 1:

~~~
#################### Starting Railway Network Analyzer ####################
Reading .railML file
Creating railML object
Analysing railML object
 Analysing graph
ne1 [-2010, 300] [-300, 300] >>   
ne4 [7083, 150] [6686, 150] <<    
ne7 [-2010, 150] [-300, 300] >>   
ne9 [-300, 300] [188, 300] >>     
ne11 [2580, 300] [2730, 150] >>   
ne14 [2730, 150] [2190, 150] <<   
ne17 [4380, 300] [2580, 300] <<   
ne23 [3810, -900] [2490, -1050] <<
ne24 [3810, -900] [2490, -1050] <<
ne26 [2490, -1050] [2138, -1050] <<
ne29 [-996, -1050] [239, -1050] >>
ne30 [-996, -1050] [-1373, -1050] <<
ne32 [239, -1050] [-150, -1050] <<
ne41 [-966, -1200] [-300, -1200] >>
ne43 [1560, -1050] [1710, -1200] >>
ne44 [1560, -1050] [1165, -1050] <<
ne47 [1710, -1200] [1290, -1200] <<
ne48 [1710, -1200] [1920, -1410] >>
ne59 [2009, 300] [2580, 300] >>
ne64 [4108, -782] [3810, -900] <<
ne65 [2138, -1050] [1866, -1050] <<
ne67 [2984, -480] [3882, -480] >>
ne70 [2984, -480] [2910, 0] <<
ne78 [4380, 300] [4825, 300] >>
ne79 [4230, 150] [4380, 300] >>
ne82 [-150, -1050] [-300, -1200] <<
ne83 [-150, -1050] [-996, -1050] <<
ne84 [-300, -1200] [-966, -1350] <<
ne86 [-2013, -750] [-1673, -750] >>
ne87 [-1673, -750] [-1523, -900] >>
ne88 [-1673, -750] [-1323, -750] >>
ne89 [-1373, -1050] [-2013, -1050] <<
ne90 [-2013, -900] [-1523, -900] >>
ne91 [-1523, -900] [-1373, -1050] >>
ne93 [4825, 300] [5149, 300] >>
ne94 [4826, 150] [4230, 150] <<
ne95 [188, 300] [2009, 300] >>
ne96 [5149, 300] [5842, 300] >>
ne97 [5149, 150] [4826, 150] <<
ne98 [5842, 300] [6686, 300] >>
ne99 [5841, 150] [5149, 150] <<
ne100 [880, -1050] [578, -1050] <<
ne101 [1165, -1050] [880, -1050] <<
ne102 [1866, -1050] [1560, -1050] <<
ne103 [3882, -480] [4108, -782] >>
ne105 [6686, 300] [7083, 300] >>
ne106 [6686, 150] [5841, 150] <<
ne85 [-300, -1200] [578, -1050] >>
ne77 [4230, 150] [3045, 75] <<
ne104 [2910, 0] [3045, 75] >>
ne52 [2730, 150] [3045, 75] >>
ne21 [4230, 150] [3045, 75] <<
ne110 [578, -1050] [239, -1050] <<
 The network is connected
~~~

*Console Output 1. Step B railway elements.*

In this example, the Console Output 1 shows that the program can identify the nodes and their directions. Consol Output 1 has, for example, this line: ne1 [-2010, 300] [-300, 300] >>, it indicates the name of the netElement (ne1), the position (origin [-2010, 30] and end point [-300, 300]) of the net element, and the direction (>>, at right in this case, but in other example it could have been at left: <<). If compare this Consol Output 1 with Figure 2, and analysing each "netElement", all elements are coincident. The same analysis for the others netElements.

### C and D. Infrastructure analysis and CDL zones detection

The process of analysing the infrastructure and detecting CDL zones produces one result: identifying the existence and position of each infrastructure element in the network: platforms, curves, level crossings,  buffer stops, derailers, lines,  operational points, signals, switches, tracks and detection elements (axle counters, rail joints and track circuits).

In section "II. RAILWAY NETWORK ANALYSER DESIGN" literal C of [1], it is shown Algorithm 2, which explains the process of analysing the network; and in the same section but in literal D, it is explained the process used to detect CDL zones.

The result of this step is shown in Console Output 2 and Figure 3.

~~~
Analysing infrastructure --> Infrastructure.RNA
 Detecting Danger --> Safe_points.RNA
  ne1 has a Platform[plf177] @ [-1539, -300]
  ne4 has a Middle point @ [6884.5, 150]
  ne7 has a Platform[plf178] @ [-1538, -150]
  ne7 has a Curve(2 lines) @ [[-450, 150]]
  ne9 has a Middle point @ [-56.0, 300]
  ne14 has a Middle point @ [2460.0, 150]
  ne17 has a Platform[plf185] @ [3623, -300]
  ne23 has a Platform[plf181] @ [3151, 1050]
  ne23 has a Curve(2 lines) @ [[3660, -1050]]
  ne24 has a Platform[plf182] @ [3151, 900]
  ne24 has a Curve(2 lines) @ [[2640, -900]]
  ne26 has a Middle point @ [2314.0, -1050]
  ne29 has a Curve(3 lines) @ [[-846, -900], [89, -900]]
  ne30 has a Middle point @ [-1184.5, -1050]
  ne32 has a Middle point @ [44.5, -1050]
  ne41 has a Platform[plf180] @ [-653, 1200]
  ne44 has a Middle point @ [1362.5, -1050]
  ne47 has a Middle point @ [1500.0, -1200]
  ne59 has a Middle point @ [2294.5, 300]
  ne64 has a Curve(2 lines) @ [[3990, -900]]
  ne65 has a Middle point @ [2002.0, -1050]
  ne67 has a Platform[plf183] @ [3430, 480]
  ne70 has a Curve(5 lines) @ [[2670, -150], [2820, -480], [2820, 0], [2910, 0]]
  ne78 has a Middle point @ [4602.5, 300]
  ne83 has a Platform[plf179] @ [-653, 1050]
  ne84 has a Curve(2 lines) @ [[-450, -1350]]
  ne86 has a Middle point @ [-1843.0, -750]
  ne88 has a Middle point @ [-1498.0, -750]
  ne89 has a Middle point @ [-1799.7, -1050]
  ne89 has a Middle point @ [-1586.3, -1050]
  ne90 has a Middle point @ [-1768.0, -900]
  ne93 has a Middle point @ [4987.0, 300]
  ne94 has a Middle point @ [4528.0, 150]
  ne95 has a LevelCrossing[lcr176] @ [1100, -300]
  ne96 has a Platform[plf187] @ [5459, -300]
  ne97 has a Middle point @ [4987.5, 150]
  ne98 has a Middle point @ [6053.0, 300]
  ne98 has a Middle point @ [6264.0, 300]
  ne98 has a Middle point @ [6475.0, 300]
  ne99 has a Platform[plf186] @ [5459, -150]
  ne100 has a Middle point @ [729.0, -1050]
  ne101 has a Middle point @ [1022.5, -1050]
  ne102 has a Middle point @ [1713.0, -1050]
  ne103 has a Curve(4 lines) @ [[3990, -480], [4108, -782], [4140, -630]]
  ne105 has a Middle point @ [6884.5, 300]
  ne106 has a Middle point @ [6052.2, 150]
  ne106 has a Middle point @ [6263.5, 150]
  ne106 has a Middle point @ [6474.8, 150]
  ne85 has a Curve(2 lines) @ [[428, -1200]]
  ne77 has a Platform[plf322] @ [3619, 0]
  ne77 has a Curve(3 lines) @ [[3120, 0], [4080, 0]]
  ne104 has a Curve(2 lines) @ [[2970, 0]]
  ne52 has a Curve(2 lines) @ [[2970, 150]]
  ne21 has a Platform[plf321] @ [3621, -150]
  ne21 has a Curve(2 lines) @ [[3120, 150]]
  ne110 has a Middle point @ [408.5, -1050]
~~~

*Console Output 2. Infraestructure analysis and CDL zone detection.*

![Figure 3](step_C_and_D_2.png "Figure 3")

*Figure 3. Infrastructure analysis and CDL zones detection: GUI Output.*

As an example, Figure 4 zoom in some of these elements.

![Figure 4](step_C_and_D_graphic.jpg "Figure 4")

*Figure 4. Infrastructure analysis and CDL zones detection: Layout.*

### E. Generate signalling

To obtain an analysis for each network element in the program configurations (view Figure 5), select only the options you want.

![Figure 5](config_options.png "Figure 5")

*Figure 5. Configuration options of RNA.*

Below, in subsections E.1, E.2, E.3, and E.4, you will find the sequence of configurations used to analyze, step by step, the railway in this example.

#### E.1. Signals generated due to line borders(L) and buffer stops(T)

The configuration of the RNA GUI application needed for this step of the analysis is shown in Figure 6.

![Figure 6](config_1.PNG "Figure 6")

*Figure 6. Configuring RNA to obtain signals for line borders(L) and buffer stops(T).*

Signals are enumerated since 00 with a prefix letter to indicate which element generates them. BufferStops and LineBorders signals start with T and L, respectively. In Figure 7, we can visualise the signals generated by applying algorithm 3, explained in [[1]](#references) section "III. SIGNALLING GENERATION".

In red letters, automatically added signals are shown.

The RNA allocates signals close to the buffer stops:

-- Stop: *T01*, *T03*, *T05*, *T07*, *T09*, *T11*, *T13*, *T15*, *T17*, *T19*, *T21*, *T23*
-- Departure: *T02*, *T04*, *T06*, *T08*, *T10*, *T12*, *T14*, *T16*, *T18*, *T20*, *T22*, *T24*

The RNA allocates signals close to the line borders. RNA allocates departure signals which are: *L25* to *L42* assigned close to every line border that belongs to a netElement whose track is longer than a configurable fixed length.

![Figure 7](Figure1.jpg "Figure 7")

*Figure 7. Signals due to line borders(L) and buffer stops(T).*

#### E.2. Signals generated due to line borders(L),buffer stops(T) and rail joints (J)

The signals for rail joints are named J and have a consecutive number of signals.

Figure 8 shows the configuration of the RNA GUI application needed for this step of analysis.

![Figure 8](config_2.PNG "Figure 8")

*Figure 8. Configuring RNA to obtain signals for line borders(L), buffer stops(T) and rail joints (J).*

The algorithm assigns signals *J43* to *J49* at the beginning and end of each track to indicate the rail joints as shown in Figure 9.

![Figure 9](Figure2.jpg "Figure 9")

*Figure 9. Signals due to line borders(L), buffer stops(T) and rail joints (J).*

#### E.3. Signals generated due to line borders(L),buffer stops(T),rail joints (J), platforms(P) and level crossings(X)

The signals for platforms are named P, and signals for level crossings are named X. A consecutive number of signals is assigned for each type of signalling.

The configuration of the RNA GUI application needed for this step of the analysis is shown in Figure 10.

![Figure 10](config_3.PNG "Figure 10")

*Figure 10. Configuring RNA to obtain signals for line borders(L),buffer stops(T),rail joints (J), platforms(P) and level crossings(X).*

Notice that RNA can be configured to avoid adding duplicate signals when the level crossing and the platform are close together, as discussed in [[1]](#references), and therefore, the signalling between them is unnecessary. However, this configuration is a special parameter in RNA. For furthermore information about this, see section [G.3.1.2.](#g32-minimum-distance-parameter) 

It is necessary to introduce signals before the train reaches the level crossing as explained in Algorithm 5, explained in [[1]](#references) section "III. SIGNALLING GENERATION".

Also, it is necessary to have a departure signal after the platform. This logic is implemented using Algorithm 6, explained in [[1]](#references) section "III. SIGNALLING GENERATION".

In red letters, the signals Generated due level crossings and platforms are shown in Figure 11.

![Figure 11](Figure3.jpg "Figure 11")

*Figure 11. Signals due to line borders(L),buffer stops(T),rail joints (J), platforms(P) and level crossings(X).*

#### E.4. Signals generated due to line borders(L),buffer stops(T),rail joints (J), platforms(P),level crossings(X) and switches(S,H,C,B)

Figure 6 shows the configuration of the RNA GUI application needed for this step of analysis.

![Figure 12](config_4.PNG "Figure 12")

*Figure 12. Configuring RNA to obtain signals for line borders(L),buffer stops(T),rail joints (J), platforms(P),level crossings(X) and switches(S,H,C,B).*

The signals for switches are named based on the point they want to protect: S for Starting branch, C for the Continue branch and B for the Detour branch. There are also signals whose name starts with H that are not explicitly protecting the starting branch, the continue branch or the detour branch of a switch. These H signals are explained in [[1]](#references) section "III. SIGNALLING GENERATION" in literal E, where a manoeuvre signal numbered with H is always added plus the corresponding numbering sequence by Algorithm 7. This manoeuvre signal always accompanies the signal of the start branch (S) of the switch, and its function is to protect the railway elements that are after this signal (i.e. elements that are in the detour branch and in the continue branch).

Signals generated for (in red letters, added signals are shown):

- Sw04: *S113*, *C112*, *H114*
- Sw05: *B125 *
- Sw08: *S97*, *C95*, *B96*, *H98*, *H99*
- Sw09: *S102*, *C100*, *B101*, *H103*
- Sw11: *S116*, *C115*, *H117*
- Sw12: *S119*, *C118*, *H120*, *H121*
- Sw13: *B123*
- Sw41: *S126*, *C124*

(Only switches in Figure 4 were analised in the previous list, all the others are shown in Figure 13)

![Figure 13](Figure4.jpg "Figure 13")

*Figure 13. Signals due to line borders(L),buffer stops(T),rail joints (J), platforms(P),level crossings(X) and switches(S,H,C,B).*

### F. Simplify signalling

The signal simplification process used by RNA relies on two main principles: i) vertical inheritance and ii) horizontal inheritance. Both principles are explained in [1] in section "IV. SIGNALLING SIMPLIFICATION".

To simplify signals mark the configuration option "Simplify signals", as shown in Figure 14.

![Figure 14](config_5.PNG "Figure 14")

*Figure 14. Configuring RNA to simplify signalling.*

After the simplification only the appropriate signals are kept, as shown in Figure 15.

![Figure 15](Figure5.jpg "Figure 15")

*Figure 15. Signalling simplification.*

The simplification process was carried out according to the process described in section IV. SIGNALLING SIMPLIFICATION of [[1]](#references), as follows:

- **Simplification by vertical inheritance**

    Vertical inheritance was applied when the B signals of the Sw12 and Sw13 were moved to the signals H33 y H36, respectably. These signals B were not created because of the RNA when analysing the switches,  applying Algorithm 8 explained in section IV. SIGNALLING SIMPLIFICATION of [[1]](#references), literal A. The same simplification was done for moving signals C and S from ne9 to become H23 and H24.

- **Simplification by horizontal inheritance**

    The simplified signals due to horizontal inheritance are follows: S116 anc C122 were deleted due these were nearby T16, and have the same direction and orientation, but T16 has a higher priority. The same situation occurs between signals B123 and T21; between C95 and P56 and between C112 and P57. In all cases, is applied Algorithm 9 (described in section IV. SIGNALLING SIMPLIFICATION of [[1]](#references)). This algorithm was designed to group nearby objects as one single object, and generating signals according to the leftmost and rightmost railway element in the new single object. 
    
    The signal priority used to decide which signal remains and which is deleted is explained in section IV. SIGNALLING SIMPLIFICATION of [[1]](#references), literal B.  

~~~
Reducing redundant signals
 removing sig52 for sig01
 removing sig53 for sig02
 removing sig25 for sig04
 removing sig54 for sig05
 removing sig55 for sig06
 removing sig79 for sig06
 removing sig85 for sig08
 removing sig58 for sig09
 removing sig59 for sig10
 removing sig108 for sig11
 removing sig116 for sig16
 removing sig122 for sig16
 removing sig115 for sig18
 removing sig118 for sig20
 removing sig123 for sig22
 removing sig26 for sig44
 removing sig44 for sig26
 removing sig46 for sig26
 removing sig71 for sig36
 removing sig36 for sig71
 removing sig39 for sig68
 removing sig68 for sig39
 removing sig47 for sig45
 removing sig45 for sig80
 removing sig50 for sig48
 removing sig51 for sig49
 removing sig78 for sig53
 removing sig95 for sig56
 removing sig112 for sig57
 removing sig82 for sig66
 removing sig109 for sig67
 removing sig76 for sig74
 removing sig77 for sig75
 removing sig88 for sig93
 removing sig107 for sig105
~~~

### G. Export a resulting railway layout description

Once the signalling is generated, it is necessary to establish the railway routes to create the railway interlocking table. A railway route is the simplest path between two consecutive signals in the same direction, using the same tracks (see [[1]](#references)).

<a name="G.1"></a>
#### G.1. Obtaining table in Design4Rail

To obtain the interlocking table is necessary to use Design4Rail software to open the archive Example_2_B.railml" generated by RNA for this example, as shown in Figure 16.

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

*Table 1. Routes in Design4Rail*

![Figure 19](import_rail_aid_5.PNG "Figure 19")

### ***Note***

   To carry out this research work, we used the software Rail-AID developed by NEAT, and provided to us on July 2021. However, NEAT no longer supports this software. They upgrade to a new software named Desgin4Rail TrackPlanner application, whose functionalities are essentially the same as Rail-AID. Because of this reason, we recommended in the manuscript and the development of the examples available in this repository, the use of Design4Rail TrackPlanner. Users are notified, that Rail-AID and Design4Rail are not free software; therefore, appropriate licenses should be purchased for use. A trial version is sufficient to open and visualize the layouts of examples 2, 5, 6 y 7. However, to open and visualize examples 1, 3 y 4 a license should be purchased.

   Moreover, it is important to mention that when the RNA exports the railML file the Rail-AID software considers all these signals as a single aspect. This issue was notified by us to NEAT in March 2022, they acknowledged the notification, agreed that there is an error on their software and committed to fix this problem. However, this problem was never solved, and NEAT discontinued Rail-AID software, as explained above. This problem is not solved yet on Design4Rail, either. To get around this issue, the RNA creates N semaphores of one aspect and displays them one after the other, instead of creating one semaphore of N aspects. As a consequence of having N semaphores of one aspect the interlocking table has more routes than the scenario where there is one semaphore of N aspects. Therefore, to get the appropriate interlocking table corresponding to one semaphore of N aspects, use the procedure shown in section [G.1.](#g1-obtaining-the-interlocking-table-in-design4rail)
   
#### G.2. Original interlocking table

Figure 20 shows the structure of the original example. The signalling and the routes were designed by experts following the RailMl standard.

![Figure 19](1_A.png "Figure 19")

*Figure 19. Original example provided by RailMl*

The signalling and the original interlocking table were designed by experts following the RailMl standard, and are shown in Table 2.

*Table 2. Original interlocking table for this example provided by RailMl*

| Route  | Entry | Exit | Switches | Platforms | Crossings | netElements |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
| R_01 | 68N1 | 69Va | 68W02_R | - | Lc01 | ne7-ne9-ne95 |
| R_02 | 68N2 | 69Va | 68W02_N | - | Lc01 | ne1-ne9-ne95 |
| R_03 | 69Va | 69A | - | - | - | ne95-ne59 |
| R_04 | 69A | 69N2 | 69W03_N | Plat09 | - | ne59-ne17 |
| R_05 | 69A | 69N3 | Sw03_NN + 69W03_R + 69W04_R | Plat08 + Plat13 | - | ne59-ne11-ne52-ne77 |
| R_06 | 69B2 | 69P2 | Sw06_N | Plat09 | - | ne78-ne17 |
| R_07 | 69B2 | 69P3 | Sw06_R + Sw07_RR | Plat13 | - | ne78-ne79-ne77 |
| R_08 | 69B2 | 69P1 | Sw06_R + Sw07_RN | Plat12 | - | ne78-ne79-ne21 |
| R_09 | 69C | 69N1 | Sw04_RR | Plat12 | - | ne70-ne104-ne21 |
| R_10 | 69Vc | 69Vc1 | - | Plat7 | - | ne67-ne70 |
| R_11 | 70Va | 70A | - | - | - | ne103-ne64 |
| R_12 | 70N2 | 69Vc | 70W01_R | - | - | ne23-ne64-ne103-ne67 |
| R_13 | 70N1 | 69Vc | 70W0_N | - | - | ne24-ne64-ne103-ne67 |
| R_14 | 70B | 70N2 | 70W02_N | Plat05 | - | ne26-ne23 |
| R_15 | 70B | 70N1 | 70W02_R | Plat06 | - | ne26-ne24 |
| R_16 | 70A | 70P1 | 70W01_N | Plat06 | - | ne64-ne24 |
| R_17 | 70A | 70P2 | 70W01_R | Plat05 | - | ne64-ne23 |
| R_18 | 69W04Y | 69N3 | Sw03_NN + 69W04_N | Plat13 | - | ne14-ne52-ne77 |
| R_19 | 72-1 | S01 | Sw04_N | - | - | ne83-ne32 |
| R_20 | 72-3b | S01 | Sw04_R + Sw05_NR | - | - | ne41-ne82-ne32 |
| R_21 | 69B1 | 69P3 | Sw07_NR | Plat08 + Plat13 | - | ne97-ne94-ne77 |
| R_22 | 69P1 | 70Va | Sw03_RR | Plat07 | - | ne21-ne104-ne70-ne67-ne103 |
| R_23 | 69B1 | 69P1 | Sw07_NN | Plat12 | - | ne94-ne21 |
| R_24 | 69P2 | 68F | 69W03_N | - | Lc01 | ne17-ne59-ne95-ne9 |
| R_25 | 72-3b | 72B | Sw05_NN + Sw41_R | - | - | ne41-ne85-ne100 |
| R_26 | 72Va | 72A | - | - | - | ne44-ne104-ne100 |
| R_27 | 72-2 | 72B | Sw09_R + Sw41_N | - | - | ne29-ne110-ne100 |
| R_28 | S01 | 72B | Sw09_N + Sw41_N | - | - | ne32-ne110-ne100 |
| R_29 | 72B | 70B | 71W01_N | - | - | ne100-ne101-ne44-ne102-ne65-ne26 |
| R_30 | 69P3 | 68F | Sw03_NN + 69W03_R + 6904_R | - | Lc01 | ne77-ne52-ne11-ne59-ne95-ne9 |
| R_31 | 70P1 | 72Va | 70W02_R + 71W01_N | - | - | ne24-ne26-ne65-ne102-ne44 |
| R_32 | 70P2 | 72Va | 70W02_N + 71W01_N | - | - | ne23-ne26-ne65-ne102-ne44 |
| R_33 | 69Vc1 | 69C | - | - | - | ne70 |

#### G.3. Generated interlocking table

The result of the automatic process carried by the RNA is the intelocking table shown in Table 3. This result is consistent with Table 1 shown in subsection [G.2.](#g2-original-interlocking-table) Original interlocking table.

*Table 3. Interlocking table obtain through RNA when the option "One-direction only" is marked.*

| Route  | Entry | Exit | Switches | Platforms | Crossings | netElements |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
| R_01 |  J43  |  L35  | 68W02_R | - | - | ne7-ne9-ne95 |
| R_02 |  P53  |  L35  | 68W02_N | - | - | ne1-ne9-ne95 |
| R_03 |  J48  |  S83  | - | - | Lc01 | ne95-ne59 |
| R_04 |  S83  |  P67  | 69W03_N | Plat09 | - | ne59-ne17 |
| R_05 |  S83  |  P75  | Sw03_NN + 69W03_R + 69W04_R | Plat08 + Plat13 | - | ne59-ne11-ne52-ne77 |
| R_06 |  S110  |  P66  | Sw06_N | Plat09 | - | ne78-ne17 |
| R_07 |  S110  |  P74  | Sw06_R + Sw07_RR | Plat08 + Plat13 | - | ne78-ne79-ne77 |
| R_08 |  S110 |  P72  | Sw06_R + Sw07_NR | Plat12 | - | ne78-ne79-ne21 |
| R_09 |  L32  |  P73  | Sw03_RR | Plat12 | - | ne70-ne104-ne21 |
| R_10 |  P64  |  L32  | - | - | - | ne67-ne70 |
| R_11 |  L41  |  S90  | - | - | - | ne103-ne64 |
| R_12 |  B89  |  P64  | 70W01_R | Plat05 | - | ne23-ne64-ne103-ne67 |
| R_13 |  P61  |  P64  | 70W01_N | Plat07 | - | ne24-ne64-ne103-ne67 |
| R_14 |  S93  |  B89  | 70W02_N | - | - | ne26-ne23 |
| R_15 |  S93  |  B92  | 70W02_R | Plat06 | - | ne26-ne24 |
| R_16 |  S90 |  P62  | 70W01_N | Plat06 | - | ne64-ne24 |
| R_17 |  S90  |  P60  | 70W01_R | Plat05 | - | ne64-ne23 |
| R_18 |  T08  |  P75  | Sw03_NN + 69W04_N | Plat08 + Plat13 | - | ne14-ne52-ne77 |
| R_19 |  P57  |  C100  | Sw04_N | - | - | ne83-ne32 |
| R_20 |  P59  |  C100  | S04_R + Sw05_NR | - | - | ne41-ne82-ne32 |
| R_21 |  L37  |  P74  | Sw07_NR | Plat08 + Plat13 | - | ne97-ne94-ne77 |
| R_22 |  P72  |  L31  | Sw03_RR | - | - | ne21-ne104-ne70-ne67 |
| R_23 |  L37  |  P72  | Sw07_NN | Plat12 | - | ne97-ne94-ne21 |
| R_24 |  P66  |  J49  | 69W03_N | - | - | ne17-ne59-ne95 |
| R_25 |  P59  |  S105  | Sw05_NN + Sw41_R | - | - | ne41-ne85-ne100-ne101-ne44 |
| R_26 |  L28  |  L40  | - | - | - | ne44-ne104 |
| R_27 |  S97  |  C124  | Sw08_R + Sw09_R | - | - | ne30-ne29-ne110 |
| R_28 |  C100  |  C124  | Sw09_N | - | - | ne32-ne110 |
| R_29 |  S105  |  S93  | 71W01_N | - | - | ne44-ne102-ne65-ne26 |
| R_30 |  S86  |  J49  | 69W03_R + 69W04_R | - | - | ne52-ne11-ne59-ne95 |
| R_31 |  J49  |  S80  | - | - | Lc01 | ne95-ne9 |
| R_32 |  P60  |  L27  | 70W02_N | - | - | ne23-ne26 |
| R_33 |  P62  |  L27  | 70W02_R | - | - | ne24-ne26 |
| R_34 |  L27  |  L30  | - | - | - | ne26-ne65 |
| R_35 |  C104  |  L28  | 71W01_N | - | - | ne102-ne44 |

Routes 1 to 29 are equivalent in both interlocking tables.

Route 30 in the original signalling is splitted in route 30 and 31 by the RNA

Route 31 and 32 in the original signalling is splitted in routes 32/34/35 and 33/34/35 respectively.

Route 33 in the orignal signallins is integrated in Routes 9, 10 and 22 by the RNA.

### G.3.1. One-directional and bidirectional tracks

RNA can consider tracks as bidirectional, while the original layout has only one-directional track. This feature is activated by mismarking the "One direction only" option, as shown in Figure 20.

![Figure 20](config_5.PNG "Figure 20")

*Figure 20. Produce routes considering bidirectional tracks*

*Table 4. Interlocking table obtain through RNA when the option "One direction only" is mismarked.*

Extra routes considering bidirectional tracks:

| Route  | Entry | Exit | Switches | Platforms | Crossings | netElements |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
| R_36 |  T02  |  P53  | - | Plat01 | - | ne1 |
| R_37 |  T04  |  L42  | - | - | Ucr01 + Ocr01 | ne4-ne106 |
| R_38 |  T06  |  P55  | - | Plat02 | - | ne7 |
| R_39 |  T10  |  P59  | - | Plat04 | - | ne41 |
| R_40 |  T12  |  L29  | 71W02 | - | - | ne47-ne48 |
| R_41 |  T14  |  S105  | Sw05_RN + Sw41_R | - | - | ne84-ne85-ne100-ne101-ne44 |
| R_42 |  T14  |  C100  | Sw04_R + Sw05_RR | - | - | ne84-ne83-ne32 |
| R_43 |  T18  |  T15  | Sw11_N | - | - | ne88-ne86 |
| R_44 |  T20  |  S97  | Sw12_N | - | - | ne89-ne30 |
| R_45 |  T22  |  S97  | Sw12_R + Sw13_R | - | - | ne90-ne91-ne30 |
| R_46 |  T24  |  P70  | - | Plat11 | Ucr01 + Ocr01 | ne105-ne98-ne96 |
| R_47 |  L30  |  C104  | - | - | - | ne65-ne102 |
| R_48 |  L31  |  P65  | - | Plat07 | - | ne67 |
| R_49 |  L33  |  L34  | - | - | - | ne78-ne93 |
| R_50 |  L34  |  L38  | - | Plat11 | - | ne96-ne98 |
| R_51 |  L35  |  J48  | - | - | - | ne95 |
| R_52 |  L38  |  T23  | - | - | Ucr01 + Ocr01 | ne98-ne105 |
| R_53 |  L40  |  S126  | - | - | - | ne101-ne100 |
| R_54 |  L42  |  L37  | - | Plat10 | - | ne108-ne99-ne97 |
| R_55 |  P55  |  J43  | - | - | - | ne7 |
| R_56 |  P56  |  S119  | Sw08_N | - | - | ne83-ne30 |
| R_57 |  P65  |  L41  | - | - | - | ne67-ne103-ne64 |
| R_58 |  P67  |  L33  | Sw06_N | - | - | ne17-ne78 |
| R_59 |  P69  |  T03  | - | - | Ucr01 + Ocr01 | ne90-ne106-ne4 |
| R_60 |  P70  |  S110  | - | - | - | ne96-ne93-ne78 |
| R_61 |  P73  |  P69  | Sw07_NN | Plat10 | - | ne21-ne94-ne97-ne99 |
| R_62 |  P73  |  L33  | Sw07_NR | - | - | ne21-ne79-ne78 |
| R_63 |  P74  |  S86  | Sw03_NN | - | - | ne77-ne52 |
| R_64 |  P75  |  P69  | Sw07_RN | - | - | ne77-ne94-ne97-ne99 |
| R_65 |  P75  |  L33  | Sw06_R + Sw07_RR | - | - | ne77-ne79-ne78 |
| R_66 |  B92  |  P61  | - | - | - | ne24 |
| R_67 |  B96  |  S119  | Sw08_R | - | - | ne29-ne30 |
| R_68 |  B101  |  B96  | - | - | - | ne29 |
| R_69 |  C124  |  S105  | Sw41_N | - | - | ne110-ne100-ne101-ne44 |
| R_70 |  B125  |  T09  | Sw05_NN | Plat04 | - | ne85-ne41 |
| R_71 |  B125  |  T13  | Sw05_RN | - | - | ne85-ne84 |
| R_72 |  S80  |  T01  | 68W02_n | Plat01 | - | ne9-ne1 |
| R_73 |  S80  |  T05  | 68W02_R | Plat02 | - | ne9-ne7 |
| R_74 |  S86  |  T07  | 69W04_N | - | - | ne52-ne14 |
| R_75 |  S105 |  L29  | 71W01_R + 71W02_N | - | - | ne44-ne43-ne48 |
| R_76 |  S126  |  S102  | Sw41_N | - | - | ne100-ne110 |
| R_77 |  S126  |  B125 | Sw41_R | - | - | ne100-ne85 |
| R_78 |  S102  |  S113  | Sw09_N | - | - | ne110-ne32 |
| R_79 |  S102  |  B101  | Sw09_R | - | - | ne110-ne29 |
| R_80 |  S113  |  P56  | Sw04_N | Plat03 | - | ne32-ne83 |
| R_81 |  S113  |  T09  | Sw04_R + Sw05_NR | Plat04 | - | ne32-ne82-ne41 |
| R_82 |  S113  |  T13  | Sw04_R + Sw05_RR | - | - | ne32-ne82-ne84 |
| R_83 |  S119  |  T19  | Sw012_N | - | - | ne30-ne89 |
| R_84 |  S119  |  T15  | Sw11_R + Sw12_R + Sw13_N | - | - | ne30-ne91-ne87-ne86 |
| R_85 |  S119  |  T21 | Sw12_R + Sw13_R | - | - | ne30-ne91-ne90 |
| R_86 |  S97  |  P57  | Sw08_N | Plat03 | - | ne30-ne83 |
| R_87 |  T16  |  T17  | Sw11_N | - | - | ne86-ne88 |
| R_88 |  T16  |  S97  | Sw11_R + Sw12_R + Sw13_N | - | - | ne86-ne87-ne91-ne30 |

Routes 34 to 88 are created considering all the signals generated to protect buffer stops, line borders and curves, and to considering bidirectional tracks. Disabling these functionalities both interlocking tables are equivalent without any other difference between them.

![Figure 21](1_B.png "Figure 21")

*Figure 21. Generate table through RNA railway generate signalling*

#### G.3.2. Minimum distance parameter

As explained in literal B of section "IV. SIGNALING SIMPLIFICATION" in [[1]](#references), more than two railway elements can be combined if they are close enough. The threshold distance to determine if this combination must be done is a configuration parameter of RNA, named MIN_DISTANCE (minimum distance). As shown in Algorithms 8, 9, and 10 in [[1]](#references), this parameter is essential to locate, relocate and simplify signals. Because of integrity software reasons, this parameter should be between 300 and 500. For default, this value is 300. Figure 22 shows the parameter configuration in the GUI of RNA. 

![Figure 22](minimum_distance_parameter.png "Figure 22")

*Figure 22. Minimum distance parameter configuration*

#### G.3.3. Fixed length parameter

The fixed length parameter is necessary to allocate the departure signals, which maintains the trains in the network until the next network approves the movement. These signals allow trains to move outside the network without restrictions only if the track is not long enough (fixed length). RNA could easily be adapted to different criteria and regulations, thanks to this parameter. As shown in Algorithms 3, and 4 in [[1]](#references). Configuration of the fixed length parameter in RNA as shown in Figure 23. Because of integrity software reasons, this parameter should be between 300 and 500. For default, this value is 200. Figure 23 shows the parameter configuration in the GUI of RNA.

![Figure 23](fixed_length_parameter.jpeg "Figure 23")

*Figure 23. Fixed length parameter configuration*

## References

[1] M. N. Menendez, S. Germino, L. Díaz-Charris, and A. Lutenberg, Automatic Railway Signalling Generation for Railways Systems Described on Railway Markup Language (railML). 





























