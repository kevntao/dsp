[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (Scoring)

##### Problem: In games like hockey and soccer, the time between goals is roughly exponential.  So you could estimate a team's goal-scoring rate by observing the number of goals they score in a game.  This estimation process is a little different from sampling the time between goals, so let's see how it works.
##### Write a function that takes a goal-scoring rate, lam, in goals per game, and simulates a game by generating the time between goals until the total time exceeds 1 game, then returns the number of goals scored.

	def playGame(lam):
    	numgoals = 0  
    	time = 0  
    	while time < 1:  
    		addtime = random.expovariate(lam)  
    	    time += addtime  
    	    numgoals += 1  
    	return numgoals

##### Write another function that simulates many games, stores the estimates of lam, then computes their mean error and RMSE.

	def stats8p3(lam):
		estimatearray = []  
		numgames = 999999  
		for i in range(numgames):  
		    result = playGame(lam)  
		    estimatearray.append(result)  
		print RMSE(estimatearray, lam)  
		print MeanError(estimatearray, lam)  

> In [49]: stats8p3(2)  
> ('RMSE: ', 1.7320871802902993)  
> ('Mean Error: ', 0.99936599936599935)  
	
##### Is this way of making an estimate biased?  Plot the sampling distribution of the estimates and the 90% confidence interval.  What is the standard error?  What happens to sampling error for increasing values of lam?

> I believe this estimation is unbiased as it is only restricted by the amount of time for the game.

> <img src="https://github.com/kevntao/dsp/blob/master/statistics/images/scoringhist.png?raw=true" width=400 height=300>  
> <img src="https://github.com/kevntao/dsp/blob/master/statistics/images/confinterval.png?raw=true" width=400 height=300>  

> Standard Error: 1.7320871802902993
> Sampling error does not fluctuate much even with increasing values of lam.

