function node = randomChoice(Probabilities,nodes)
    x = cumsum([0 Probabilities(:).'/sum(Probabilities(:))]);
    x(end) = 1e3*eps + x(end);
    [a a] = histc(rand,x);
    node = nodes(a);

end
