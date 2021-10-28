    The purpose of plot.pdf is to analyze historical
Bitcoin price data to see if streaks of 
increasing/decreasing prices affect 
the probability of the next price being an increase
or decrease.
    For example, in the plot 'Every 15 seconds over 
an hour', Bitcoin price data is collected in 15 second
intervals over the course of an hour. For a given data point,
the X axis represents how many data points were increasing or 
decreasing before it and the y axis represents how much that 
point increased or decreased from the previous. For instance
with plot 'Every 15 seconds over an hour' a point at (-4, 0.2)
had a minute straight of decreasing prices leading up to it, 
and then a 0.2% increase in price from the end of that minute. 
    Each of these plots are symmetric about y=0 so it appears
as if increases/decreases in prices across different time periods
are completely independent of prior increases/decreases. This makes
sense since it would be very easy for stock trading bots to 
exploit if they weren't independent. Too bad, or I'd be exploiting
it too!