def easy_question(num):
    easy_question_bank = {
        # Current Affairs (India)
        1: "Who is the current Prime Minister of India?",
        2: "Which state in India is known as the 'Land of Five Rivers'?",
        3: "What is the capital of India?",
        4: "Which Indian city is known as the 'Silicon Valley of India'?",
        5: "Who is the current President of India?",
        # General Knowledge (India)
        6: "What is the national sport of India?",
        7: "What is the national bird of India?",
        8: "What is the national flower of India?",
        9: "What is the national animal of India?",
        10: "What is the currency of India?",
        # Technology
        11: "What does 'H' stand for in HTTP?",
        12: "What does 'U' stand for in URL?",
        13: "Which company developed the Windows operating system?",
        14: "What does 'A' stand for in AI?",
        15: "What does 'C' stands for in CPU?",
        # Programming (C/C++/Python/Java)
        16: "Which programming language is known as the 'mother of all languages'?",
        17: "What is the file extension for Python files?",
        18: "Which keyword is used to define a function in Python?",
        19: "Which programming language is used for Android development?",
        20: "What does  the first 'O' stand for in OOP?",
    }
    return easy_question_bank[num]

def hard_question(num):
    hard_question_bank = {
        # Current Affairs (India)
        21: "Who is the current Chief Justice of India?",
        22: "Which Indian state has the highest literacy rate?",
        23: "Which Indian state has the largest area?",
        24: "Which Indian state has the highest population?",
        25: "Who is the current Finance Minister of India?",
        # General Knowledge (India)
        26: "Who wrote the Indian National Anthem?",
        27: "What is the national river of India?",
        28: "Which Indian city is known as the 'City of Joy'?",
        29: "Which Indian city is known as the 'Pink City'?",
        30: "Which Indian state is known as the 'Spice Garden of India'?",
        # Technology
        31: "What does 'I' stand for IP in networking?",
        32: "What does 'D' stand for in DNS?",
        33: "Which company developed the Android operating system?",
        34: "What does 'I' stand forin IOT?",
        35: "What does 'R' stands for in RAM?",
        # Programming (C/C++/Python/Java)
        36: "Which programming language is used for web development?",
        37: "What is the file extension for Java files?",
        38: "Which keyword is used to create a class in Java?",
        39: "Which programming language is used for data analysis?",
        40: "What does 'I' stand for in IDE?",
    }
    return hard_question_bank[num]

def options(num):
    options_bank = {
        # Easy Question Options
        1: ["Narendra Modi", "Rahul Gandhi", " Bhupendra Patel", "Adityanath yogi"],
        2: ["Punjab", "Rajasthan", "Kerala", "Gujarat"],
        3: ["Delhi", "Mumbai", "Chennai", "Kolkata"],
        4: ["Bangalore", "Hyderabad", "Pune", "Chennai"],
        5: ["Murmu", "Kovind", "Mukherjee", "Kalam"],
        6: ["Hockey", "Cricket", "Football", "Badminton"],
        7: ["Peacock", "Sparrow", "Crow", "Pigeon"],
        8: ["Lotus", "Rose", "Lily", "Sunflower"],
        9: ["Tiger", "Lion", "Elephant", "Leopard"],
        10: ["Rupee", "Dollar", "Euro", "Pound"],
        11: ["Hypertext", "Hyperlink", "Hypermedia", "Hyperdata"],
        12: ["Uniform", "Universal", "Unique", "Unified"],
        13: ["Microsoft", "Apple", "Google", "IBM"],
        14: ["Artificial", "Automated", "Advanced", "Augmented"],
        15: ["Central", "Core", "Control", "Compute"],
        16: ["C", "Python", "Java", "C++"],
        17: [".py", ".java", ".cpp", ".cs"],
        18: ["def", "function", "func", "define"],
        19: ["Java", "Kotlin", "Swift", "Dart"],
        20: ["Object", "Oriented", "Programming", "Paradigm"],
        # Hard Question Options
        21: ["Chandrachud", "Gogoi", "Bobde", "Ramana"],
        22: ["Kerala", "Tamil Nadu", "Goa", "Punjab"],
        23: ["Rajasthan", "Madhya Pradesh", "Maharashtra", "Uttar Pradesh"],
        24: ["Uttar Pradesh", "Bihar", "West Bengal", "Maharashtra"],
        25: ["Sitharaman", "Jaitley", "Mukherjee", "Chidambaram"],
        26: ["Tagore", "Nehru", "Gandhi", "Patel"],
        27: ["Ganga", "Yamuna", "Brahmaputra", "Godavari"],
        28: ["Kolkata", "Mumbai", "Delhi", "Chennai"],
        29: ["Jaipur", "Jodhpur", "Udaipur", "Bikaner"],
        30: ["Kerala", "Tamil Nadu", "Karnataka", "Andhra Pradesh"],
        31: ["Internet", "Internal", "Interconnected", "Interim"],
        32: ["Domain", "Data", "Digital", "Dynamic"],
        33: ["Google", "Microsoft", "Apple", "Samsung"],
        34: ["Internet", "Intelligent", "Integrated", "Interactive"],
        35: ["Random ", "Read", "Rapid", "Reliable"],
        36: ["HTML", "Python", "JavaScript", "PHP"],
        37: [".java", ".py", ".cpp", ".cs"],
        38: ["class", "define", "struct", "object"],
        39: ["Python", "R", "SQL", "Java"],
        40: ["Integrated", "Interactive", "Intelligent", "Innovative"],
    }
    return options_bank[num]

def answers(num):
    answers_bank = {
        # Easy Question Correct Answers
        1: "Modi",
        2: "Punjab",
        3: "Delhi",
        4: "Bangalore",
        5: "Murmu",
        6: "Hockey",
        7: "Peacock",
        8: "Lotus",
        9: "Tiger",
        10: "Rupee",
        11: "Hypertext",
        12: "Uniform",
        13: "Microsoft",
        14: "Artificial",
        15: "Central",
        16: "C",
        17: ".py",
        18: "def",
        19: "Java",
        20: "Object",
        # Hard Question Correct Answers
        21: "Chandrachud",
        22: "Kerala",
        23: "Rajasthan",
        24: "Uttar Pradesh",
        25: "Sitharaman",
        26: "Tagore",
        27: "Ganga",
        28: "Kolkata",
        29: "Jaipur",
        30: "Kerala",
        31: "Internet",
        32: "Domain",
        33: "Google",
        34: "Internet",
        35: "Random",
        36: "HTML",
        37: ".java",
        38: "class",
        39: "Python",
        40: "Integrated",
    }
    return answers_bank[num]