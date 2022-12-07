function newLattice = Recover(lattice, gamma)
    latticeLength = length(lattice);
    for i = 1:latticeLength
        for j = 1:latticeLength
            indexInfected = find(lattice{i, j} == 2);
            if isempty(indexInfected)
                continue
            end
            for index = indexInfected
                randomNr = rand();
                if randomNr < gamma
                    lattice{i, j}(index) = 3;   % infected gets recovered
                end
            end
        end
    end

    newLattice = lattice;

end
% function lattice = Recover(lattice, gamma)
%     L = length(lattice);
%      for i = 1:L
%          for j = 1:L
%              r = rand();
%              if (gamma > r && ~isempty(find(lattice{i,j} == 2, 1)))
%                  infectedAgentIndex = find(lattice{i,j} == 2);
%                  for n = infectedAgentIndex
%                      lattice{i,j}(n) = 3;
%                  end
%              end
%          end
%      end
% end













               
   
