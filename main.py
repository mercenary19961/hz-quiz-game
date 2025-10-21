questions = [
    {
        "question": "What is the output of type({})?",
        "options": ["A) <class 'set'>", "B) <class 'dict'>", "C) <class 'list'>", "D) <class 'tuple'>"],
        "answer": "B",
    },
    {
        "question": "Which of the following creates a list?",
        "options": ["A) ()", "B) {}", "C) []", "D) <>"],
        "answer": "C",
    },
    {
        "question": "What is the result of 3 // 2 in Python?",
        "options": ["A) 1.5", "B) 1", "C) 2", "D) 0"],
        "answer": "B",
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["A) func", "B) def", "C) function", "D) lambda"],
        "answer": "B",
    },
    {
        "question": "What does the expression 'hello' * 3 evaluate to?",
        "options": ["A) Error", "B) 'hello3'", "C) 'hellohellohello'", "D) 3"],
        "answer": "C",
    },
    {
        "question": "Which of these is immutable?",
        "options": ["A) list", "B) dict", "C) set", "D) tuple"],
        "answer": "D",
    },
    {
        "question": "What is the correct way to import the math module?",
        "options": ["A) include math", "B) using math", "C) import math", "D) module math"],
        "answer": "C",
    },
    {
        "question": "What is the output of bool([])?",
        "options": ["A) True", "B) False", "C) []", "D) Error"],
        "answer": "B",
    },
    {
        "question": "Which operator checks for object identity?",
        "options": ["A) ==", "B) is", "C) in", "D) !="],
        "answer": "B",
    },
    {
        "question": "What is the result of len({'a':1,'b':2,'c':3})?",
        "options": ["A) 6", "B) 3", "C) 2", "D) 1"],
        "answer": "B",
    },
    {
        "question": "Which statement is used to handle exceptions?",
        "options": ["A) try/except", "B) do/catch", "C) attempt/rescue", "D) guard/handle"],
        "answer": "A",
    },
    {
        "question": "What is the output of list(range(2, 7, 2))?",
        "options": ["A) [2, 3, 4, 5, 6, 7]", "B) [2, 4, 6]", "C) [2, 5]", "D) [3, 5, 7]"],
        "answer": "B",
    },
    {
        "question": "How do you write a single-line comment?",
        "options": ["A) // comment", "B) <!-- comment -->", "C) # comment", "D) /* comment */"],
        "answer": "C",
    },
    {
        "question": "Which built-in function returns an iterator of paired items from two iterables?",
        "options": ["A) pair()", "B) join()", "C) zip()", "D) map()"],
        "answer": "C",
    },
    {
        "question": "What is the output of '5' + '3'?",
        "options": ["A) 8", "B) '53'", "C) Error", "D) 15"],
        "answer": "B",
    },
    {
        "question": "Which method adds an element to the end of a list?",
        "options": ["A) add()", "B) push()", "C) append()", "D) insert_end()"],
        "answer": "C",
    },
    {
        "question": "Which of these creates a set with elements 1 and 2?",
        "options": ["A) {1, 2}", "B) (1, 2)", "C) [1, 2]", "D) {'1','2'}"],
        "answer": "A",
    },
    {
        "question": "What is the correct file handling mode to append text?",
        "options": ["A) 'r'", "B) 'w'", "C) 'a'", "D) 'x'"],
        "answer": "C",
    },
    {
        "question": "What does the 'pass' statement do?",
        "options": ["A) Skips iteration", "B) Does nothing (placeholder)", "C) Exits function", "D) Raises an error"],
        "answer": "B",
    },
    {
        "question": "Which of these is NOT a valid variable name?",
        "options": ["A) _count", "B) count2", "C) 2count", "D) count_"],
        "answer": "C",
    },
    {
        "question": "Which built-in converts a string to an integer?",
        "options": ["A) toInt()", "B) int()", "C) number()", "D) parseInt()"],
        "answer": "B",
    },
    {
        "question": "What is the output of sum([1,2,3], 10)?",
        "options": ["A) 6", "B) 16", "C) 10", "D) Error"],
        "answer": "B",
    },
    {
        "question": "What does list comprehension [x*x for x in range(3)] produce?",
        "options": ["A) [0, 1, 4]", "B) [1, 4, 9]", "C) [0, 1, 2]", "D) [2, 4, 6]"],
        "answer": "A",
    },
    {
        "question": "Which statement correctly defines a class?",
        "options": ["A) def MyClass:", "B) class MyClass:", "C) type MyClass:", "D) object MyClass:"],
        "answer": "B",
    },
    {
        "question": "What is a correct way to inherit from a base class Base?",
        "options": ["A) class Sub: inherit Base", "B) class Sub(Base):", "C) class Sub -> Base:", "D) class Sub = Base:"],
        "answer": "B",
    },
    {
        "question": "Which decorator is used to define a static method?",
        "options": ["A) @classmethod", "B) @staticmethod", "C) @abstractmethod", "D) @property"],
        "answer": "B",
    },
    {
        "question": "What does the 'with' statement use under the hood?",
        "options": ["A) __enter__ and __exit__", "B) __open__ and __close__", "C) __start__ and __stop__", "D) __in__ and __out__"],
        "answer": "A",
    },
    {
        "question": "What is the output of ','.join(['a','b','c'])?",
        "options": ["A) ['a,b,c']", "B) 'a,b,c'", "C) 'abc'", "D) ['a','b','c']"],
        "answer": "B",
    },
    {
        "question": "Which collection type preserves insertion order (CPython 3.7+)?",
        "options": ["A) set", "B) dict", "C) frozenset", "D) heapq"],
        "answer": "B",
    },
    {
        "question": "What is the difference between '==' and 'is'?",
        "options": ["A) No difference", "B) '==' compares values; 'is' compares identities", "C) '==' compares identities; 'is' compares values", "D) Both compare identities"],
        "answer": "B",
    },
    {
        "question": "Which keyword creates a generator function?",
        "options": ["A) yield", "B) return", "C) generate", "D) async"],
        "answer": "A",
    },
    {
        "question": "What is the output of any([0, '', None, 5])?",
        "options": ["A) True", "B) False", "C) None", "D) Error"],
        "answer": "A",
    },
    {
        "question": "How do you specify a default value for a function parameter?",
        "options": ["A) def f(x := 10):", "B) def f(x = 10):", "C) def f(x default 10):", "D) def f(x:10):"],
        "answer": "B",
    },
    {
        "question": "Which statement about dictionaries is TRUE?",
        "options": ["A) Keys can be lists", "B) Keys must be hashable", "C) Values must be strings", "D) They don't preserve order"],
        "answer": "B",
    },
    {
        "question": "What is the effect of 'break' inside a loop?",
        "options": ["A) Skips to next iteration", "B) Exits the loop", "C) Restarts the loop", "D) Pauses the loop"],
        "answer": "B",
    },
    {
        "question": "What does enumerate(['a','b'], start=1) yield first?",
        "options": ["A) (0, 'a')", "B) (1, 'a')", "C) (1, 'b')", "D) ('a', 1)"],
        "answer": "B",
    },
    {
        "question": "Which exception is raised by int('x')?",
        "options": ["A) TypeError", "B) ValueError", "C) NameError", "D) KeyError"],
        "answer": "B",
    },
    {
        "question": "What is the output of {x for x in 'abca'}?",
        "options": ["A) {'a','b','c','a'}", "B) {'a','b','c'}", "C) ['a','b','c']", "D) ('a','b','c')"],
        "answer": "B",
    },
    {
        "question": "Which import gives 'sqrt' directly?",
        "options": ["A) import math.sqrt", "B) from math import sqrt", "C) using math.sqrt", "D) include sqrt from math"],
        "answer": "B",
    },
    {
        "question": "What does dict.get('k', 0) return if 'k' is missing?",
        "options": ["A) None", "B) 0", "C) ''", "D) Raises KeyError"],
        "answer": "B",
    },
    {
        "question": "Which is a valid list slice of lst?",
        "options": ["A) lst[::]", "B) lst(:)", "C) lst<>", "D) lst{}"],
        "answer": "A",
    },
    {
        "question": "What is the result of sorted({3,1,2})?",
        "options": ["A) {1,2,3}", "B) [1, 2, 3]", "C) (1,2,3)", "D) Error"],
        "answer": "B",
    },
    {
        "question": "Which statement defines a virtual environment with venv from CLI?",
        "options": ["A) python -m env myenv", "B) python -m venv myenv", "C) pip venv myenv", "D) py venv create myenv"],
        "answer": "B",
    },
    {
        "question": "What is the output of print('a', 'b', sep='-')?",
        "options": ["A) a b", "B) a-b", "C) a--b", "D) 'a', 'b'"],
        "answer": "B",
    },
    {
        "question": "Which built-in applies a function to all items and returns an iterator?",
        "options": ["A) apply()", "B) exec()", "C) map()", "D) pair()"],
        "answer": "C",
    },
    {
        "question": "What is the correct way to open a text file with UTF-8 encoding?",
        "options": ["A) open('f.txt')", "B) open('f.txt','r','utf-8')", "C) open('f.txt', encoding='utf-8')", "D) open('f.txt', mode='utf-8')"],
        "answer": "C",
    },
    {
        "question": "Which statement about list vs tuple is TRUE?",
        "options": ["A) Lists are immutable, tuples are mutable", "B) Both are immutable", "C) Lists are mutable, tuples are immutable", "D) Both are mutable"],
        "answer": "C",
    },
    {
        "question": "Which of these is a correct f-string?",
        "options": ["A) f('value is {x}')", "B) f\"value is {x}\"", "C) f[value is {x}]", "D) f{value is x}"],
        "answer": "B",
    },
    {
        "question": "What will [*'ab', *'cd'] evaluate to?",
        "options": ["A) ['ab','cd']", "B) ['a','b','c','d']", "C) [('a','b'),('c','d')]", "D) Error"],
        "answer": "B",
    },
    {
        "question": "Which function returns the memory address identity of an object?",
        "options": ["A) hash()", "B) id()", "C) addr()", "D) ref()"],
        "answer": "B",
    },
    {
        "question": "Which keyword is used to create an iterator class with next()?",
        "options": ["A) __get__", "B) __next__", "C) __call__", "D) __iter__"],
        "answer": "D",
    },
    {
        "question": "Which of the following best describes a decorator?",
        "options": ["A) A function returning a class", "B) A function that takes and returns a function", "C) A class that decorates strings", "D) A context manager"],
        "answer": "B",
    },
]


score = 0
question_number = 1

for q in questions:
    print(f"Question number:{question_number}\n")
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The answer is {q['answer']}.\n")

    question_number += 1
    print(f"Your current score is: {score}/{question_number - 1}\n")

print(f"Quiz finished! Your score: {score}/{len(questions)}")

