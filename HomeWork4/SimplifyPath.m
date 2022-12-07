function simplifyPath = SimplifyPath(path, distanceMatrix)

    simplifyPath = [];
    i = 1;
    while i < length(path)+1
        if ismember(path(i), path(i+1:end))
            k = find(path(i+1:end) == path(i));
            i = k(1) + i;   % Find the next index of repeated vertices
        else
            simplifyPath(end+1) = path(i);
            i = i+1;
        end
    end

end



    