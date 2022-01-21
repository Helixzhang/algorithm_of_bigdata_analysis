function [Y] = sample_pca(X)
% author: JYT
% X - row data

% centralization X
centralized_X = X-ones(size(X,1),1)*mean(X);

% covariance X,$\Sigma = cov(X)$
cov_X = cov(centralized_X);

% get eigenvalue(D) and eigenvector(E) of cov_X
[E, D] = eig(cov_X); 

% get index of sort eigenvalue by desc($\lamda_1 >= \lamda_2 >= \cdots
% \lamda_n$)
[~,index] = sort(diag(-D));

% sort eig matrix by index
E = E(:,index);

%return pca vector Y by E'*X
Y = E'*X;
end