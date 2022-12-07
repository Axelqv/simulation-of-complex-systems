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
betas = [0.01:0.04:1];
gammas = [0.0075:0.000205:0.0125];
initializeAgents = InitializeAgentsWithPos(L, N, nrOfInfected);

trials = 4;
% RArray1 = zeros(trials, length(betas));
% RArray2 = zeros(trials, length(betas));
RArray = zeros(length(gammas), length(betas));
for j = 1:length(gammas)
    gamma = gammas(j);
    R = zeros(trials, length(betas));
    for trial =  1:trials
        for i = 1:length(betas)
            beta = betas(i);
            agents = initializeAgents;
            for t = 1:time
                agents = Move(agents, d, L);
                agents = Recover(agents,gamma);
                agents = Infected(agents, beta);
                data = Data(agents);
            end
            R(trial, i) = data(3);
        end
    end
    RAverages = sum(R,1) / trials;
    RArray(j, :) = RAverages;
end

% R1Averages = sum(RArray1,1) / trials;
% R2Averages = sum(RArray2,1)/ trials;
% scatter(betas, R1Averages,'filled','b')
% hold on
% scatter(betas, R2Averages,'filled','g')
% legend(sprintf('gamma=%0.3f',gammas(1)), sprintf('gamma=%0.3f', gammas(2)),'Location','southeast')


%% Saving RArray and plot phase diagram

save('RAverages','RArray')
gammaBetas = betas ./ gammas;
[x, y] = meshgrid(betas,gammaBetas);
surf(x, y, RArray')
xlabel('beta')
ylabel('beta/gamma')
title('Rinf')
view(2)
colorbar








