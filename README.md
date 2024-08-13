# ThreadsWithEvents
FSU COP4521: Secure, Parallel, and Distributed Programming Module 11 with Dr. Karen Works

<h2>Description</h2>
This project uses threads with events to calculate the time value of money. There are three threads that take in random interest rates and various numbers of years to calculate future values, and a fourth thread that waits on the other three threads in order to calculate which has the highest future value. 
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b>
- <b>threading</b>
- <b>concurrent.futures</b>
- <b>ThreadPoolExecutor</b>

<h2>Environments Used </h2>

- <b>PyCharm</b>

<h2>Program walk-through:</h2>

<p align="center">
In PyCharm, run the script, and observe the output: <br/>
<img src="https://i.imgur.com/6r4xguw.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
After running again, we can see a different oupput with the new set of randomly generated interest rates:  <br/>
<img src="https://i.imgur.com/6DzbLqb.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Each time we run, new output is generated, and the thread with the most number of payments always has the highest future value: <br/>
<img src="https://i.imgur.com/ubrmhje.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
