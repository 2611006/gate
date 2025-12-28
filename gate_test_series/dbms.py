# dbms.py

questions = {
    "easy": [
        {"q": "What does SQL stand for?", "options": ["Structured Query Language", "Simple Query Language", "Sequential Query Language", "Standard Query Language"], "correct": "Structured Query Language"},
        {"q": "Which of the following is a characteristic of a DBMS?", "options": ["Data Redundancy", "Data Isolation", "Data Integrity", "Low Security"], "correct": "Data Integrity"},
        {"q": "A row in a database table is also known as a:", "options": ["Attribute", "Tuple", "Relation", "Field"], "correct": "Tuple"},
        {"q": "Which SQL command is used to remove all records from a table but keep the structure?", "options": ["DELETE", "DROP", "TRUNCATE", "REMOVE"], "correct": "TRUNCATE"},
        {"q": "The 'Primary Key' of a table must be:", "options": ["Unique", "Not Null", "Both Unique and Not Null", "Null"], "correct": "Both Unique and Not Null"},
        {"q": "Which of the following is a DDL command?", "options": ["SELECT", "INSERT", "CREATE", "UPDATE"], "correct": "CREATE"},
        {"q": "What is the full form of ACID in databases?", "options": ["Atomicity, Consistency, Isolation, Durability", "Access, Control, Integrity, Data", "Atomicity, Columnar, Index, Data", "Auto, Command, Input, Delete"], "correct": "Atomicity, Consistency, Isolation, Durability"},
        {"q": "In a relational model, a column is called an:", "options": ["Entity", "Attribute", "Tuple", "Domain"], "correct": "Attribute"},
        {"q": "Which command is used to save changes permanently in a database?", "options": ["SAVE", "ROLLBACK", "COMMIT", "GRANT"], "correct": "COMMIT"},
        {"q": "A database schema is:", "options": ["Data in the database", "The logical structure of the database", "A query language", "A table row"], "correct": "The logical structure of the database"}
    ],
    "medium": [
        {"q": "Which Normal Form handles the removal of partial functional dependencies?", "options": ["1NF", "2NF", "3NF", "BCNF"], "correct": "2NF"},
        {"q": "What is the purpose of a Foreign Key?", "options": ["To uniquely identify a row", "To establish a link between two tables", "To index a column", "To prevent null values"], "correct": "To establish a link between two tables"},
        {"q": "In ER Diagrams, a double rectangle represents a:", "options": ["Strong Entity", "Weak Entity", "Derived Attribute", "Relationship"], "correct": "Weak Entity"},
        {"q": "Which join returns all rows from the left table and matched rows from the right table?", "options": ["Inner Join", "Right Join", "Left Join", "Full Join"], "correct": "Left Join"},
        {"q": "What is 'Functional Dependency'?", "options": ["Dependency between rows", "Relationship between attributes", "Dependency on hardware", "A type of database security"], "correct": "Relationship between attributes"},
        {"q": "The 'Group By' clause is used in conjunction with:", "options": ["DDL commands", "Aggregate functions", "Foreign keys", "Primary keys"], "correct": "Aggregate functions"},
        {"q": "Which of the following ensures that a transaction is all-or-nothing?", "options": ["Consistency", "Isolation", "Atomicity", "Durability"], "correct": "Atomicity"},
        {"q": "A 'View' in SQL is:", "options": ["A physical table", "A virtual table based on a query", "A backup of a table", "A database user"], "correct": "A virtual table based on a query"},
        {"q": "Which operator is used for pattern matching in SQL?", "options": ["BETWEEN", "LIKE", "EXISTS", "MATCH"], "correct": "LIKE"},
        {"q": "The degree of a relation refers to the number of:", "options": ["Rows", "Tables", "Attributes", "Keys"], "correct": "Attributes"}
    ],
    "hard": [
        {"q": "A schedule is 'Conflict Serializable' if its precedence graph is:", "options": ["Cyclic", "Acyclic", "Complete", "Connected"], "correct": "Acyclic"},
        {"q": "Which of the following is strictly stronger than 3NF?", "options": ["2NF", "BCNF", "1NF", "None of these"], "correct": "BCNF"},
        {"q": "In a B+ tree, where are the actual data pointers or records stored?", "options": ["In the root node", "In internal nodes", "In leaf nodes only", "In all nodes"], "correct": "In leaf nodes only"},
        {"q": "The 'Log-Based Recovery' method uses which of the following to recover from a crash?", "options": ["Redo and Undo operations", "Indexes", "Primary Keys", "Shadow Paging only"], "correct": "Redo and Undo operations"},
        {"q": "Which lock mode allows multiple transactions to read a data item simultaneously?", "options": ["Exclusive (X) Lock", "Shared (S) Lock", "Intent Lock", "Deadlock"], "correct": "Shared (S) Lock"},
        {"q": "What is 'Lossless Join' property used to check?", "options": ["Table size", "Decomposition quality", "Query speed", "Data security"], "correct": "Decomposition quality"},
        {"q": "The 'Cascading Rollback' problem is avoided in which type of schedules?", "options": ["Non-recoverable", "Cascaleless", "Unserializable", "Strict"], "correct": "Cascaleless"},
        {"q": "In SQL, the 'HAVING' clause is different from 'WHERE' because:", "options": ["HAVING is for rows, WHERE is for columns", "HAVING is used with grouped data", "WHERE is only for Primary Keys", "They are the same"], "correct": "HAVING is used with grouped data"},
        {"q": "The number of tuples in a relation is called its:", "options": ["Degree", "Cardinality", "Domain", "Schema"], "correct": "Cardinality"},
        {"q": "Two-Phase Locking (2PL) protocol ensures:", "options": ["No Deadlocks", "Serializability", "High Availability", "No Cascading Rollbacks"], "correct": "Serializability"}
    ]
}