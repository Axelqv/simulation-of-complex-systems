
close all
clear all
clc
L = 100;
N = 1000;
infectedProb = 0.01;

% l = find(M==1);
% k = find(M==2);
% length(l)+length(k)
% % 
% [x1, y1] = find(M==1);
% [x2, y2] = find(M==2);
% scatter(x1, y1, 10, "filled", MarkerFaceColor='r')
% hold on
% scatter(x2, y2, 10, "filled", MarkerFaceColor='g')


% Initialize lattice
initLattice = InitLatticeWithAgents(L,N,infectedProb);
initData = Data(initLattice);
nrOfInitInfected = initData(2);



beta = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9];  % infected probability
gamma = 0.03; % recover probability
d = 0.8;
for b = beta
    time = [];
    t = 0;
    nSuceptibleList = [];
    nInfectedList = [];
    nRecoveredList = [];
    lattice = initLattice;
%     while(FindInfected(lattice))
    for h = 1:1000
        data = Data(lattice);
        nSuceptibleList(end+1) = data(1);
        nInfectedList(end+1) = data(2);
        nRecoveredList(end+1) = data(3);
%         clf
        lattice = Move(lattice, d);
        lattice = infection(lattice, b);
        lattice = Recover(lattice, gamma);
        PlotModel(lattice)
        drawnow
        t = t + 1;
        time(end+1) = t;
%         if (nSuceptibleList(t) + nInfectedList(t) + nRecoveredList(t)) ~= N
%             disp('something wrong')
%             break
%         end
    end
    if b == 0.1
        b1Suceptible = nSuceptibleList;
        b1Infected = nInfectedList;
        b1Recovered = nRecoveredList;
    elseif b== 0.2
        b2Suceptible = nSuceptibleList;
        b2Infected = nInfectedList;
        b2Recovered = nRecoveredList;
    elseif b== 0.3
        b3Suceptible = nSuceptibleList;
        b3Infected = nInfectedList;
        b3Recovered = nRecoveredList;
    elseif b== 0.4
        b4Suceptible = nSuceptibleList;
        b4Infected = nInfectedList;
        b4Recovered = nRecoveredList;
    elseif b== 0.5
        b5Suceptible = nSuceptibleList;
        b5Infected = nInfectedList;
        b5Recovered = nRecoveredList;
    elseif b== 0.6
        b6Suceptible = nSuceptibleList;
        b6Infected = nInfectedList;
        b6Recovered = nRecoveredList;
    elseif b== 0.7
        b7Suceptible = nSuceptibleList;
        b7Infected = nInfectedList;
        b7Recovered = nRecoveredList;
    elseif b== 0.8
        b8Suceptible = nSuceptibleList;
        b8Infected = nInfectedList;
        b8Recovered = nRecoveredList;
    elseif b== 0.9
        b9Suceptible = nSuceptibleList;
        b9Infected = nInfectedList;
        b9Recovered = nRecoveredList;
    end

end

subplot(3,3,1)
plot(time, b1Suceptible,'b')
hold on
plot(time, b1Recovered,'g')
plot(time, b1Infected,'r')
title('beta=0.1')

subplot(3,3,2)
plot(time, b2Suceptible,'b')
hold on
plot(time, b2Recovered,'g')
plot(time, b2Infected,'r')
title('beta=0.2')

subplot(3,3,3)
plot(time, b3Suceptible,'b')
hold on
plot(time, b3Recovered,'g')
plot(time, b3Infected,'r')
title('beta=0.3')

subplot(3,3,4)
plot(time, b4Suceptible,'b')
hold on
plot(time, b4Recovered,'g')
plot(time, b4Infected,'r')
title('beta=0.4')

subplot(3,3,5)
plot(time, b5Suceptible,'b')
hold on
plot(time, b5Recovered,'g')
plot(time, b5Infected,'r')
title('beta=0.5')

subplot(3,3,6)
plot(time, b6Suceptible,'b')
hold on
plot(time, b6Recovered,'g')
plot(time, b6Infected,'r')
title('beta=0.6')

subplot(3,3,7)
plot(time, b7Suceptible,'b')
hold on
plot(time, b7Recovered,'g')
plot(time, b7Infected,'r')
title('beta=0.7')

subplot(3,3,8)
plot(time, b8Suceptible,'b')
hold on
plot(time, b8Recovered,'g')
plot(time, b8Infected,'r')
title('beta=0.8')

subplot(3,3,9)
plot(time, b9Suceptible,'b')
hold on
plot(time, b9Recovered,'g')
plot(time, b9Infected,'r')
title('beta=0.9')


%% check to see that we initialize N agents in the grid
nrOfA = 0;
for j= 1:length(lattice)
    for i= 1:length(lattice)
        a = lattice{j, i};
        nrElements = length(a);
        nrOfA = nrOfA + nrElements;
    end
end






