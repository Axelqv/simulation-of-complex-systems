function findInfected = FindInfected(lattice)
    
    findInfected = false;
    latticeLength = length(lattice);
     for i = 1:latticeLength
        for j = 1:latticeLength
            indexInfected = find(lattice{i, j} == 2);
            if ~isempty(indexInfected)
                findInfected = true;
                return
            end
        end
     end

end





            
                