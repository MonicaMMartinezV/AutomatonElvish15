% Author: Monica Monserrat Martinez Vasquez
% Date: March 31, 2024
% Project: Final automaton (DFA)
% Purpose of the project: Lexical analysis parser using an automaton, which can detect the elven language.

% Definition of states.
state(start).
state(s0).
state(s1).
state(s2).
state(s3).
state(s4).
state(s5).
state(s6).
state(s7).
state(s8).

% Initial state.
initial(start).

% Accepted states.
accepted(s1).
accepted(s2).

% Transitions.
trans(start, 'a', s0).
trans(s0, 'n', s1).
trans(s1, 'd', s2).
trans(s1, 'c', s3).
trans(s3, 'a', s1).
trans(s1, 'a', s4).
trans(s4, 'r', s5).
trans(s5, 'y', s6).
trans(s6, 'a', s1).
trans(s0, 'm', s7).
trans(s7, 'i', s8).
trans(s8, 'l', s1).

% DFA function to convert a string into a list of characters and check its acceptance.
dfa(Str):-
    % This function separates a string into a list of characters.
    atom_chars(Str, Chars),
    aux(Chars),!.

% Check function to start the accept process with the initial state.
aux(Input):-
    initial(InitialState),
    % Print the introduced word.
    write(Input),
    accept(InitialState, Input).

% Verification of string acceptance.
accept(State, []) :-
    accepted(State).

% Separate the Head (or actual character) from a Tail (the rest of
% the characters).
accept(State, [H|T]) :-
    trans(State, H, NextState),
    accept(NextState, T).