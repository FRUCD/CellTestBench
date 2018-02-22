# CellTestBench
## Operation
First, make sure that the Arduino is plugged into your computer. For Chris, you no longer have to use the same COM port each time. It will figure it out for you :)

Run
```
python read_data_rev_2.py
```
You should see a message confirming that the Arduino was found.

Make sure both power supplies are powered on (the 12v supply is for the timing board, not the Arduino). Press the trigger. This should create a new file. Do not open this file until it is closed by the logging program. The board will be ready to create another new file on a trigger. Repeat 199 more times. 
