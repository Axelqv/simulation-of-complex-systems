clear all
close all
clc

%% 15.7
N = 40;
maxSteps = 80;
nAnts = 20;
alpha = 0.8;
beta = 1.0;
rho = 0.5;

randomVertices = GenRandomVertices(N);
xVertices = randomVertices(:,1);
yVertices = randomVertices(:,2);
tri = delaunayTriangulation(xVertices, yVertices);
triplot(tri)

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
while distanceCondition < 10
    s0 = randi(N);
    t0 = randi(N);
    distanceCondition = pdist2(randomVertices(s0,:), randomVertices(t0,:));
end


% for all ants append its path to a cell array
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
    
% Check which ants that arrive to the destionation
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
    end
end


% 
%%% Plot all ants that reached the destination
for k = 1:length(arrivals)
    arrivalPath = arrivals{k};
    figure(k)
    triplot(tri)
    hold on
    plotx = randomVertices(arrivalPath,1);
    ploty = randomVertices(arrivalPath,2);
    plot(plotx,ploty,'-o','LineWidth',3)
    scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
    scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
    legend('edges','path','startpoint','endpoint','Location','best')
    title('Not simplified path')

    %%% Saving the paths figures in a certain folder
    folder = 'C:\Users\axelq\OneDrive\Skrivbord\MpCas\Simulation of complex systems\simulation-of-complex-systems\HomeWork4\15.7\15.7b)\NotSimplified';
    baseFileName = sprintf('Figure %d.png', k);
    fullFileName = fullfile(folder, baseFileName);
    saveas(figure(k),fullFileName)
end
% 
%%% Plot the above paths when they are simplified
j = 1;
for k = length(arrivals)+1:length(arrivalsSimplified)+length(arrivals)
    arrivalPathSimplified = arrivalsSimplified{j};
    figure(k)
    triplot(tri)
    hold on
    plotx = randomVertices(arrivalPathSimplified,1);
    ploty = randomVertices(arrivalPathSimplified,2);
    plot(plotx,ploty,'-o','LineWidth',3)
    scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
    scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
    legend('edges','path','startpoint','endpoint','Location','best')
    title('Simplified path')

    %%% Saving the Simplified paths figures in a certain folder
    folder = 'C:\Users\axelq\OneDrive\Skrivbord\MpCas\Simulation of complex systems\simulation-of-complex-systems\HomeWork4\15.7\15.7b)\simplified';
    baseFileName = sprintf('SimplifiedFigure %d.png', j);
    fullFileName = fullfile(folder, baseFileName);
    saveas(figure(k),fullFileName)
    j = j+1;
end
% 
% 
figure(k+1)
triplot(tri)
hold on
plotx = randomVertices(shortestPath,1);
ploty = randomVertices(shortestPath,2);
plot(plotx,ploty,'-o','LineWidth',3)
scatter(randomVertices(s0,1),randomVertices(s0,2),'g','square','filled')
scatter(randomVertices(t0,1),randomVertices(t0,2),'y','square','filled')
legend('edges','shortest path','startpoint','endpoint','Location','best')
title('Simplified shortest path')

folder = 'C:\Users\axelq\OneDrive\Skrivbord\MpCas\Simulation of complex systems\simulation-of-complex-systems\HomeWork4\15.7\15.7b)\shortestPath';
baseFileName = 'Shortest Path.png';
fullFileName = fullfile(folder, baseFileName);
saveas(figure(k+1),fullFileName)






        
















