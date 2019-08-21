x <- as.data.frame(data[,c(5,8,9,10)])
ncp <- length(unique(x$Predation)) #Number of classes of Predation
ncd <- length(unique(x$Danger)) #Number of classes of Danger
res <- matrix(NA,ncp*ncd,5)
k <- 1
for (i in 1:ncp) {
for (j in 1:ncd) {
if (length(x$TotalSleep[(x$Predation == i) & (x$Danger == j)]) > 0) {
aux <- x$TotalSleep[(x$Predation == i) & (x$Danger == j)]
res[k,] <- c(min(aux),mean(aux),max(aux),i,j)
} else {
res[k,] <- c(0,0,0,i,j)
}
k <- k+1
}
}
colnames(res) <- c("MinTS", "MeanTotalSleep", "MaxTS", "Predation", "Danger")
res <- as.data.frame(res)
ggplot(data = res, aes(x = Predation, y = Danger)) +
geom_tile(aes(fill = MeanTotalSleep), colour = "white") +
scale_fill_gradient(low = "white", high = "steelblue")