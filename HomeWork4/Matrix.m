function Mmatrix = Matrix(N)
% Create the M matrix by generate random connections which is all ones
tmpMatrix = randi([0 1],N,N);
tmpMatrix = tril(tmpMatrix,-1);
Mmatrix = tmpMatrix + tmpMatrix';

end
