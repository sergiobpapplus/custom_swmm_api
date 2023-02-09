---
title: 'swmm_api: API for reading, manipulating and running SWMM-Projects'
tags:
  - SWMM
  - Stormwater
  - Hydrology
  - Hydraulics
authors:
 - name: Pichler, Markus^[corresponding author]
   orcid: 0000-0002-8101-2163
   affiliation: 1
affiliations:
 - name: Graz University of Technology
   index: 1
date: 17 January 2022
bibliography: paper.bib
---

# Summary

The "swmm-api" package is a powerful tool for modellers and researchers who use the Storm Water Management Model (SWMM, [@swmm]). This software enables the manipulation and analysis of SWMM models, both in terms of the input data and the simulation results. The package is written in Python, making it an attractive option for those who use this language for data management and advanced analysis.

One of the key features of swmm-api is its ability to read and write SWMM import-files (.inp), allowing the user to manipulate the model structure and input data. The package also has the capability to run the SWMM model within the Python environment, providing users with quick access to simulation results. Furthermore, swmm-api can read both the report (.rpt) and binary output-files (.out), presenting the results as a Pandas DataFrame for easy analysis. The ability to read binary hotstart-files (.hst) is also included, which enables the acceleration of simulation time by using initial values stored in the file.

The swmm-api package is designed to be flexible and user-friendly, with an object-oriented structure that is lightweight and fast. The package is based on the SWMM command line syntax, making it easy to use for those familiar with this model. Additionally, swmm-api has the ability to interact with GIS data, making it a valuable tool for modellers working with spatial data.

This package has numerous research applications, including the generation and validation of student homework, the automatic updating of the SWMM model for the city of Graz using GIS databases of the sewer system, and the calibration of modified SWMM models that incorporate energy balance into the computational core. By default, swmm-api would not break if any new objects are added in future SWMM versions, making it a reliable tool for modellers and researchers.

In conclusion, the "swmm-api" package provides a valuable addition to the suite of tools available to modellers and researchers who use the SWMM. With its ability to manipulate, analyse, and visualise SWMM models, swmm-api represents a critical component for those who need to perform advanced analysis, optimisation tasks, or model calibration. Furthermore, its flexibility, ease of use, and compatibility with other data analysis tools make it an ideal choice for researchers and practitioners who want to get the most out of their SWMM models.

# A Statement of Need


The field of urban water management requires robust and efficient tools for modelling, analysis and optimization. The package "swmm-api" was developed to address these needs by providing a python interface to the Storm Water Management Model (SWMM), a widely used tool for the simulation of urban water systems. The software allows users to interact with SWMM models, read and write input files, run simulations and analyze the results. It is based on the SWMM syntax, making it a familiar and user-friendly tool for existing SWMM users.

Compared to similar tools such as "swmmr" [@leutnant:2019] written in R, the "swmm-api" package offers the advantages of being in Python, a popular programming language in the scientific community. It also has the capability to adapt to future changes in SWMM, ensuring that users will not face compatibility issues. This makes the "swmm-api" package a valuable addition to the suite of tools available to urban water management researchers and practitioners.

# Acknowledgements

The development of swmm-api would not have been possible without the support of the Institute of Urban Water Management at the University of Technology Graz. I would like to express my heartfelt gratitude to all my coworkers who provided me with valuable advice and feedback throughout the development process. Their expertise and insights were invaluable in helping me to create an API that will be of great benefit to the scientific community. Without their guidance and support, this project would not have been possible.

# References
