# **AutomatonElvish15: E1 Implementation of Lexical Analysis (Automaton and Regular Expression)**
Automaton and regular expression that recognizes the elvish language

## Description

The provided code defines a Deterministic Finite Automaton (DFA) for recognizing specific words in the Elven language. This language is fictional, originating from fantasy literature such as J.R.R. Tolkien's Middle-earth universe, referred to as a language spoken by elves in that universe (OWTTA, 2022). The modeling technique I decided to use was a DFA for the task of recognizing the language because, firstly, the five words of the Elvish language follow clear rules and patterns, making it easy to model with an automaton. This provides a representation of states and transitions, enabling the lexical analysis of Elven to identify and tokenize words in texts written in this language.

## Model of the Solution

The provided automaton is designed to recognize words in the Elvish language. It consists of several states representing different stages of recognizing a valid Elvish word. The accepted test cases are:

- an
- and
- anca
- anarya
- amil

In order to accept these words, I decided to use a DFA, modeled as follows:
![Automaton](automatonImage.jpg)

This automaton operates with the initial state "start" and two states, "s1" and "s2", which are designated as accepted states. Transitions are defined for each state and input symbol combination. This DFA is designed to accept words like "amil", "an", "anarya", "anca", and "and" from the Elvish language, providing a mechanism for efficient language recognition. The presented automaton is equivalent to the following regular expression:

DFA 1 -> RE 1: 
{^a(mil|n(d|arya|ca)?)$}

## Implementation
The implementation follows the estructure outlined in the "automatonElven15.pl" file. To use the file you can:
- Use the file "testO.pl":
  You need to download "automatonElven15.pl" and "testO.pl", go to the folder where you have downloaded the files, and in the Command Prompt, you have to make the query of the testO file and call the test function *run_test.* When you do this, the test cases will execute automatically and mark which ones were rejected and which ones were accepted.
- Put the input in the follow format:
  ```
  ?- dfa("amil").
  ```
  And the program should return "Accepted" if the string is one of the five words accepteded or "Rejected" if the string is not part of the language.

Both can be done from the terminal or from the SWI-Prolog application.

Some examples of inputs and outputs are: 
 
  dfa("anasn").  -> [a,n,a,s,n] Rejected 
                     false.
                     
  dfa("an").  -> [a,n] Accepted 
                  true.
                  
  dfa("anarya").  -> [a,n,a,r,y,a] Accepted 
                      true.
                      
  dfa("aamila").  -> [a,a,m,i,l,a] Rejected 
                     false.

Here's a breakdown of how it works:

- **States definition:** The automaton defines multiple states, including a starting state (start) and several intermediary states (s0 to s8).

- **Initial state:** The starting state is defined as 'start', indicating the initial point.

- **Accepted states:** States 's1' and 's2' are marked as accepted states, indicating that reaching these states signifies the successful recognition of an Elvish word.

- **Transitions:** Transitions between states are defined based on the input characters.

- **Acceptance function:** Defines the acceptance criteria for the input string. If the current state is an accepted state and the input string is empty, the word is accepted as an Elvish word.

- **Aux Function:** Initializes the acceptance process by starting from the initial state and recursively traversing the transitions based on the input characters.

- **DFA Function:** Converts a given string into a list of characters and initiates the acceptance process for each string. If the string is accepted, it returns true; otherwise, false.

## Tests
The file tests.txt contains all the cases tested for the automaton.

## Analysis
The complexity of this code primarily depends on the length of the input string and the number of transitions required to process it. Since Prolog operates on a non-deterministic basis and explores all possible paths, the complexity can be high for larger input strings or automata with many states and transitions. However, the complexity can be bounded by the size of the automaton and the length of the input string. The overall complexity of this is $O(n)$, where n is the length of the input string, because the program processes the input character by character, transitioning between states. This is equivalent to the next code:

```python
for element in list:  # Through the list
    print(element)
```

## References
[^1]: OWTTA (2022). Elvish languages. One Wiki to Rule Them All. The Lord of the Rings Wiki (https://lotr.fandom.com/wiki/Elvish_languages)
