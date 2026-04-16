% Exercise A

parent(alex, bella).
parent(alex, carlos).
parent(diana, bella).
parent(diana, carlos).
parent(bella, emma).
parent(frank, emma).
male(alex).
male(carlos).
male(frank).
female(diana).
female(bella).
female(emma).

% Rules
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
mother(X, Y) :- female(X), parent(X, Y).
father(X, Y) :- male(X), parent(X, Y).

/*
Results:

?- sibling(bella, X).
X = carlos.

?- grandparent(X, emma).
X = alex ;
X = diana.

?- mother(X, carlos).
X = diana.
*/

% Exercise B

list_op([], List, List).
list_op([Head|List_1], List_2, [Head|List_3]) :-
	list_op(List_1, List_2, List_3).

/*
Answers:
?- list_op([a,b], [b,c], X).
X = [a, b, b, c].
We are concatenating the two lists, so the result is [a, b] followed by [b, c]

?- list_op(X, Y, [a,b,c]).
X = [], Y = [a, b, c] ;
X = [a], Y = [b, c] ;
X = [a, b], Y = [c] ;
X = [a, b, c], Y = [].
Here, we are finding all possible ways to split the list [a, b, c] 
into two lists X and Y such that concatenating X and Y gives [a, b, c], 
the results show all possible splits of the list
*/


% Exercise C

% Base case, union of empty list with List2 is List2
union_list([], List2, List2).

% If H is already in List2, skip it
union_list([H|T], List2, Result) :-
	member(H, List2),
	union_list(T, List2, Result).

% If H is not in List2, include H in the result
union_list([H|T], List2, [H|Result]) :-
	\+ member(H, List2),
	union_list(T, List2, Result).

/*
Examples

?- union_list([a,b,c], [b,c,d], X).
X = [a, b, c, d].

?- union_list([1,2,2,3], [3,4], X).
X = [1, 2, 2, 3, 4].

*/
