#pip install Flask
#pip install -U Flask-SQLAlchemy
#pip install Jinja2
from flask import Flask, render_template

# create the app
app = Flask(__name__)

facebook_interview_questions = [
    [
        "Reverse a string.",
        ["A) Using a loop", "B) Using recursion", "C) Using built-in functions", "D) Using stack"]
    ],
    [
        "Find the missing number in an array of integers from 1 to N.",
        ["A) Sort and search", "B) Use XOR", "C) Mathematical formula", "D) Use a hash set"]
    ],
    [
        "Implement an algorithm to check if a string has all unique characters.",
        ["A) Brute force method", "B) Use a hash set", "C) Sorting", "D) Bit manipulation"]
    ],
    [
        "Given two strings, write a method to decide if one is a permutation of the other.",
        ["A) Sort and compare", "B) Use hash maps", "C) Character count arrays", "D) XOR the strings"]
    ],
    [
        "Reverse a linked list.",
        ["A) Iterative approach", "B) Recursive approach", "C) Using stacks", "D) Using pointers"]
    ],
    [
        "Find the longest substring without repeating characters.",
        ["A) Sliding window approach", "B) Hash set and two pointers", "C) Dynamic programming", "D) Brute force method"]
    ],
    [
        "Implement a stack using arrays/linked lists.",
        ["A) Using arrays with dynamic resizing", "B) Using linked list nodes", "C) Using queues", "D) Using hash maps"]
    ],
    [
        "Determine if a given number is a power of two.",
        ["A) Bit manipulation", "B) Using modulus operation", "C) Prime factorization", "D) Recursive approach"]
    ],
    [
        "Given a matrix, rotate it by 90 degrees.",
        ["A) Transpose and reverse rows", "B) Using extra memory", "C) Simulating the rotation", "D) In-place rotation"]
    ],
    [
        "Find the kth largest element in an array.",
        ["A) Sorting and indexing", "B) Use min/max heap", "C) Quickselect algorithm", "D) Use hash maps"]
    ],
    [
        "Implement a binary search tree (BST) and its basic operations.",
        ["A) Insert, delete, search", "B) Using arrays", "C) Breadth-first search", "D) Using stacks"]
    ],
    [
        "Merge two sorted arrays into a single sorted array.",
        ["A) Using extra space", "B) Merge and sort", "C) Two-pointer approach", "D) Using binary search"]
    ],
    [
        "Given an array, find the maximum subarray sum.",
        ["A) Brute force method", "B) Kadane's algorithm", "C) Divide and conquer", "D) Using hash maps"]
    ],
    [
        "Write a function to implement a basic calculator.",
        ["A) Using stacks", "B) Recursive descent parsing", "C) Using regular expressions", "D) Reverse Polish notation"]
    ],
    [
        "Check if a string is a palindrome.",
        ["A) Using two pointers", "B) Reversing the string", "C) Stack and queue comparison", "D) Using regular expressions"]
    ]
]

facebook_interview_answers = ['B', 'C', 'B', 'C', 'A', 'A', 'B', 'A', 'D', 'C', 'A', 'C', 'B', 'A', 'A']

apple_interview_questions = [
    [
        "What is the time complexity of the quicksort algorithm?",
        ["A) O(n log n)", "B) O(n^2)", "C) O(n)", "D) O(log n)"]
    ],
    [
        "What data structure is best suited for implementing a LIFO (Last-In-First-Out) structure?",
        ["A) Queue", "B) Stack", "C) Linked List", "D) Tree"]
    ],
    [
        "Which search algorithm requires the array to be sorted beforehand?",
        ["A) Binary Search", "B) Linear Search", "C) Depth-First Search", "D) Breadth-First Search"]
    ],
    [
        "What is an AVL tree used for?",
        ["A) To store key-value pairs", "B) To implement priority queues", "C) For sorting elements", "D) For self-balancing"]
    ],
    [
        "Which sorting algorithm works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order?",
        ["A) Bubble Sort", "B) Merge Sort", "C) Heap Sort", "D) Insertion Sort"]
    ],
    [
        "What is the purpose of a hash table?",
        ["A) To store data in a sorted manner", "B) To eliminate collisions", "C) To efficiently retrieve and store data", "D) To perform mathematical operations"]
    ],
    [
        "Which of the following is not a type of queue?",
        ["A) Circular Queue", "B) Priority Queue", "C) Linear Queue", "D) Random Queue"]
    ],
    [
        "What is the space complexity of a binary search algorithm?",
        ["A) O(n)", "B) O(log n)", "C) O(n log n)", "D) O(1)"]
    ],
    [
        "What is the purpose of the Dijkstra algorithm?",
        ["A) To find the shortest path in a weighted graph", "B) To sort arrays efficiently", "C) To balance binary trees", "D) To perform encryption"]
    ],
    [
        "Which data structure is typically used for breadth-first search and depth-first search algorithms?",
        ["A) Queue", "B) Stack", "C) Linked List", "D) Array"]
    ],
    [
        "What does the term 'asymptotic analysis' in algorithm analysis refer to?",
        ["A) Analyzing algorithms based on their average-case performance", "B) Analyzing algorithms based on their best-case performance", "C) Analyzing algorithms based on their worst-case performance", "D) Analyzing algorithms based on fixed input sizes"]
    ],
    [
        "Which of the following is an example of a divide and conquer algorithm?",
        ["A) Quick Sort", "B) Bubble Sort", "C) Insertion Sort", "D) Selection Sort"]
    ],
    [
        "In terms of trees, what do 'depth' and 'height' refer to?",
        ["A) Number of edges in the tree", "B) Number of nodes in the tree", "C) Distance between nodes", "D) Levels in the tree"]
    ],
    [
        "What is the role of the 'head' in a linked list?",
        ["A) It points to the middle node", "B) It points to the last node", "C) It points to the first node", "D) It's a pointer to a random node"]
    ],
    [
        "What's the difference between an array and a linked list in terms of memory allocation?",
        ["A) Arrays allocate memory dynamically", "B) Arrays have elements scattered in memory", "C) Linked lists allocate contiguous memory", "D) Linked lists have fixed size allocation"]
    ]
]

apple_answers = ['A', 'A', 'A', 'D', 'A', 'C', 'D', 'B', 'A', 'A', 'C', 'A', 'B', 'C', 'B']

# Questions with answer options
amazon_interview_questions = [
    [
        "Reverse a Linked List.",
        [
            ["A) Using Recursion", "B) Using Iteration", "C) Using Stack", "D) All of the above"],
        ]
    ],
    [
        "Find the maximum element in a Stack.",
        [
            ["A) Iterating through stack", "B) Using a temporary stack", "C) Storing max as a variable", "D) All of the above"],
        ]
    ],
    [
        "Implement a Queue using Stacks.",
        [
            ["A) Using two stacks", "B) Using a single stack", "C) Using arrays", "D) Using a linked list"],
        ]
    ],
    [
        "Check if a string is a palindrome.",
        [
            ["A) Using two pointers", "B) Reversing the string", "C) Using a stack", "D) Comparing characters"],
        ]
    ],
    [
        "Find the intersection point of two Linked Lists.",
        [
            ["A) Using two pointers", "B) Storing nodes in a hash table", "C) Traversing both lists", "D) Reversing the lists"],
        ]
    ],
    [
        "Given a sorted array, create a balanced Binary Search Tree (BST).",
        [
            ["A) Iterative approach", "B) Recursive approach", "C) Using a queue", "D) Using a hash map"],
        ]
    ],
    [
        "Find the first non-repeated character in a string.",
        [
            ["A) Using a hash map", "B) Counting characters", "C) Sorting the string", "D) Traversing the string"],
        ]
    ],
    [
        "Implement an LRU (Least Recently Used) Cache.",
        [
            ["A) Using arrays", "B) Using a doubly linked list", "C) Using a hash map", "D) Using a queue"],
        ]
    ],
    [
        "Rotate an array to the right by k steps.",
        [
            ["A) Reversing the array", "B) Using additional space", "C) Using cyclic replacements", "D) Shifting elements"],
        ]
    ],
    [
        "Merge two sorted arrays.",
        [
            ["A) Using an extra array", "B) Merging in-place", "C) Sorting after merging", "D) Using a priority queue"],
        ]
    ],
    [
        "Determine if a binary tree is height-balanced.",
        [
            ["A) Counting height recursively", "B) Using a stack", "C) Traversing the tree", "D) Storing depth in a list"],
        ]
    ],
    [
        "Count the number of islands in a 2D grid.",
        [
            ["A) Using DFS (Depth-First Search)", "B) Using BFS (Breadth-First Search)", "C) Union-Find Algorithm", "D) Greedy approach"],
        ]
    ],
    [
        "Given a matrix, spiral order the elements.",
        [
            ["A) Using recursion", "B) Iterating through matrix", "C) Using queues", "D) Rotating the matrix"],
        ]
    ],
    [
        "Reverse words in a string.",
        [
            ["A) Using split and join", "B) Reversing each word", "C) Using a stack", "D) Iterating through characters"],
        ]
    ],
    [
        "Implement a binary search algorithm.",
        [
            ["A) Recursive approach", "B) Iterative approach", "C) Using hash map", "D) Using queue"],
        ]
    ],
]

# Correct Answers
amazon_interview_answers = [
    "D", "C", "A", "D", "B", "B", "A", "B", "C", "A", "A", "C", "B", "A", "B"
]


netflix_interview_questions = [
    [
        "1. What data structures would you use to create a spell checker?",
        ["A. Hash table", "B. Trie", "C. Linked List", "D. Stack"]
    ],
    [
        "2. How would you design a system to efficiently serve recommendations to millions of users in real-time?",
        ["A. Using machine learning algorithms", "B. Implementing a distributed system", "C. Caching strategies", "D. Using collaborative filtering"]
    ],
    [
        "3. Explain the concept of caching and its applications in system design?",
        ["A. Reducing latency by storing frequently accessed data", "B. Managing memory efficiently", "C. Load balancing", "D. Database sharding"]
    ],
    [
        "4. Describe the CAP theorem and its implications in distributed systems?",
        ["A. Consistency, Availability, Partition tolerance", "B. Eventual consistency", "C. Network congestion handling", "D. System synchronization"]
    ],
    [
        "5. How would you implement a rate limiter for API requests in a distributed system?",
        ["A. Using token buckets", "B. Load balancing techniques", "C. Implementing queues", "D. Database indexing"]
    ],
    [
        "6. Discuss the advantages and disadvantages of microservices architecture?",
        ["A. Scalability, fault isolation", "B. Increased complexity, network overhead", "C. Monolithic structure", "D. Code reusability"]
    ],
    [
        "7. What is the difference between TCP and UDP? When would you use one over the other?",
        ["A. Connection-oriented vs connectionless", "B. Reliability vs speed", "C. Streaming vs datagrams", "D. Network congestion control"]
    ],
    [
        "8. Explain the concept of sharding in databases and its benefits?",
        ["A. Horizontal partitioning for scalability", "B. Vertical partitioning for security", "C. Query optimization", "D. Indexing techniques"]
    ],
    [
        "9. How would you ensure data consistency in a distributed system?",
        ["A. Using distributed transactions", "B. Implementing distributed locks", "C. Eventual consistency model", "D. Database normalization"]
    ],
    [
        "10. Discuss the differences between synchronous and asynchronous communication in distributed systems?",
        ["A. Blocking vs non-blocking calls", "B. Message passing vs shared memory", "C. Latency handling", "D. Fault tolerance"]
    ],
    [
        "11. Describe the concept of fault tolerance and how it's achieved in a distributed system?",
        ["A. Redundancy and replication", "B. Load balancing strategies", "C. Error detection and correction", "D. Hardware failure prevention"]
    ],
    [
        "12. How would you design a content delivery network (CDN) to optimize media streaming?",
        ["A. Edge caching and server distribution", "B. Network protocols optimization", "C. Quality of Service (QoS) monitoring", "D. Packet filtering"]
    ],
    [
        "13. Discuss the challenges and solutions for handling massive traffic spikes in a web service?",
        ["A. Implementing auto-scaling", "B. Using load balancers", "C. Content delivery network (CDN)", "D. Application-level caching"]
    ],
    [
        "14. Explain the concept of consistent hashing and its role in distributed systems?",
        ["A. Balancing load in distributed systems", "B. Preventing network congestion", "C. Achieving uniform data distribution", "D. Data encryption techniques"]
    ],
    [
        "15. How would you optimize a system’s database to handle a massive amount of read-heavy requests?",
        ["A. Using read replicas", "B. Database denormalization", "C. Implementing caching layers", "D. Load balancing the database"]
    ]
]

netflix_interview_answers = [
    "B", "B", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"
]

google_interview_questions = [
    [
        "Reverse a linked list.",
        [
            "A) Using iteration",
            "B) Using recursion",
            "C) Using stacks",
            "D) Using queues"
        ]
    ],
    [
        "Implement a binary search algorithm.",
        [
            "A) Pythonic approach",
            "B) Iterative solution",
            "C) Recursive approach",
            "D) Linear search"
        ]
    ],
    [
        "Find the missing number in an array of integers from 1 to n.",
        [
            "A) Sorting the array first",
            "B) Using a hash map",
            "C) Using bitwise XOR",
            "D) Brute-force approach"
        ]
    ],
    [
        "Given two strings, write a method to decide if one is a permutation of the other.",
        [
            "A) Sorting and comparing the strings",
            "B) Using hash maps",
            "C) Checking for equal lengths",
            "D) Using sets"
        ]
    ],
    [
        "Implement a stack using arrays or linked lists.",
        [
            "A) Linked list with a tail pointer",
            "B) Linked list with a head pointer",
            "C) Array with dynamic resizing",
            "D) Array with fixed size"
        ]
    ],
    [
        "Write a function to check if a string is a palindrome.",
        [
            "A) Iterative approach",
            "B) Recursive solution",
            "C) Using stacks",
            "D) Using two pointers"
        ]
    ],
    [
        "Implement an algorithm to determine if a string has all unique characters.",
        [
            "A) Using sets",
            "B) Sorting the string",
            "C) Brute-force approach",
            "D) Checking ASCII values"
        ]
    ],
    [
        "Given a sorted array, create a balanced binary search tree.",
        [
            "A) Using the middle element as the root",
            "B) Constructing recursively",
            "C) Using hash maps",
            "D) Sorting the array"
        ]
    ],
    [
        "Find the intersection of two arrays.",
        [
            "A) Using sets",
            "B) Sorting the arrays",
            "C) Hash map approach",
            "D) Two-pointer technique"
        ]
    ],
    [
        "Given a string, compress it by shortening consecutive character sequences.",
        [
            "A) Using a hash map",
            "B) Iterating and checking for duplicates",
            "C) Brute-force compression",
            "D) Using regular expressions"
        ]
    ],
    [
        "Implement a queue using stacks.",
        [
            "A) Single stack approach",
            "B) Double stack approach",
            "C) Using recursion",
            "D) Circular queue"
        ]
    ],
    [
        "Merge two sorted linked lists into a single sorted list.",
        [
            "A) Iterative approach",
            "B) Recursive solution",
            "C) Using additional space",
            "D) Comparing element by element"
        ]
    ],
    [
        "Write an algorithm to perform string matching.",
        [
            "A) Naive pattern searching",
            "B) Using regular expressions",
            "C) Rabin-Karp algorithm",
            "D) Knuth-Morris-Pratt algorithm"
        ]
    ],
    [
        "Given a matrix, rotate it by 90 degrees.",
        [
            "A) Using extra space",
            "B) In-place rotation",
            "C) Transpose and reverse",
            "D) Rotate layer by layer"
        ]
    ],
    [
        "Write a program to find the kth largest element in an unsorted array.",
        [
            "A) Quickselect algorithm",
            "B) Sorting the array",
            "C) Using heaps",
            "D) Linear search"
        ]
    ]
]

google_interview_answers = [
    "B", "B", "C", "A", "A", "D", "A", "B", "D", "B", "B", "D", "A", "B", "A"
]

FAANG = ['Meta', 'Apple', 'Amazon', 'Netflix', 'Google']

@app.route('/meta')
@app.route('/meta/<int:number><answer>')
def meta(number=0, answer=None):
    if answer == 'None':
        answer = None
    next_title = 'meta'
    current_QandA = facebook_interview_questions[number]
    current_question = current_QandA[0]
    current_answer_choices = current_QandA[1]
    the_actual_answer = facebook_interview_answers
    the_user_answer = answer

    return render_template("main_web.html", interview_questions=current_question, interview_questions_choices = current_answer_choices, interview_answers=the_actual_answer[number], the_title = 'Meta', number=number, next_title = next_title, the_user_answer = the_user_answer )

@app.route('/apple')
@app.route('/apple/<int:number><answer>')
def apple(number=0, answer=None):
    if answer == 'None':
        answer = None
    next_title = 'apple'
    current_QandA = apple_interview_questions[number]
    current_question = current_QandA[0]
    current_answer_choices = current_QandA[1]
    the_actual_answer = apple_answers
    the_user_answer = answer
    return render_template("main_web.html", interview_questions=current_question, interview_questions_choices = current_answer_choices, interview_answers=the_actual_answer[number], the_title = 'Meta', number=number, next_title = next_title, the_user_answer = the_user_answer )

@app.route('/amazon')
@app.route('/amazon/<int:number><answer>')
def amazon(number=0, answer=None):
    if answer == 'None':
        answer = None
    next_title = 'amazon'
    current_QandA = amazon_interview_questions[number]
    current_question = current_QandA[0]
    current_answer_choices = current_QandA[1]
    the_actual_answer = amazon_interview_answers
    the_user_answer = answer
    return render_template("main_web.html", interview_questions=current_question, interview_questions_choices = current_answer_choices, interview_answers=the_actual_answer[number], the_title = 'Meta', number=number, next_title = next_title, the_user_answer = the_user_answer )

@app.route('/netflix')
@app.route('/netflix/<int:number><answer>')
def netflix(number=0, answer=None):
    if answer == 'None':
        answer = None
    next_title = 'netflix'
    current_QandA = netflix_interview_questions[number]
    current_question = current_QandA[0]
    current_answer_choices = current_QandA[1]
    the_actual_answer = netflix_interview_answers
    the_user_answer = answer
    return render_template("main_web.html", interview_questions=current_question, interview_questions_choices = current_answer_choices, interview_answers=the_actual_answer[number], the_title = 'Meta', number=number, next_title = next_title, the_user_answer = the_user_answer )

@app.route('/google')
@app.route('/google/<int:number><answer>')
def google(number=0, answer=None):
    if answer == 'None':
        answer = None
    next_title = 'google'
    current_QandA = google_interview_questions[number]
    current_question = current_QandA[0]
    current_answer_choices = current_QandA[1]
    the_actual_answer = google_interview_answers
    the_user_answer = answer

    return render_template("main_web.html", interview_questions=current_question, interview_questions_choices = current_answer_choices, interview_answers=the_actual_answer[number], the_title = 'Meta', number=number, next_title = next_title, the_user_answer = the_user_answer )


@app.route('/')
def welcome_page():
    return render_template('welcome_page.html')

if __name__ == '__main__':
    app.run(debug=True)
