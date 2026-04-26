% Parent Relationships
parent(mary, mike).
parent(mary, lucy).
parent(john, mike).
parent(john, lucy).
parent(mike, tom).
parent(mike, anna).
parent(susan, tom).
parent(susan, anna).
parent(lucy, alex).

% Gender
male(john).
male(mike).
male(tom).
male(alex).

female(mary).
female(susan).
female(lucy).
female(anna).

% Rules
father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

ancestor(A, D) :- parent(A, D).
ancestor(A, D) :- parent(A, X), ancestor(X, D).
