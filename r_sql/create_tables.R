library(DBI)

initialise_db <- function() {
  db_filename <- "airline2.db"
  
  # change working directory
  current_wd = getwd()
  setwd('../..')
  
  if (file.exists(db_filename)) {
    file.remove(db_filename)
  }
  
  conn <- dbConnect(RSQLite::SQLite(), db_filename)
  
  # restore working directory
  setwd(current_wd)
  
  return(conn)
}


create_tables <- function(conn) {
  current_wd = getwd()
  setwd('../../dataverse_files')
  
  airports <- read.csv("airports.csv", header = TRUE)
  carriers <- read.csv("carriers.csv", header = TRUE)
  planes <- read.csv("plane-data.csv", header = TRUE)
  
  dbWriteTable(conn, "airports", airports)
  dbWriteTable(conn, "carriers", carriers)
  dbWriteTable(conn, "planes", planes)
  
  # restore working directory
  setwd(current_wd)
}