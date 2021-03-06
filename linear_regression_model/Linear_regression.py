#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

#class that models linear regression
class lin_reg:
    def fit(self,x,y,lambda_=0):
        self.x = np.array(x)
        self.y = y
        self.w = np.zeros((np.shape(x)[1],1))  #weights
        self.b = [0]                           #bias
        self.lambda_ = lambda_                 #regularization factor 
     
    def normalize(self,xin):                   #to fit the data more accurately
        Mean=np.mean(xin,axis=0)
        Std=np.std(xin,axis=0)
        return (xin - Mean ) / Std,Mean,Std
    
    def cost_fn(self):                         #mean squared error
        return np.sum(np.square(self.x.dot(self.w)+self.b-self.y))/2/np.size(self.y)+lambda_/2/np.size(self.y)*np.square(self.w)
    
  def grad_descent(self,l_rate,no_of_iter,lambda_=0):  #gradient descent
        m=np.size(self.y)
        for i in range(no_of_iter):
            dif=self.x.dot(self.w)+self.b-self.y
            self.w -= l_rate / m * self.x.T.dot(dif) + lambda_ / m * self.w
            self.b -= np.sum(l_rate / m * dif)
        return self.w,self.b
    
    def predict(self,xin):        #predicts results for the test data
        return np.dot(xin,self.w)+self.b
    
    def accuracy(self,x,y):       #tests accuracy of the predicted data
        y_pred = self.predict(x)
        err = abs(np.mean((y-y_pred)/y))
        return (1-err)*100
    


# In[ ]:





# In[ ]:




