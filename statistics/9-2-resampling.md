[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (Resampling)

##### Problem: In "Testing a Difference in Means", we simulated the null hypothesis by permutation; that is, we treated the observed values as if they represented the entire population, and randomly assigned the members of the population to the two groups.
##### An alternative is to use the sample to estimate the distribution for the population, then draw a random sample from that distribution. This process is called resampling.  There are several ways to implement the resampling, but one of the simplest is to draw a sample, with replacement, from the observed values, as in "Power".
##### Write a class named DiffMeansResample that inherits from DiffMeansPermute and overrides RunModel to implement resampling, rather than permutation.

    class DiffMeansResample(hypothesis.DiffMeansPermute):
        def RunModel(self):
            group1 = np.random.choice(self.pool, self.n, replace=True)
            group2 = np.random.choice(self.pool, self.m, replace=True)
            return group1, group2

##### Use this model to test the differences in pregnancy length and birth weight.  How much does the model affect the results?

> Pregnancy Length  
> p-value:  0.1674  
> actual:   0.0780372667775  
> ts max:   0.226752436104  

> Birth Weight  
> p-value:  0.0  
> actual:   0.124761184535  
> ts max:   0.112243501197  

> Resampling has minimal effect on the results vs permutation.  
