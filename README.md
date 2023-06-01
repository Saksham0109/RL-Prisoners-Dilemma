# RL-Prisoners-Dilemma

Prisoner's Dilemma is a famous game theory problem which goes as follows:

Two members of a criminal gang, A and B, are arrested and imprisoned. Each prisoner is in solitary confinement with no means of communication with their partner. The principal charge would lead to a sentence of 7 years in prison; however, the police do not have the evidence for a conviction. They plan to sentence both to 1 years in prison on a lesser charge but offer each prisoner a Faustian bargain:

If one of them confesses to the crime of the principal charge, betraying the other, they will be pardoned and free to leave while the other must serve the entirety of the sentence instead of just 1 years for the lesser charge.
 
This leads to a possible of four different outcomes:

A: If A and B both remain silent, they will each serve the lesser charge of 1 years in prison.

B: If A betrays B but B remains silent, A will be set free while B serves 7 years in prison.

C: If A remains silent but B betrays A, A will serve 7 years in prison and B will be set free.

D: If A and B both betray the other, they share the sentence and serve 3 years.

Economics states choosing to confess is a dominant strategy for both.

In this project,i try and train a RL model on the problem and come up with its solution.