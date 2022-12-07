clear all
close all
clc
L = 100;
N = 1000;
nrOfInfected = 10;
d = 0.8;
beta = 0.6;
gamma = 0.01;
time = 1000;
betas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9];
initializeAgents = InitializeAgentsWithPos(L, N, nrOfInfected);


dataArray = zeros(3*length(betas),time);
for i = 1:length(betas)
    beta = betas(i);
    agents = initializeAgents;
    for t = 1:time
        dataArray(1+3*(i-1):3+3*(i-1),t) =  Data(agents);
        agents = Move(agents, d, L);
        agents = Recover(agents,gamma);
        agents = Infected(agents, beta);
    end
end


% timeVector = [1:time];
% length(timeVector)
% plot(timeVector, dataArray(1,:))
% hold on
% plot(timeVector, dataArray(2,:))
% plot(timeVector,dataArray(3,:))

for i = 1:length(betas)
    beta = betas(i);
    subplot(3,3,i)
    plot(dataArray(1+3*(i-1),:),'b')
    hold on
    plot(dataArray(2+3*(i-1),:),'r')
    plot(dataArray(3+3*(i-1),:),'g')
    title(sprintf('beta=%0.1f',beta))
end






