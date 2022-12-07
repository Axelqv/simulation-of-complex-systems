function newLattice = NewMove(lattice, d)
    N = length(lattice)
    randomNumbers = rand(N,1);
    index = find(randomNumbers < d);

    movements = [0, 1; 0, -1; ]



  

    