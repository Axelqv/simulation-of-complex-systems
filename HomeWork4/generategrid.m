clear all
close all
clc

zeros(10);

vecx = [];
vecy = [];
for i= 1:10
    for j=1:10
        vecx(end+1) = i * rand;
        vecy(end+1) = j * rand;

    end
end

tri = delaunayTriangulation(vecx',vecy');
% triplot(dt)
% E = edges(dt);

% Mmatrix = zeros(length(E));
% for i = 1:length(E)
%     Mmatrix(E(i,1), E(i,2)) = 1;
% end
% Mmatrix = Mmatrix + Mmatrix';


AdjMat = false(N);
for kk=1:size(tri,1)
    AdjMat(tri(kk,1), tri(kk,2));
    AdjMat(tri(kk,2), tri(kk,3));
    AdjMat(tri(kk,3), tri(kk,1));
end

AdjMat = AdjMat | AdjMat';


