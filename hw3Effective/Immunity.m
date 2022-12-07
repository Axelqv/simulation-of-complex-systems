function agents = Immunity(agents, alpha)

    indexRecovered = find(agents(:,3)==3);
    randomNumbers = rand(length(indexRecovered),1);

    indexGettingSuceptible = indexRecovered(find(randomNumbers<alpha));
    if ~isempty(indexGettingSuceptible)
        agents(indexGettingSuceptible,3) = 1;
    end

end
