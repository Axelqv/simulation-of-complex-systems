
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



betas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9];  % infected probability
gammas = [0.01, 0.02]; % recover probability
d = 0.8;
trials = 4;

RList1 = zeros(trials, length(betas));
RList2 = zeros(trials, length(betas));
for trial = 1:trials
    for g = 1:length(gammas)
        gamma = gammas(g);
        for l = 1:length(betas)
            beta = betas(l);
            time = [];
            t = 0;
            lattice = initLattice;
        %     while(FindInfected(lattice))
            for h = 1:1000
                data = Data(lattice);
        %         clf
                lattice = Move(lattice, d);
                lattice = infection(lattice, beta);
                lattice = Recover(lattice, gamma);
            %     PlotModel(lattice)
            %     drawnow
                t = t + 1;
                time(end+1) = t;
                
        %         if (nSuceptibleList(t) + nInfectedList(t) + nRecoveredList(t)) ~= N
        %             disp('something wrong')
        %             break
        %         end
            end
            data = Data(lattice);
            if g == 1
                RList1(trial, l) = data(3);
            else
                RList2(trial, l) = data(3);
            end
        end   
    end
end

averageR1 = sum(RList1,1)/trials;
averageR2 = sum(RList2,1)/trials;

scatter(betas, averageR1,'filled','b')
hold on
scatter(betas, averageR2,'filled','g')
legend('gamma=0.1', 'gamma=0.2')



%% store
save('R1average',"averageR1")
save('Raverage2','averageR2')
save('betas',"betas")
save('gammas',"gammas")
betaGamma1 = betas/gammas(1);
betaGamma2 = betas/gammas(2);

figure(1)
scatter(betaGamma1, averageR1)
hold on
scatter(betaGamma2, averageR2)
xlabel('beta/gamma')
ylabel('R average')
legend('gamma = 0.1', 'gamma = 0.2')
hold off

figure(2)
scatter(betas, averageR1,'filled','b')
hold on
scatter(betas, averageR2,'filled','g')
legend('gamma=0.1', 'gamma=0.2')
xlabel('beta')
ylabel('R average')
hold off

figure(3)
imagesc(betas, betaGamma1, averageR1)
colorbar















%% check to see that we initialize N agents in the grid
nrOfA = 0;
for j= 1:length(lattice)
    for i= 1:length(lattice)
        a = lattice{j, i};
        nrElements = length(a);
        nrOfA = nrOfA + nrElements;
    end
end






