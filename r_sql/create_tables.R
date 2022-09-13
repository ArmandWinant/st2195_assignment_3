library(DBI)

initialise_db <- function() {
  working_directory = getwd()
  setwd('..')
  
  db_filename <- "airline2.db"
  
  # remove the db file if it exists
  if (file.exists(db_filename))
    file.remove(db_filename)
  
  # create database and open connection
  conn <- dbConnect(RSQLite::SQLite(), db_filename)
  
  # restore the initial working directory
  setwd(working_directory)
  
  return (conn)
}