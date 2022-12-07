clear all
close all
clc

%%% 15.7
N = 40;
maxSteps = 80;
nAnts = 20;
alpha = 0.8;
beta = 1.0;
rho = 0.5;
iterations = 80;
% 
randomVertices = GenRandomVertices(N);
xVertices = randomVertices(:,1);
yVertices = randomVertices(:,2);
tri = delaunayTriangulation(xVertices, yVertices);
% triplot(tri)

Edges = edges(tri);

Mmatrix = zeros(N);
for i = 1:length(Edges)
    Mmatrix(Edges(i,1), Edges(i,2)) = 1;
end
Mmatrix = Mmatrix + Mmatrix';


% Calculating the distance
distanceMatrix = Distances(Mmatrix, randomVertices);
% figure(1)
% pcolor(distances)
% c = gray;
% colormap(c)
% grid on
% colorbar
% title('distances where white means infinity distance (no direct connections)')


% Calculating the weightmatrix
weightMatrix = WeightMatrix(distanceMatrix);
% figure(3)
% pcolor(weightMatrix)

% calculating the pheromone matrix
pheromoneMatrix = PheromoneMatrix(Mmatrix); 
% figure(4)
% pcolor(pheromoneMatrix)

% Generate the path
path = GenPath(2, Mmatrix);

% Calculate the length of the path 
pathLength = GetPathLengt(path, distanceMatrix);

% simplify the path
sPath = SimplifyPath(path, distanceMatrix);

%%%%%
% to avoid that starting point is to close to end point
distanceCondition = 0;
while distanceCondition < 30
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
    shortestPathDistance = 100;
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


%%% Plot all ants that reached the destination
% for k = 1:length(arrivals)
%     arrivalPath = arrivals{k};
%     figure(k)
%     triplot(tri)
%     hold on
%     plotx = randomVertices(arrivalPath,1);
%     ploty = randomVertices(arrivalPath,2);
%     plot(plotx,ploty,'-o','LineWidth',3)
%     scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
%     scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
%     legend('edges','path','startpoint','endpoint','Location','best')
%     title('Not simplified path')

%     %%% Saving the paths figures in a certain folder
%     folder = 'C:\Users\axelq\OneDrive\Skrivbord\MpCas\Simulation of complex systems\simulation-of-complex-systems\HomeWork4\15.7\15.7b)\NotSimplified';
%     baseFileName = sprintf('Figure %d.png', k);
%     fullFileName = fullfile(folder, baseFileName);
%     saveas(figure(k),fullFileName)
% end

%%% Plot the above paths when they are simplified
% j = 1;
% for k = length(arrivals)+1:length(arrivalsSimplified)+length(arrivals)
%     arrivalPathSimplified = arrivalsSimplified{j};
%     figure(k)
%     triplot(tri)
%     hold on
%     plotx = randomVertices(arrivalPathSimplified,1);
%     ploty = randomVertices(arrivalPathSimplified,2);
%     plot(plotx,ploty,'-o','LineWidth',3)
%     scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
%     scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
%     legend('edges','path','startpoint','endpoint','Location','best')
%     title('Simplified path')
% 
% %     %%% Saving the Simplified paths figures in a certain folder
% %     folder = 'C:\Users\axelq\OneDrive\Skrivbord\MpCas\Simulation of complex systems\simulation-of-complex-systems\HomeWork4\15.7\15.7b)\simplified';
% %     baseFileName = sprintf('SimplifiedFigure %d.png', j);
% %     fullFileName = fullfile(folder, baseFileName);
% %     saveas(figure(k),fullFileName)
% %     j = j+1;
% end





%%
clc
figure(1)
plot(1:iterations,shortestPathDistances)
ylabel('L(n)')
xlabel('n')
title('Length of shortest path for every round')
index = find(shortestPathDistances==min(shortestPathDistances));
firstShortestPathIndex = index(1);
firstShortestPath = shortestPaths{firstShortestPathIndex};

figure(2)
triplot(tri)
hold on
plotx = randomVertices(firstShortestPath,1);
ploty = randomVertices(firstShortestPath,2);
plot(plotx,ploty,'-o','Color','r','LineWidth',3)
scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
legend('edges','path','startpoint','endpoint','Location','best')
title('Shortest path')




%%%%% This code snippet do not work in matlab but do so in python
% for i = 1:N
%     for j = 1:N
%         plot([randomVertices(i,1),randomVertices(j,1)], ...
%             [randomVertices(i,2),randomVertices(j,2)],'-o','Color','k','LineWidth',pheromoneMatrix(i,j)*2)
%     end
% end



iPheromoneMatrix = 1;   %iterator
for h = 1:length(pheromoneMatrices)
    if rem(h,4) == 1
        figure(h)
        triplot(tri)
        hold on
        pher = pheromoneMatrices{iPheromoneMatrix};
        for i = 1:N
            for j = 1:N
                if pher(i, j) > 0.3
                    plot([randomVertices(i,1),randomVertices(j,1)],[randomVertices(i,2),randomVertices(j,2)],'-o','Color','k','LineWidth',3)
                    msg = sprintf('Pheromone matrix iteration %d',iPheromoneMatrix);
                    title(msg)
                end
            end
        end
    end
    iPheromoneMatrix = iPheromoneMatrix + 1;
end






