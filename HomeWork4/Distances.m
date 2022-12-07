function distanceMatrix = Distances(Mmatrix, vertices)
    
    N = length(vertices);
    distanceMatrix = zeros(N,N);
    
%     % Taking out the upper triagular part of Mmatrix
%     upperOfMmatrix = triu(Mmatrix);
   

%     % Find all indexes of ones
    for i = 1:N
        for j = 1:N
            if Mmatrix(i, j) == 1
                distance = pdist2(vertices(i,:), vertices(j,:));
                distanceMatrix(i, j) = distance;
            else
                distanceMatrix(i, j) = inf;
            end
        end
    end




%     % Generate random distances for all ones
%     randomDistances = randi(50, length(indexOfOnes), 1);
%     upperOfMmatrix(indexOfOnes) = randomDistances;

    
% 
%     % Make the distance matrix by adding the inverse of upperOfMmatrix
%     distanceMatrix = upperOfMmatrix + upperOfMmatrix';
% 
%     % Find all indexes of zeros in distance matrix
%     indexOfZeros = find(distanceMatrix == 0);
% 
%     % Set all the zeros to inf distance
%     distanceMatrix(indexOfZeros) = inf;
end




    