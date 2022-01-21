function [result] = sample_lingress(X,Y,i)
    beta = (inv(X'*X))*X'*Y(:,i);
    result = X*beta;
end