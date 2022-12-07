clear all
close all
clc
figure(1)
randomVertices = GenRandomVertices(20);
tri = delaunayTriangulation(randomVertices);
triplot(tri)


figure(2)
xVertices = randomVertices(:,1);
yVertices = randomVertices(:,2);
tri1 = delaunayTriangulation(xVertices, yVertices);
triplot(tri1)
