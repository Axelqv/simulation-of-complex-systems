function lattice = InitLatticeWithAgents(L, N, infectedProb)

    lattice = cell(L);
    for n = 1:(N - N*infectedProb)
        coord = randi(L,1,2);
        x = coord(1);
        y = coord(2);
        lattice{x, y} = [lattice{x, y}, 1];
        if (n > (N - 2*N*infectedProb))
            lattice{x, y} = [lattice{x, y}, 2];
        end
    end

end




    