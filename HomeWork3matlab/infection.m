function newLattice = infection(lattice, beta)
    latticeLength = length(lattice);
    for i = 1:latticeLength
        for j = 1:latticeLength
            indexInfected = find(lattice{i, j} == 2);
            if isempty(indexInfected)
                continue
            end
            indexSuceptible = find(lattice{i, j} == 1);
            if isempty(indexSuceptible)
                continue
            end
            for index=indexInfected
                randomNr = rand();
                if randomNr < beta
                    for indexS = indexSuceptible
                        lattice{i, j}(indexS) = 2; % suceptible gets infected
                    end
                end
            end
        end
    end

    newLattice = lattice;

end

            




               
                
 


                
            
                

                
