function newPheromoneMatrix = UpdatePheromones(pheromoneMatrix, j, path, pathDistance)

    pheromoneMatrix(path(j), path(j+1)) = pheromoneMatrix(path(j), path(j+1)) + 1/pathDistance;
    pheromoneMatrix(path(j+1), path(j)) = pheromoneMatrix(path(j+1), path(j)) + 1/pathDistance;
    newPheromoneMatrix = pheromoneMatrix;
end

