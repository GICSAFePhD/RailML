# Example_1
## Name: 

![alt text](1_A.png)

| Route  | Entry | Exit | Switches | Platforms | Crossings | Tracks |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
| R_1 |  S07  |  S11  | Sw01_N  | - | - | ne14-ne16  |
| R_2 |  S08  |  S11  | Sw01_R  | - | - | ne15-ne16  |
| R_3 |  S09  |  S12  | Sw02_N  | - | - | ne18-ne16  |
| R_4 |  S10  |  S13  | Sw03_N  | - | - | ne20-ne19  |
| R_5 |  S10  |  S12  | Sw03_R + Sw02_R  | - | - | ne20-ne17-ne16  |

![alt text](1_B.png)

| Route  | Entry | Exit | Switches | Platforms | Crossings | Tracks |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
| R_1 |  P10  |  S18  | Sw01_N  | - | - | ne14-ne16  |
| R_2 |  B14  |  S18  | Sw01_R  | - | - | ne15-ne16  |
| R_3 |  P11  |  S15  | Sw02_N  | - | - | ne18-ne16  |
| R_4 |  S21  |  T01  | Sw03_N  | - | - | ne20-ne19  |
| R_5 |  S21  |  S15  | Sw03_R + Sw02_R | - | - | ne20-ne17-ne16  |
| R_6 |  S15  |  P09  | Sw01_N  | - | Lc01 | ne16-ne14  |
| R_7 |  S15  |  L04  | Sw01_R  | - | Lc01 | ne16-ne15  |
| R_8 |  S18  |  P12  | Sw02_N  | - | Lc01 | ne16-ne18  |
| R_9 |  T02  |  L06  | SW03_N  | -  | - | ne19-ne20  |
| R_10 |  S18  |  L06  | Sw02_R + Sw03_R  | - | Lc01 | ne16-ne17-ne20  |

Routes 1 to 5 are the same in both interlocking tables, but RNA considers tracks as bidirectional while the original layout has only one direction per track. Routes 6 to 10 are the opposite of routes 1 to 5. It does not affect safety, RNA always considers every possible route in the layout.

# Example_2
## Name: 

# Example_3
## Name:

# Example_4
## Name:

![alt text](4_A.png)

| Route  | Entry | Exit | Switches | Platforms | Crossings | Tracks |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
| R_1 |  S07  |  S11  | Sw01_N  | - | - | ne14-ne16  |

![alt text](4_B.png)

| Route  | Entry | Exit | Switches | Platforms | Crossings | Tracks |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
| R_13 |  S23  |  C25  | Sw01_N | - | - | ne01-ne02 |
| R_09 |  C21  |  T01  | Sw01_N | - | - | ne02-ne01 |
| R_14 |  S23  |  J11  | Sw01_R | - | - | ne01-ne03 |
| R_06 |  J12  |  T01  | Sw01_R | - | - | ne03-ne01 |
| R_19 |  S27  |  C21  | Sw02_N | - | - | ne04-ne02 |
| R_10 |  C25  |  T03  | Sw02_N | - | - | ne02-ne04 |
| R_20 |  S27  |  J12  | Sw02_R | - | - | ne04-ne03 |
| R_05 |  J11  |  T04  | Sw02_R | - | - | ne03-ne04 |
| R_15 |  S31  |  C33  | Sw03_N | - | - | ne05-ne06 |
| R_11 |  C29  |  T05  | Sw03_N | - | - | ne06-ne05 |
| R_16 |  S31  |  J17  | Sw03_R | - | - | ne05-ne07 |
| R_08 |  J18  |  T05  | Sw03_R | - | - | ne07-ne05 |
| R_17 |  S35  |  C29  | Sw04_N | - | - | ne08-ne06 |
| R_12 |  C33  |  T07  | Sw04_N | - | - | ne06-ne08 |
| R_18 |  S35  |  J18  | Sw04_R | - | - | ne08-ne07 |
| R_07 |  J17  |  T07  | Sw04_R | - | - | ne07-ne08 |
| R_01 |  T02  |  S23  | - | - | - | ne01 |
| R_02 |  T04  |  S27  | - | - | - | ne04 |
| R_03 |  T06  |  S31  | - | - | - | ne05 |
| R_04 |  T08  |  S35  | - | - | - | ne08 |

# Example_5

# Example_6

# Example_7

# Example_8

- [ ] Original signalling
- [ ] Original interlocking table
