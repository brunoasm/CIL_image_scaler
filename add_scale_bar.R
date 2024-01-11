library(magick)
library(tiff)

add_scale_bar <- function(original_file_name, image_path, csv_path, x_coord, y_coord) {
  # Read the scale information from the CSV file
  scale_info <- read.csv(csv_path)
  
  # Determine the scale size and label based on camera make and match pattern
  scale_size_pixels <- NULL
  scale_label <- NULL
  for (row in 1:nrow(scale_info)) {
    if (grepl(scale_info$match_pattern[row], original_file_name)) {
      scale_size_pixels <- as.integer(scale_info$scale_size_pixels[row])
      scale_label <- as.character(scale_info$scale_label[row])
      break
    }
  }
  
  if (is.null(scale_size_pixels)) {
    print("No matching scale information found.")
    return(NULL)
  }
  
  # Read the original image
  original_image <- image_read(image_path)
  
  # Get the dimensions of the original image
  width <- image_info(original_image)$width[1]
  height <- image_info(original_image)$height[1]
  
  # Adjust y_coord for bottom-left origin
  y_coord <- height - y_coord
  
  # Create a scale bar
  scale_bar <- image_blank(width = width, height = height, color = "none") %>%
    image_draw() 
  rect(xleft = x_coord, ybottom = y_coord - 10, xright = x_coord + scale_size_pixels, ytop = y_coord, 
       col = "white", border = "white")
  dev.off()
  
  # Create a label as a separate image using base R graphics
  label_file <- tempfile(fileext = ".png")
  png(label_file, width = width, height = height, bg = "transparent")
  par(mar = c(0, 0, 0, 0))
  plot(0, 0, type = "n", xlim = c(0, width), ylim = c(0, height), ann = FALSE, axes = FALSE)
  text(x = x_coord-100, y = height - y_coord-50, labels = scale_label, col = "white", cex = 6, pos=1, offset=)  # Adjust 'cex' for size
  dev.off()
  
  # Read the label image
  label_text_image <- image_read(label_file)
  
  # Merge and flatten images
  final_combined_image <- image_flatten(c(original_image,label_text_image,scale_bar), operator = "over")
  
  # Create 'output' directory if it doesn't exist
  output_dir <- "images_with_scale"
  if (!dir.exists(output_dir)) {
    dir.create(output_dir)
  }
  
  # Save the final combined image in 'output' directory
  output_file_path <- file.path(output_dir, basename(sub("\\.[^.]*$", "_scaled.tif", original_file_name)))
  image_write(final_combined_image, output_file_path)
  
  # Optionally, delete the label file to clean up
  if (file.exists(label_file)) {
    file.remove(label_file)
  }
}
