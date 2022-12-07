function data = Data(lattice)
    
    nSuceptible = 0;
    nInfected = 0;
    nRecovered = 0;
    latticeLength = length(lattice);
     for i = 1:latticeLength
        for j = 1:latticeLength
            site = lattice{i, j};
            for agent = site
                if agent == 1
                    nSuceptible = nSuceptible + 1;
                elseif agent == 2
                    nInfected = nInfected + 1;
                elseif agent == 3
                    nRecovered = nRecovered + 1;
                end
            end
        end
     end

     data = [nSuceptible, nInfected, nRecovered];
     
end

