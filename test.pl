% Author: Monica Monserrat Martinez Vasquez
% Date: March 30, 2024
% Project: DFA Test
% Purpose of the project: Test if the DFA works.

% Alphabet = {a,n,m,i,l,d,r,y,c}
% Accepted words = {an, and, anca, anarya, amil}
:-['automatonElven15'].

% Case 1: word aksjd. This test case is to check if the first letter is a
%         and everything else is wrong.
% Ouput should be false
testRejected1 :-
    write("Must be false: "),
    dfa('aksjd').

% Case 2: word kaja. This test case is to check if the first letter is wrong.
% Ouput should be false
testRejected2 :-
    write("Must be false: "),
    dfa('kaja').

% Case 3: word aa. This test case is to check if the first and the second
%         letter are a.
% Ouput should be false.
testRejected3 :-
    write("Must be false: "),
    dfa('aa').

% Case 4: word amila. This test case is to check if the last letter is wrong.
% Ouput should be false
testRejected4 :-
    write("Must be false: "),
    dfa('amila').

% Case 5: word benji. This test case is to check if all the letters
%         are wrong.
% Ouput should be false
testRejected5 :-
    write("Must be false: "),
    dfa('benji').

% Case 6: word benji. This test case is to check if all the letters
%         are wrong.
% Ouput should be false
testRejected6 :-
    write("Must be false: "),
    dfa('mon').

% Case 7: word benji. This test case is to check if only one letter
%         is wrong.
% Ouput should be false
testRejected7 :-
    write("Must be false: "),
    dfa('anna').

% Case 8: word kilo. This test case is to check if all the letters
%         are wrong.
% Ouput should be false
testRejected8 :-
    write("Must be false: "),
    dfa('kilo').

% Case 9: word hello. This test case is to check if all the letters
%         are wrong.
% Ouput should be false
testRejected9 :-
    write("Must be false: "),
    dfa('hello').

% Case 10: word hello. This test case is to check if all the letters
%         are wrong.
% Ouput should be false
testRejected10 :-
    write("Must be false: "),
    dfa('pals').

% Case 11: word an. This test case is to check an accepted word.
% Ouput should be true
testAccepted1 :-
    write("Must be true: "),
    dfa('an').

% Case 12: word and. This test case is to check an accepted word.
% Ouput should be true
testAccepted2 :-
    write("Must be true: "),
    dfa('and').

% Case 13: word anca. This test case is to check an accepted word.
% Ouput should be true
testAccepted3 :-
    write("Must be true: "),
    dfa('anca').

% Case 14: word anarya. This test case is to check an accepted word.
% Ouput should be true
testAccepted4 :-
    write("Must be true: "),
    dfa('anarya').

% Case 15: word amil. This test case is to check an accepted word.
% Ouput should be true
testAccepted5 :-
    write("Must be true: "),
    dfa('amil').