library(ggplot2)

dat = read.table("btlens.txt")

aplot = ggplot(data = dat, aes(V1))+ geom_histogram()+
    geom_vline(xintercept=98)+
    geom_vline(xintercept=197)+
    geom_vline(xintercept=246)

pdf("btlens.pdf", height=3, width=4)
aplot
dev.off()
