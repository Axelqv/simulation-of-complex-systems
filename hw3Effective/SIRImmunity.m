clear all
close all
clc
L = 100;
N = 1000;
nrOfInfected = 100;
d = 0.8;
beta = 0.8;
gamma = 0.01;
alpha = 0.005;
time = 60000;
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
        agents = Immunity(agents, alpha);
    end
end

% agents = initializeAgents;
% dataArray = zeros(3,time);
% for t = 1:time
%     dataArray(:,t) =  Data(agents);
%     agents = Move(agents, d, L);
%     agents = Recover(agents,gamma);
%     agents = Infected(agents, beta);
%     agents = Immunity(agents, alpha);
% end



% timeVector = [1:time];
% length(timeVector)
% plot(timeVector, dataArray(1,:),'b')
% hold on
% plot(timeVector, dataArray(2,:),'r')
% plot(timeVector,dataArray(3,:),'g')

for i = 1:length(betas)
    beta = betas(i);
    subplot(3,3,i)
    plot(dataArray(1+3*(i-1),:),'b')
    hold on
    plot(dataArray(2+3*(i-1),:),'r')
    plot(dataArray(3+3*(i-1),:),'g')
    print1 = sprintf('beta=%0.1f',beta);
    print3 = sprintf('alpha=%0.4f, gamma=%0.3f',alpha,gamma);
    title(print1)
    sgtitle(print3)
end






