function agents = InitializeAgentsWithPos(L, N, nrOfInfected)
    agents = zeros(N,3);
    for n = 1:N
        coord = randi(L,1,2);
        x = coord(1);
        y = coord(2);
        agents(n,1) = x;
        agents(n,2) = y;
        agents(n,3) = 1;
        if (n > (N - nrOfInfected))
            agents(n,3) = 2;
        end
    end
end

