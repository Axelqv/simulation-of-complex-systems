function lattice = Move(lattice, d)
    newLattice = lattice;
    for i = 1:length(lattice)
        for j = 1:length(lattice)
            numberOfAgents = size(lattice{i,j}, 2);
            for n = 1:numberOfAgents
                r = rand();
                if (d > r)
                    savedAgent = lattice{i,j}(1);
                    lattice{i,j}(1) = [];
                    newLattice{i, j}(1) = [];
                    dir = randi(4);
                    if (dir == 1)
                        if (j == 1)
                            newLattice{i, end} = [newLattice{i, end}, savedAgent];
                        else
                            newLattice{i, j-1} = [newLattice{i, j-1}, savedAgent];
                        end
                    elseif (dir == 2)
                        if (j == length(lattice))
                            newLattice{i, 1} = [newLattice{i, 1}, savedAgent];
                        else
                            newLattice{i, j+1} = [newLattice{i, j+1}, savedAgent];
                        end
                    elseif (dir == 3)
                        if (i == 1)
                            newLattice{end, j} = [newLattice{end, j}, savedAgent];
                        else
                            newLattice{i-1, j} = [newLattice{i-1, j}, savedAgent];
                        end
                    elseif (dir == 4)
                        if (i == length(lattice))
                            newLattice{1, j} = [newLattice{1, j}, savedAgent];
                        else
                            newLattice{i+1, j} = [newLattice{i+1, j}, savedAgent];
                        end
                    end

                     newLattice{x, y} = [newLattice{x, y}, savedAgent];
                end
            end
        end
    end
    lattice = newLattice;
end
          