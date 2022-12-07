function agents = Recover(agents, gamma)

    indexOfInfected = find(agents(:, 3)==2);
    randomNumbers = rand(length(indexOfInfected),1);

    indexGettingRecovered = indexOfInfected(find(randomNumbers<gamma));
    if~isempty(indexGettingRecovered)
        agents(indexGettingRecovered,3) = 3;
    end

end
