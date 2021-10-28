df1 = read.csv('stonks_15sec_per_hour.csv')
df2 = read.csv('stonks_5min_per_week.csv')
df3 = read.csv('stonks_hour_per_month.csv')
df4 = read.csv('stonks_day_per_5years.csv')

out = 'plot.pdf'
if (file.exists(out)) {
    file.remove(out)
}
pdf(file=out, width=10, height=7, onefile=FALSE)
plot.new()
par(mfrow=c(2,2))

plot(df1$Streaks, df1$Gains, xlab='Streak', ylab='% gain', xaxt='n', yaxt='n')
title('Every 15 seconds over an hour')
axis(1, at=seq(-8, 8, 2))
axis(2, at=seq(-0.2, 0.2, 0.1))

plot(df2$Streaks, df2$Gains,  xlab='Streak', ylab='% gain', xaxt='n', yaxt='n')
title('Every 5 minutes over a week')
axis(1, at=seq(-8, 8, 2))
axis(2, at=seq(-1.5, 1.5, 0.5))

plot(df3$Streaks, df3$Gains,  xlab='Streak', ylab='% gain', xaxt='n', yaxt='n')
title('Every hour over a month')
axis(1, at=seq(-8, 8, 2))
axis(2, at=seq(-5, 5, 1))

plot(df4$Streaks, df4$Gains,  xlab='Streak', ylab='% gain', xaxt='n', yaxt='n')
title('Every day over 5 years')
axis(1, at=seq(-12, 12, 3))
axis(2, at=seq(-50, 50, 20))

dev.off()