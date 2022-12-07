function agents = Infected(agents, beta)

    % Find index of suceptible and infected
    indexOfInfected = find(agents(:, 3) == 2);
    coordsOfInfected = agents(indexOfInfected, 1:2);
    
    % use index to find pos of suceptible and infected
    indexOfSuceptible = find(agents(:,3)==1);
    coordsOfSuceptible = agents(indexOfSuceptible,1:2);
    
    % find sites where there is suceptible and infected
    InfectedWithSuceptibleIndex = find(ismember(coordsOfSuceptible, coordsOfInfected, 'rows'));
    if isempty(InfectedWithSuceptibleIndex)
        return
    else
    
        % Suceptible gets infected with probability beta
        randomNumbers = rand(length(InfectedWithSuceptibleIndex),1);
        suceptibleGetInfectedIndex = InfectedWithSuceptibleIndex(find(randomNumbers<beta));
        if ~isempty(suceptibleGetInfectedIndex)
            coordsOfGettingInfected = coordsOfSuceptible(suceptibleGetInfectedIndex,:);
            gettingInfectedIndex = find(ismember(agents(:,1:2),coordsOfGettingInfected,"rows"));
            agents(gettingInfectedIndex,3) = 2;
    
        end
    end
end
    



    