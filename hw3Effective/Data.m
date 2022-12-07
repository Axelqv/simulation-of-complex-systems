function data = Data(agents)

   % Find index of the Three different types of agents
   indexOfSuceptible = find(agents(:,3)==1);
   indexOfInfected = find(agents(:,3)==2);
   indexOfRecovered = find(agents(:,3)==3);
   

   nrOfSuceptible = length(indexOfSuceptible);
   nrOfInfected = length(indexOfInfected);
   nrOfRecovered = length(indexOfRecovered);

   data = [nrOfSuceptible; nrOfInfected; nrOfRecovered];

