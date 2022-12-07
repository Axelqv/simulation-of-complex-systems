function pathLength = GetPathLengt(path, distanceMatrix)

    sum = 0;
    for i = 1:length(path)-1
        distance = distanceMatrix(path(i), path(i+1));
        sum = sum + distance;
    end
pathLength = sum;
end

    