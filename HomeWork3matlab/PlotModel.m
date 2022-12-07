function PlotModel(lattice)

    
    positions = zeros(length(lattice), length(lattice));

    for i = 1:length(lattice)
        for j = 1:length(lattice)
            mostFrequentAgent = mode(lattice{i,j});
            if (mostFrequentAgent == 1)
                positions(i,j) = 1;
            elseif (mostFrequentAgent == 2)
                positions(i,j) = 2;
            elseif (mostFrequentAgent == 3)
                positions(i,j) = 3;
            else
                positions(i,j) = 0;
            end
        end
    end
    
    [x1,y1] = find(positions == 1);
    [x2, y2] = find(positions == 2);
    [x3, y3] = find(positions == 3);
    scatter(x1, y1, 10, "filled", MarkerFaceColor='b')  % suceptible
    hold on
    scatter(x2, y2, 10, "filled", MarkerFaceColor='r')  % infected
    scatter(x3, y3, 10, "filled", MarkerFaceColor='g')  % recovered


end