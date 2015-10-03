#Assignment 1
For the assignment 1, I chose six distributions that were poisson, binomial, Chi-square, normal, uniform, and exponential distribution. All these distributions had the same sample means 100.
mymean=100
df=100
mysize=2000/(np.array(range(1,100)+[10]))
md={}
means={}
md['pois'][n] = np.random.poisson(df, size=n)
md['binomial'][n] = np.random.binomial(200, 0.45, size=n)
md['chisq'][n] = np.random.chisquare(df, size=n)
md['normal'][n] = np.random.normal(100, 200, size=n)
md['uniform'][n] = np.random.uniform(df, size=n)
md['exponential'][n] = np.random.exponential(df, size=n)
#Assignment2
<<<<<<< HEAD
<<<<<<< HEAD
#Assignment 2
#Assignment2
For assignment 2, I follow and understand notebook and repeat the z-test and Chi-square test for other data included in the paper we are working with by filling missing celss in the notebook.
For assignment 2, I repeat the z-test and chisq test for other data included in the paper we are working with by fill in missing cells in the notebook.
=======
>>>>>>> b28f3d787ed0d17209c6ce8869332ee89ba3ad96
I repeat the z-test and the chisq test for other data included in the paper we are working with
=======
>>>>>>> b28f3d787ed0d17209c6ce8869332ee89ba3ad96
