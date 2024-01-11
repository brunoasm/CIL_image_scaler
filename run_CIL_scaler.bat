@echo off
Rscript -e "if (!require(\"shiny\")) install.packages(\"shiny\"); library(shiny); shiny::runGitHub(\"brunoasm/CIL_image_scaler\", launch.browser = TRUE)"
