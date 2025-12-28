# os.py

questions = {
    "easy": [
        {"q": "What is the primary purpose of an Operating System?", "options": ["To build hardware", "To act as an interface between user and hardware", "To design algorithms", "To create web pages"], "correct": "To act as an interface between user and hardware"},
        {"q": "Which of the following is the 'Heart' of the Operating System?", "options": ["Shell", "Kernel", "Compiler", "Task Manager"], "correct": "Kernel"},
        {"q": "The process of loading the operating system into memory is called:", "options": ["Loading", "Booting", "Starting", "Caching"], "correct": "Booting"},
        {"q": "Which of the following is NOT a state of a process?", "options": ["New", "Running", "Finished", "Waiting"], "correct": "Finished"},
        {"q": "What is a 'Thread' in an OS?", "options": ["A heavy-weight process", "A light-weight process", "A type of hardware", "A storage device"], "correct": "A light-weight process"},
        {"q": "The main memory of a computer is also known as:", "options": ["ROM", "Cache", "RAM", "Hard Disk"], "correct": "RAM"},
        {"q": "Which command in Linux is used to list files in a directory?", "options": ["dir", "ls", "list", "show"], "correct": "ls"},
        {"q": "What is the full form of FIFO?", "options": ["First In First Out", "Fast Input Fast Output", "File Input File Output", "First In Final Out"], "correct": "First In First Out"},
        {"q": "A situation where a process is waiting for an event that will never occur is called:", "options": ["Starvation", "Deadlock", "Interrupt", "Trap"], "correct": "Deadlock"},
        {"q": "Which of the following is a GUI-based Operating System?", "options": ["MS-DOS", "UNIX", "Windows", "All of the above"], "correct": "Windows"}
    ],
    "medium": [
        {"q": "Which scheduling algorithm can lead to the 'Convoy Effect'?", "options": ["Round Robin", "SJF", "FCFS", "Priority Scheduling"], "correct": "FCFS"},
        {"q": "What is 'Thrashing' in memory management?", "options": ["Excessive swapping of pages", "High CPU utilization", "Deleting files", "Formatting the disk"], "correct": "Excessive swapping of pages"},
        {"q": "Which of the following is a technique to handle Deadlocks by ensuring they never occur?", "options": ["Deadlock Detection", "Banker's Algorithm", "Deadlock Recovery", "Mutual Exclusion"], "correct": "Banker's Algorithm"},
        {"q": "In Paging, what is 'Belady’s Anomaly'?", "options": ["Page faults decrease as frames increase", "Page faults increase as frames increase", "Memory access becomes faster", "Memory access becomes slower"], "correct": "Page faults increase as frames increase"},
        {"q": "The interval from the time of submission of a process to the time of completion is:", "options": ["Waiting Time", "Response Time", "Turnaround Time", "Throughput"], "correct": "Turnaround Time"},
        {"q": "What is a 'SemaPhore' used for?", "options": ["Memory allocation", "Process synchronization", "Disk scheduling", "Error detection"], "correct": "Process synchronization"},
        {"q": "Virtual memory is typically implemented by:", "options": ["Demand Paging", "Fragmentation", "Physical Addressing", "Caching"], "correct": "Demand Paging"},
        {"q": "Which disk scheduling algorithm services requests closest to the current head position?", "options": ["FCFS", "SCAN", "SSTF", "C-SCAN"], "correct": "SSTF"},
        {"q": "Internal fragmentation is a problem in which memory management technique?", "options": ["Paging", "Segmentation", "Variable Partitioning", "None"], "correct": "Paging"},
        {"q": "The section of code where a process accesses shared resources is called:", "options": ["Entry Section", "Critical Section", "Exit Section", "Remainder Section"], "correct": "Critical Section"}
    ],
    "hard": [
        {"q": "In the context of the Banker's Algorithm, if Max(i,j) - Allocation(i,j) <= Available(j), the state is:", "options": ["Safe", "Unsafe", "Deadlock", "Depends on other processes"], "correct": "Safe"},
        {"q": "Which of the following is NOT a necessary condition for Deadlock?", "options": ["Mutual Exclusion", "No Preemption", "Hold and Wait", "Preemption"], "correct": "Preemption"},
        {"q": "If a system has 3 processes each needing 2 units of a resource, what is the minimum number of resources to ensure no deadlock?", "options": ["3", "4", "5", "6"], "correct": "4"},
        {"q": "The 'Dining Philosophers' problem is a classic example of:", "options": ["Producer-Consumer", "Synchronization and Deadlock", "Disk Scheduling", "Memory Fragmentation"], "correct": "Synchronization and Deadlock"},
        {"q": "What is the main difference between Paging and Segmentation?", "options": ["Paging is variable-sized; Segmentation is fixed", "Paging is fixed-sized; Segmentation is variable", "Both are fixed-sized", "Both are variable-sized"], "correct": "Paging is fixed-sized; Segmentation is variable"},
        {"q": "In the 'Inverted Page Table' approach, the table is indexed by:", "options": ["Process ID", "Frame Number", "Page Number", "Segment Number"], "correct": "Frame Number"},
        {"q": "Which page replacement algorithm is optimal but impossible to implement in practice?", "options": ["LRU", "FIFO", "Optimal Page Replacement", "MRU"], "correct": "Optimal Page Replacement"},
        {"q": "A 'Zombie' process is a process that has:", "options": ["Finished execution but still has an entry in the process table", "Not yet started", "Been killed by the user", "No parent process"], "correct": "Finished execution but still has an entry in the process table"},
        {"q": "What is the 'TLB' (Translation Lookaside Buffer) used for?", "options": ["Storing process data", "Speeding up virtual to physical address translation", "Disk caching", "Handling interrupts"], "correct": "Speeding up virtual to physical address translation"},
        {"q": "The 'Working Set' model of memory management is used to prevent:", "options": ["Deadlock", "Thrashing", "Fragmentation", "Starvation"], "correct": "Thrashing"}
    ]
}