function nextNode = BranchDecision(alpha, beta, i, weightMatrix, Mmatrix, pheromoneMatrix)

    possibleNextNode = find(Mmatrix(i,:) == 1);
    nextProbability = zeros(1,length(possibleNextNode));
    
    for j = 1:length(nextProbability)
        Nominator = pheromoneMatrix(i, possibleNextNode(j))^alpha * weightMatrix(i, possibleNextNode(j))^beta;
        nextProbability(j) = Nominator;
    end
    nextProbability = nextProbability./sum(nextProbability);
    nextNode = randomChoice(nextProbability, possibleNextNode);

end

        

