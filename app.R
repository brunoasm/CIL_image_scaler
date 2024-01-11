library(shiny)
source('add_scale_bar.R')

options(shiny.maxRequestSize = 10 * 1024^3)

ui <- fluidPage(
  titlePanel("Green and Purple Stations Scale Bar Addition"),
  sidebarLayout(
    sidebarPanel(
      fileInput("file1", "Choose TIFF File(s)", multiple = TRUE, accept = c(".tif", ".tiff"))
    ),
    mainPanel(
      uiOutput("downloadUI")
    )
  )
)

server <- function(input, output) {
  processed_files <- reactiveVal(NULL)
  
  output$downloadUI <- renderUI({
    if (!is.null(processed_files())) {
      downloadButton("download", "Download Processed Images")
    }
  })
  
  observeEvent(input$file1, {
    req(input$file1)
    
    withProgress(message = 'Processing images...', value = 0, {
      total <- length(input$file1$datapath)
      for (i in seq_along(input$file1$datapath)) {
        incProgress(1 / total, detail = paste("Processing", input$file1$name[i]))
        
        original_file_name <- input$file1$name[i]
        temp_filepath <- input$file1$datapath[i]
        
        # Call the updated add_scale_bar function with the original file name
        add_scale_bar(original_file_name, temp_filepath, "scale_info.csv", 100, 100)
      }
      
      # Zip files
      #zip_path <- tempfile(fileext = ".zip")
      #zip(zip_path, list.files("output", full.names = TRUE))
      #processed_files(zip_path)
    })
  })
  
  #output$download <- downloadHandler(
    #filename = function() { "processed_images.zip" },
    #content = function(file) {
     # file.copy(processed_files(), file)
    #}
  #)
}

shinyApp(ui = ui, server = server)
