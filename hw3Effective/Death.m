function agents = Death(agents, mu)

    indexOfInfected = find(agents(:, 3) == 2);
    randomNr = rand(length(indexOfInfected),1);
    indexOfGettingDead = indexOfInfected(find(randomNr<mu));
    if ~isempty(indexOfGettingDead)
        agents(indexOfGettingDead,3) = 0;
    end
end
