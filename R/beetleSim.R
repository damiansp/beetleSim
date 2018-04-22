#---------#---------#---------#---------#---------#---------#---------#---------
rm(list=ls())

# Set up model parameters
START_DATE <- c(1900, 1) # All dates: c(Year, Month)
START_TEMP <- 13
X_DIM <- 10
Y_DIM <- 10
CELL_SIZE <- 10 # in km
BEETLE_MEAN_DISPERSAL_DISTANCE <- 15 # km
BEETLE_SD_DISPERSAL_DISTANCE <- 5
MEAN_ANNUAL_TEMP_INCREASE <- 0.01
SD_ANNUAL_TEMP_INCREASE <- 0.03



# Data set up------------------------------------------------------------
init.grid <- function(x.dim, y.dim) {
  x <- rep(1:x.dim, y.dim)
  y <- unlist(lapply(1:y.dim, function(x) rep(x, x.dim)))
  grid <- data.frame(x=x, y=y)
  grid
}


# Assign mean temp to cell (random for now--later as f(x, y))
add.temp.mean <- function(grid) {
  grid$temp.mean <- rnorm(nrow(grid), 13, 10)
  grid
}


add.temp.sd <- function(grid) {
  grid$temp.sd <- abs(rnorm(nrow(grid), sd=20))
  grid
}


add.precip.mean <- function(grid) {
  grid$precip.mean <- rexp(nrow(grid), 0.1)
  grid
}


add.precip.sd <- function(grid) {
  grid$precip.sd <- rpois(nrow(grid), 10)
  grid
}


add.tree.coverage <- function(grid) {
  grid$tree <- pmax(pmin(rnorm(nrow(grid), 0.7, 0.1), 1), 0)
  grid
}


add.beetle.coverage <- function(grid) {
  grid$beetle <- pmax(pmin(rnorm(nrow(grid), 0.01, 0.03), 1), 0)
  grid
}


create.grid <- function(x.dim, y.dim) {
  grid <- init.grid(x.dim, y.dim)
  grid <- add.temp.mean(grid)
  grid <- add.temp.sd(grid)
  grid <- add.precip.mean(grid)
  grid <- add.precip.sd(grid)
  grid <- add.tree.coverage(grid)
  grid <- add.beetle.coverage(grid)
  grid
}





# Events---------------------------------------------------------------
increment.month <- function(year.month) {
  year.month[2] <- year.month[2] + 1
  if (year.month[2] > 12) {
  	year.month[1] <- year.month[1] + 1
  	year.month[2] <- 1
  }
  year.month
}


# update temp


# update precip


# update tree pop as f(precip)


# beetle reproduce as f(tree)


# beetle disperse as f(dispersal)


# beetle mortality as f(temp)



# Output plots---------------------------------------------------------
get.matrix <- function(grid, field) {
  x.max <- max(grid$x)
  y.max <- max(grid$y)
  mat <- matrix(nrow=x.max, ncol=y.max)
  for (i in 1:nrow(grid)) {
  	x <- grid[i, 'x']
  	y <- grid[i, 'y']
  	cell.value <- grid[i, field]
  	mat[x, y] <- cell.value
  }
  mat
}


# Tree or beetle grid
plot.grid <- function(grid, field) {
  mat <- get.matrix(grid, field)
  par(mar=c(rep(0.5, 4)))
  image(mat, 
        zlim=c(0, 1), 
        col=colorRampPalette(c('red', 'green'))(20), 
        xaxt='n', 
        yaxt='n')
}



get.global.population <- function(grid, field) {
  if (!(field %in% c('tree', 'beetle'))) {
  	stop(
  	  'get.global.population() can only take "tree" or "beetle" as field args')
  }
  sum(grid[, field]) / nrow(grid)
}



# Beetle grid


# Global tree and beetle populations


# Global temp and precipitation


get.temperature.forecast <- function(years) {
  months <- 12 * years
  mean.global.temp <- numeric(years)
  mean.global.temp[1] <- start.temp
  for (year in 2:years) {
  	temp.increase <- rnorm(
  	  1, MEAN_ANNUAL_TEMP_INCREASE, SD_ANNUAL_TEMP_INCREASE)
  	mean.global.temp[year] <- mean.global.temp[year - 1] + temp.increase
  }
  mean.global.temp	
}


main <- function(start.date, start.temp, years=100) {
  mean.global.temp <- get.temperature.forecast(years)
  plot(mean.global.temp, type='l')
  # Placeholders to track elapsed time, tree, and beetle population histories
  elapsed.months <- 1:(months)
  tree.history <- numeric(months)
  beetle.history <- numeric(months)
  
  grid <- create.grid(X_DIM, Y_DIM)
  
  for (m in 1:months) {
  	tree.history[m] <- get.global.population(grid, 'tree')
  	beetle.history[m] <- get.global.population(grid, 'beetle')
  }
  
  
  head(grid)
}


main(START_DATE, START_TEMP)