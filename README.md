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
