[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (Weight vs. Age)

##### Problem: Make a scatter plot of birth weight vs. mother's age. Plot percentiles of birth weight vs. mother's age. Compute Pearson's and Spearman's correlations. How would you characterize the relationship between these variables?


Scatter plot of birth weight vs. mother's age
> <img src="https://github.com/kevntao/dsp/blob/master/statistics/images/weight-age.png?raw=true" width=400 height=300>  

Plot of percentiles of birth weight vs. mother's age
> <img src="https://github.com/kevntao/dsp/blob/master/statistics/images/weight-age2.png?raw=true" width=400 height=300>  

Pearson's Correlation
> In [15]: thinkstats2.Corr(df.agepreg, df.totalwgt_lb)  
> Out[15]: 0.068833970354109056  

Spearman's Correlation
> In [16]: thinkstats2.SpearmanCorr(df.agepreg, df.totalwgt_lb)  
> Out[16]: 0.094610041096582262  

My Findings:
> The scatterplot does not show any significant relationship between the 2 variables as there is no correlation
