parse_data <- function(filename) {
  lines <- readLines(filename)
  
  # Filter lines to extract player info and details
  player_info_lines <- lines[seq(3, length(lines)-1, 4)]
  player_detail_lines <- lines[seq(4, length(lines), 4)]
  
  # Define the widths of columns based on fixed-width formatting
  info_widths <- c(5, 32, 5, 6, 6, 6, 6, 6, 6, 6)
  detail_widths <- c(5, 35, 6, 6, 6, 6, 6, 6, 6)
  
  # Parse the lines
  info_df <- read.fwf(textConnection(player_info_lines), widths = info_widths, stringsAsFactors = FALSE, header = FALSE)
  detail_df <- read.fwf(textConnection(player_detail_lines), widths = detail_widths, stringsAsFactors = FALSE, header = FALSE)
  
  # Extract ratings
  ratings <- strsplit(trimws(detail_df$V2), " ")
  preRatings <- sapply(ratings, function(x) as.integer(substr(x[4], 3, 6)))
  postRatings <- sapply(ratings, function(x) as.integer(substr(x[5], 4, 7)))
  
  # Consolidate the data into a single dataframe
  combined_df <- data.frame(
    PairNum = as.integer(trimws(info_df$V1)),
    PlayerName = trimws(info_df$V2),
    TotalPts = as.numeric(trimws(info_df$V3)),
    USCF_ID = as.integer(trimws(substr(detail_df$V2, 3, 10))),
    PreRating = preRatings,
    PostRating = postRatings,
    Round1 = trimws(info_df$V4),
    Round2 = trimws(info_df$V5),
    Round3 = trimws(info_df$V6),
    Round4 = trimws(info_df$V7),
    Round5 = trimws(info_df$V8),
    Round6 = trimws(info_df$V9),
    Round7 = trimws(info_df$V10),
    Color1 = trimws(detail_df$V3),
    Color2 = trimws(detail_df$V4),
    Color3 = trimws(detail_df$V5),
    Color4 = trimws(detail_df$V6),
    Color5 = trimws(detail_df$V7),
    Color6 = trimws(detail_df$V8),
    Color7 = trimws(detail_df$V9)
  )
  
  return(combined_df)
}

# Load the data into a dataframe
setwd("/Users/afraser/Documents/src/cuny-datascience/data607-data-acquisition-and-management/projects/project1-parse-chess-file")
df <- parse_data("chess_tournamentinfo.txt")
print(df)

