function [temp,Y] = sample_kmeans(X,k,epsilon)
%   author:JYT
%   Input -
%   X - input row sample
%   k - num of cluster center
%   epsilon - error of pause iteration

%   Output - 
%   temp - a matrix combined sample-X and classfication index result
%   Y - the coordinate of center after iteration

% init
curr_dist = inf;
delta = inf;
[m,~] = size(X);
Y = [];
%init firstly centers
for i=1:m:m/k
    Y = [Y X(i,:)];
end

while delta > epsilon
   % cal distance bewteen sample-X and center with matrix and dist()
   % function
   dist_mat = dist(X-Y);
   % find minium distance from dist_mat each row, return dis and index
   [dis,index] = min(dist_mat,[],2);
   % combin X and index result for new matrix
   temp = [X index];
   % clean center selection
   Y = [];
   % cal mean of every index as new cluster center
   for i=1:k
       Y = [Y mean(temp(temp(:,2)==i),1)];
   end
   % cal delta to determin whether pause loop/iteration
   delta = curr_dist - sum(dis);
   % save current distance to curr_dist
   curr_dist = sum(dis);
end    
end

