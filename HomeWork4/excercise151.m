clear all
close all
clc

%% 15.1
N = 10;

% a)
Mmatrix = Matrix(N);
figure(1)
pcolor(Mmatrix)


% b)
randomVertices = GenRandomVertices(N);
distances = Distances(Mmatrix, randomVertices);
figure(1)
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

% d)
pheromoneMatrix = PheromoneMatrix(Mmatrix); 
figure(4)
pcolor(pheromoneMatrix)

% e)
path = GenPath(2, Mmatrix);

% f)
pathLength = GetPathLengt(path, distances);

% g)
sPath = SimplifyPath(path, distances);

% delaunay plot
x = randomVertices(:,1);
y = randomVertices(:,2);
figure(2)
plot(x,y,'.','markersize',12)
grid on
hold on
DT = delaunay(x,y);
triplot(DT,x,y)

figure(3)
tri = delaunayTriangulation(x,y);
triplot(tri,x,y)










