function weightMatrix = WeightMatrix(distanceMatrix)
    
    % Find index of inf distances 
    indexOfinf = find(distanceMatrix == inf);

    % Make all inf to one
    distanceMatrix(indexOfinf) = 1;

    % Make all the non inf distances to weights
    tmpMatrix = 1./distanceMatrix;

    % Find index of all ones in tmpWeigth matrix and set these weigths to
    % zero
    indexOfOnes = find(tmpMatrix == 1);
    tmpMatrix(indexOfOnes) = 0;
    weightMatrix = tmpMatrix;

end


