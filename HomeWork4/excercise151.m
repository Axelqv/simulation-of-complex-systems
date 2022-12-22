clear all
close all
clc

N = 10;

% a)
Mmatrix = Matrix(N);
figure(1)
pcolor(Mmatrix)
title('connection matrix')


% b)
randomVertices = GenRandomVertices(N);
distances = Distances(Mmatrix, randomVertices);
figure(2)
pcolor(distances)
c = gray;
colormap(c)
grid on
colorbar
title('distances where white means infinity distance (no direct connections)')

% c)
weightMatrix = WeightMatrix(distances);
figure(3)
pcolor(weightMatrix)
title('Weight matrix')
colorbar
% d)
pheromoneMatrix = PheromoneMatrix(Mmatrix); 
figure(4)
pcolor(pheromoneMatrix)
title('Pheromone matrix')
% e)
path = GenPath(2, Mmatrix);

% f)
pathLength = GetPathLengt(path, distances);

% g)
sPath = SimplifyPath(path, distances);

% delaunay plot
%
% figure(2)
% plot(x,y,'.','markersize',12)
% grid on
% hold on
% DT = delaunay(x,y);
% triplot(DT,x,y)

figure(5)
x = randomVertices(:,1);
y = randomVertices(:,2);
tri = delaunayTriangulation(x,y);
triplot(tri)










