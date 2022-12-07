function randomVertices = GenRandomVertices(N)

    x = randperm(N,N);
    y = randperm(N,N);
    randomVertices = cat(2,x',y');

end

