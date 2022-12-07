clear all
close all
clc
L = 100;
N = 1000;
nrOfInfected = 10;
d = 0.8;
beta = 0.6;
gamma = 0.01;
mu = 0.00007;
time = 1000;
betas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9];
initializeAgents = InitializeAgentsWithPos(L, N, nrOfInfected);


% dataArray = zeros(4*length(betas),time);
% for i = 1:length(betas)
%     beta = betas(i);
%     agents = initializeAgents;
%     for t = 1:time
%         dataArray(1+4*(i-1):4+4*(i-1),t) =  DataMortality(agents);
%         agents = Move(agents, d, L);
%         agents = Recover(agents,gamma);
%         agents = Infected(agents, beta);
%         agents = Death(agents, mu);
%     end
% end
% 
% 
% 
% for i = 1:length(betas)
%     beta = betas(i);
%     subplot(3,3,i)
%     plot(dataArray(1+4*(i-1),:),'b')
%     hold on
%     plot(dataArray(2+4*(i-1),:),'r')
%     plot(dataArray(3+4*(i-1),:),'g')
%     plot(dataArray(4+4*(i-1),:),'k')
%     title(sprintf('beta=%0.1f, mu=%0.4f',beta,mu))
% end


%% 11.3b)
betas = [0.3, 0.6];
gammas = [0.01, 0.015];
trials = 3;
mus = [0:0.001:0.02];
DArray1 = zeros(trials, length(mus));
DArray2 = zeros(trials, length(mus));
DArray3 = zeros(trials, length(mus));
DArray4 = zeros(trials, length(mus));
DArray5 = zeros(trials, length(mus));
DArray6 = zeros(trials, length(mus));
DArray7 = zeros(trials, length(mus));
DArray8 = zeros(trials, length(mus));
for m = 1:length(mus)
    mu = mus(m);
    for j = 1:length(gammas)
        gamma = gammas(j);
        for i = 1:length(betas)
            beta = betas(i);
            for trial =  1:trials
                agents = initializeAgents;
                for t = 1:time
                    agents = Move(agents, d, L);
                    agents = Recover(agents,gamma);
                    agents = Infected(agents, beta);
                    agents = Death(agents,mu);
                    data = DataMortality(agents);
                end
                if i==1 && j==1
                    DArray1(trial,m) = data(4);  % beta1 & gamma1
                elseif i==1 && j==2
                    DArray2(trial,m) = data(4);   %beta1 & gamma2
                elseif i==2 && j==1     
                    DArray3(trial,m) = data(4);    %beta2 & gamma1
                elseif i==2 && j==2     
                    DArray4(trial,m) = data(4);    %beta2 & gamma2
                end
            end
        end
    end
end


D1Averages = sum(DArray1,1) / trials;
D2Averages = sum(DArray2,1)/ trials;
D3Averages = sum(DArray3,1)/ trials;
D4Averages = sum(DArray4,1)/ trials;
scatter(mus, D1Averages,'b')
hold on
scatter(mus, D2Averages,'r')
scatter(mus, D3Averages,'k')
scatter(mus, D4Averages,'g')
prints1 = sprintf('gamma=%0.3f, beta=%0.3f',gammas(1),betas(1));
prints2 = sprintf('gamma=%0.3f, beta=%0.3f',gammas(2),betas(1));
prints3 = sprintf('gamma=%0.3f, beta=%0.3f',gammas(1),betas(2));
prints4 = sprintf('gamma=%0.3f, beta=%0.3f',gammas(2),betas(2));
legend(prints1,prints2,prints3,prints4,'Location','best');
xlabel('mu')
ylabel('Dinf')







        
            
%                 if j == 1 && i==1
%                     DArray1(trial,i) = data(4);
%                 elseif j==1 && i==2
%                     DArray3(trial,i) = data(4);
%                 elseif j==1 && i==3
%                     DArray4(trial,i) = data(4)
%     
%                 elseif j == 2
%                     DArray2(trial,i) = data(4);
%                 end
%             end
%         end
%     end
% 
% R1Averages = sum(DArray1,1) / trials;
% R2Averages = sum(DArray2,1)/ trials;
% scatter(betas, R1Averages,'filled','b')
% hold on
% scatter(betas, R2Averages,'filled','g')
% legend(sprintf('gamma=%0.3f',gammas(1)), sprintf('gamma=%0.3f', gammas(2)),'Location','southeast')






