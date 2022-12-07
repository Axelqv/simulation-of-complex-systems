close all
clear all
clc
L = 100;
N = 1000;
infectedProb = 0.01;


% Initialize lattice


Initlattice = zeros(N,3);
for n = 1:N
    coord = randi(L,1,2);
    x = coord(1);
    y = coord(2);
    Initlattice(n,1) = x;
    Initlattice(n,2) = y;
    Initlattice(n,3) = 1;
    if (n > (N - N*infectedProb))
        Initlattice(n,3) = 2;
    end
end






