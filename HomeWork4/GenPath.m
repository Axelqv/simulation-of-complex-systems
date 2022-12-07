function path = GenPath(i, Mmatrix)

    k = size(Mmatrix,2);
    tmpMatrix = Mmatrix;
    node = i;
    path = [node];
    
%     for l = 1:k-1
%         path(end+1) = node;
%         tmpMatrix(:,node) = 0;
%         PossibleConnectedNodes = tmpMatrix(node,:);
%         connectedNodes = find(PossibleConnectedNodes==1);
% 
%         if length(connectedNodes) == 1
%             node = connectedNodes;
%         else
%             node = randsample(connectedNodes,1);
%         end
% 
%        
%     end
    for l = 1:k-1
        PossibleConnectedNodes = Mmatrix(node,:);
        connectedNodes = find(PossibleConnectedNodes==1);
        if length(connectedNodes) == 1
            node = connectedNodes;
        else
            node = randsample(connectedNodes,1);
        end
        path(end+1) = node;
       
    end

end


        
        


        

    

    