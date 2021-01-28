"""
An industrial company has N factories each producing some pollution every month. The company decided to
reduce the fume emissions using one or more filters. Every such filter reduces the pollution by half. 
When the second(subsequent) filter is applied, it again reduces by half the remaining pollution 
emitted after fitting the existing filter(s). You are given an array of N integers describing the
amount of pollution produced by the factories. Your tas is to find the minimum number of filters needed
to decrease the total sum of pollution by at least half.

Which given an array of integers A of length N, returns the minimum number of filters needed to reduce
the total pollution by half
"""