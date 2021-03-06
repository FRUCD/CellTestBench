setwd("C:/Users/Schuyler/Documents/Formula/CellTestBench/Data")
graphAll <- function() {
  for (f in dir()) {
    #jpeg(paste('Graphs/', tools::file_path_sans_ext(f),'.jpg',sep=""), width=800, height=600)
    dev.new(width=8,height=6,noRStudioGD = TRUE)
    print(f)
    data <- read.table(f, header=T, sep=",")
    time <- (0:(nrow(data) - 1)) * 200
    volt <- data[,1]
    plot(time, volt, type="n", axes=T)#xaxt="n")
    xax <- seq(0, time[length(time)], 1000)
    #xaxRed <- xax[seq(1, length(xax), 2)]
    #xaxBlack <- xax[seq(0, length(xax), 2)]
    #axis(side = 1, at = , col.ticks=)
    #axis(side = 1, at = xaxRed, col.ticks="red", labels=T)
    axis(side = 1, at = xax, col.ticks="black", labels=F)
    #axis(side = 1, at = xaxBlack, col.ticks="black", labels=F)
    #axis(side = 2, at = seq(4.08,4.16, .01), labels=F)
    lines(time, volt)
    grid(nx=length(xax), ny=NULL)
    title("Voltage over time", f)
    dev.off()
  }
}

processAll <- function() {
  d <- matrix(ncol = 3)
  
  for (i in 1:length(dir())) {
    f <- paste(i, "chargeData.csv", sep="")
    data <- read.table(f, header=T, sep=",")
    volt <- data[,1]
    ocv <- mean(volt[3:6])
    tailvolt <- mean(volt[(length(volt) - 50):(length(volt) - 40)])
    delt <- tailvolt - ocv
    d <- rbind(d, c(ocv, tailvolt, delt))
  }
  d <- d[-1,]
  colnames(d) <- c("OCV", "TailVolt", "Diff")
  rownames(d) <- 1:length(dir())
  
  write.csv(d,file="data.csv")
}