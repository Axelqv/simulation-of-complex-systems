function agents = Move(agents, d, L)
    N = length(agents);    %number of agents
    randomNumbers = rand(N,1);
    indexForMove = find(randomNumbers < d);

    nMovingAgents = length(indexForMove);   %nr of agents that will move

    randomMoveIndex = randi(4, nMovingAgents, 1);
    Movements = [0, 1; 0, -1; 1, 0; -1, 0];

    move = Movements(randomMoveIndex, :);
    agents(indexForMove, 1:2) = agents(indexForMove, 1:2) + move;

    % coordinates that gets outside grid gets to other side (PBC)
    tooSmallCoordinates = find(agents(:, 1:2) < 1);
    tooBigCoordinates = find(agents(:, 1:2) > L); 
    if ~isempty(tooBigCoordinates)
        agents(tooBigCoordinates) = agents(tooBigCoordinates) - L;
    end
    if ~isempty(tooSmallCoordinates)
        agents(tooSmallCoordinates) = agents(tooSmallCoordinates) + L;

    end
end
%         



