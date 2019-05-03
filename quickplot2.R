library(ggplot2)

dat = read.table("btlens2.txt")

aplot = ggplot(data = dat, aes(V1))+ geom_histogram()+
    geom_vline(xintercept=100)+
    geom_vline(xintercept=230)

pdf("btlens2.pdf", height=3, width=4)
aplot
dev.off()
