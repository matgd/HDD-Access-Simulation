HDD-Access-Simulation
===
This program simulates work of Hard Drive depending of the algorithm.  

List of used algorithms:
---
- FCFS
- SSTF
- SCAN
- CSCAN
- LOOK
- CLOOK    

Program reades requests from the file called <i>"callouts.txt"</i>  
In each line there is a single request.  
Request is an integer from MIN to MAX.
First "block" of the HDD is '1' but you decide about MAX (program asks you) so mind about that when generating requests.  
You can generate them with help of my other Python program <i>int-txt-generator</i>.  
Example "callouts.txt" file is in repository. The numbers in there don't reach above 5000.    

Program calculates travel distance of HDD's head, and time.  

Here's an example of running the program:  
---
Write 'MAX' size of HDD: <b>5000</b>       <i># Block range in HDD is 1 - 5000.</i>    
Write 'TIME_PER_BLOCK': <b>0.1</b>         <i># Reads double. Head's speed defined by time per block.</i>    
Write 'HEAD_START' position: <b>2500</b>   <i># Starting position of HDD's head.</i>    
Write 'DATA_PROCESS_TIME': <b>10</b>       <i># When data is being processed (head reaches request) adds given time.</i>    
  
==== FCFS - Results ====  
Total course:  4307					<i># Total travel distance.</i>  
Total time:    630.7				<i># Total executing time.</i>    
  
==== SSTF - Results ====  
Total course:  2469  
Total time:    446.9  
  
==== SCAN - Results ====  
Total course:  2499  
Total time:    449.9  
  
==== C-SCAN - Results ====  
Total course:  2499  
Total time:    449.9  
  
==== LOOK - Results ====  
Total course:  2469  
Total time:    446.9  
  
==== C-LOOK - Results ====  
Total course:  2469  
Total time:    446.9  

