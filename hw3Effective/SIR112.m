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
gammas = [0.01, 0.02];
initializeAgents = InitializeAgentsWithPos(L, N, nrOfInfected);

trials = 4;
RArray1 = zeros(trials, length(betas));
RArray2 = zeros(trials, length(betas));
for j = 1:length(gammas)
    gamma = gammas(j);
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
            if j == 1
                RArray1(trial,i) = data(3);
            elseif j == 2
                RArray2(trial,i) = data(3);
            end
        end
    end
end

R1Averages = sum(RArray1,1) / trials;
R2Averages = sum(RArray2,1)/ trials;
scatter(betas, R1Averages,'filled','b')
hold on
scatter(betas, R2Averages,'filled','g')
legend(sprintf('gamma=%0.3f',gammas(1)), sprintf('gamma=%0.3f', gammas(2)),'Location','southeast')








