clear all
close all
clc

%%% 15.7
N = 40;
maxSteps = 80;
nAnts = 20;
alpha = 0.8;
beta = 0.5;
rho = 0.5;
iterations = 150;


zeros(N);

vecx = [];
vecy = [];
for i= 1:N
    for j=1:N
        vecx(end+1) = i;
        vecy(end+1) = j;

    end
end


randomVertices = cat(1,vecx,vecy)';
tri = delaunayTriangulation(vecx',vecy');
triplot(tri)

Edges = edges(tri);

Mmatrix = zeros(length(Edges));
for i = 1:length(Edges)
    Mmatrix(Edges(i,1), Edges(i,2)) = 1;
end
Mmatrix = Mmatrix + Mmatrix';



% AdjMat = false(N^2);
% for kk=1:size(tri,1)
%     AdjMat(tri(kk,1), tri(kk,2));
%     AdjMat(tri(kk,2), tri(kk,3));
%     AdjMat(tri(kk,3), tri(kk,1));
% end
% 
% AdjMat = AdjMat | AdjMat';
% Mmatrix = AdjMat;




% Calculating the distance
distanceMatrix = Distances(Mmatrix, randomVertices);

% Calculating the weightmatrix
weightMatrix = WeightMatrix(distanceMatrix);

% calculating the pheromone matrix
pheromoneMatrix = PheromoneMatrix(Mmatrix); 

%%%%%
% to avoid that starting point is to close to end point
distanceCondition = 0;
while distanceCondition < 40
    s0 = randi(N);
    t0 = randi(N);
    distanceCondition = pdist2(randomVertices(s0,:), randomVertices(t0,:));
end

%%% running the algorithm
pheromoneMatrices = {};
shortestPaths = {};
shortestPathDistances = [];
for iteration = 1:iterations
    % for all ants append its path to a cell array
    pheromoneMatrix = pheromoneMatrix .* (1-rho);
    paths = {};
    for i = 1:nAnts
        paths{i,1} = [];
        paths{i,1} = [paths{i,1},s0];
        for step = 1:maxSteps
            nextNode = BranchDecision(alpha, beta, paths{i,1}(end), weightMatrix, Mmatrix, pheromoneMatrix);
            paths{i,1} = [paths{i,1},nextNode];
            if nextNode == t0   % break when reach target
                break     
            end
        end
    end
    
    %%% Check which ants that arrive to the destination
    shortestPathDistance = 300;
    nReachedDestination = 0;
    arrivals = {};    % append all the ants that reach the destination
    arrivalsSimplified = {};    % append the simplified paths that reached 
                                % The destination
    j = 1;  % Just a index to append correct
    for i = 1:nAnts
        iPath = paths{i,1};
        if ~isempty(find(iPath==t0))
            nReachedDestination = nReachedDestination+1;
            arrivals{j,1} = iPath;
            iPathSimplified = SimplifyPath(iPath,distanceMatrix);
            arrivalsSimplified{j,1} = iPathSimplified;
            j = j+1;
    
            iPathDistance = GetPathLengt(iPathSimplified,distanceMatrix);
            if iPathDistance < shortestPathDistance
                shortestPathDistance = iPathDistance;
                shortestPath = iPathSimplified;
            end
            % Update the pheromones
            for j = 1:length(iPathSimplified)-1
                pheromoneMatrix = UpdatePheromones(pheromoneMatrix, j, iPathSimplified, iPathDistance);
            end
    
        end
    end
    shortestPaths{iteration} = shortestPath;
    pheromoneMatrices{iteration} = pheromoneMatrix;
    shortestPathDistances(end+1) = shortestPathDistance;
end


% find the first shorthes path
index = find(shortestPathDistances==min(shortestPathDistances));
firstShortestPathIndex = index(1)
firstShortestPath = shortestPaths{firstShortestPathIndex};

% Plot the shortest paths length as fun of nr of rounds
figure(1)
plot(1:iterations,shortestPathDistances)
ylabel('L(n)')
xlabel('n')
msg1 = sprintf('Length of shortest path for every round, N=%d. First found round=%d',N,firstShortestPathIndex);
title(msg1)


% Plot the shortest path found
figure(2)
triplot(tri)
hold on
plotx = randomVertices(firstShortestPath,1);
ploty = randomVertices(firstShortestPath,2);
plot(plotx,ploty,'-o','Color','r','LineWidth',3)
scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
legend('edges','path','startpoint','endpoint','Location','best')
msg2 = sprintf('Shortest path, N=%d. First found round=%d',N, firstShortestPathIndex);
title(msg2)



% Plot the phermoneMatrix at round 1
pheromoneMatrix = pheromoneMatrices{1};
figure(3)
for i = 1:N
    for j = 1:N
        if Mmatrix(i,j) == 1
        plot([randomVertices(i,1),randomVertices(j,1)], ...
            [randomVertices(i,2),randomVertices(j,2)],'-o','Color','r','LineWidth',pheromoneMatrix(i,j)*10)
        hold on
        end
    end
end
scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
msg3 = sprintf('Pheromone matrix round %d',1);
title(msg3)

% Plot the phermoneMatrix at first round when the shortest path is found
pheromoneMatrix = pheromoneMatrices{firstShortestPathIndex};
figure(4)
for i = 1:N
    for j = 1:N
        if Mmatrix(i,j) == 1
        plot([randomVertices(i,1),randomVertices(j,1)], ...
            [randomVertices(i,2),randomVertices(j,2)],'-o','Color','r','LineWidth',pheromoneMatrix(i,j)*10)
        hold on
        end
    end
end
scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
msg4 = sprintf('Pheromone matrix round %d',firstShortestPathIndex);
title(msg4)


% Plot the phermoneMatrix at round 50
pheromoneMatrix = pheromoneMatrices{50};
figure(5)
for i = 1:N
    for j = 1:N
        if Mmatrix(i,j) == 1
        plot([randomVertices(i,1),randomVertices(j,1)], ...
            [randomVertices(i,2),randomVertices(j,2)],'-o','Color','r','LineWidth',pheromoneMatrix(i,j)*10)
        hold on
        end
    end
end
scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
msg5 = sprintf('Pheromone matrix round %d',50);
title(msg5)

pheromoneMatrix = pheromoneMatrices{150};
figure(6)
for i = 1:N
    for j = 1:N
        if Mmatrix(i,j) == 1
        plot([randomVertices(i,1),randomVertices(j,1)], ...
            [randomVertices(i,2),randomVertices(j,2)],'-o','Color','r','LineWidth',pheromoneMatrix(i,j)*10)
        hold on
        end
    end
end
scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
msg6 = sprintf('Pheromone matrix round %d',150);
title(msg6)


%% subsection to plot different pheromone matrixes from all the stored ones from the simulation
pheromoneMatrix = pheromoneMatrices{80};
figure(7)
for i = 1:N
    for j = 1:N
        if Mmatrix(i,j) == 1
        plot([randomVertices(i,1),randomVertices(j,1)], ...
            [randomVertices(i,2),randomVertices(j,2)],'-o','Color','r','LineWidth',pheromoneMatrix(i,j)*10)
        hold on
        end
    end
end
scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
msg7 = sprintf('Pheromone matrix round %d',80);
title(msg7)

pheromoneMatrix = pheromoneMatrices{10};
figure(8)
for i = 1:N
    for j = 1:N
        if Mmatrix(i,j) == 1
        plot([randomVertices(i,1),randomVertices(j,1)], ...
            [randomVertices(i,2),randomVertices(j,2)],'-o','Color','r','LineWidth',pheromoneMatrix(i,j)*10)
        hold on
        end
    end
end
scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
msg8 = sprintf('Pheromone matrix round %d',10);
title(msg8)


pheromoneMatrix = pheromoneMatrices{5};
figure(9)
for i = 1:N
    for j = 1:N
        if Mmatrix(i,j) == 1
        plot([randomVertices(i,1),randomVertices(j,1)], ...
            [randomVertices(i,2),randomVertices(j,2)],'-o','Color','r','LineWidth',pheromoneMatrix(i,j)*10)
        hold on
        end
    end
end
scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
msg9 = sprintf('Pheromone matrix round %d',5);
title(msg9)




