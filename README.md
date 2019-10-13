### Introduction
This workshop will cover methods to explore, analyze, and do stuff with common data sources in a bio lab. We’ll use temperature data from probes that were connected to an incubator over the course of a week as an example. Data analysis topics include:

- Data extraction
- Data shaping
- Data slicing and aggregation
- Calculating statistics and metrics
- Plotting your data
- Protocol

### Set up

- Download Anaconda onto your laptop and install. Anaconda packages all the different tools you’ll need into one download. In this workshop we’ll make use of Jupyter Lab as an interface, Pandas for analyzing our data, and Matplotlib to plot our data.
- Start a local Jupyter sever by typing jupyter lab into the terminal (Mac/Linux) or command line (Windows)
- From the Jupyter interface in your browser, open _DIY Tools for Data Analysis.ipynb_ and follow the instructions there

The notebook starts off using that data in _demo\_data.csv_, but you can replace it with the more complex data in _biosummit\_data.csv_ or you can run ```python data_generator.py``` to make a bunch of random data to analyze.
