# Global events tone visualizer
A simulator to visualize global events and their tone.

![insights_hotspot_4_max_news_events](https://user-images.githubusercontent.com/22005866/143729754-75c9922b-b45d-4b7e-81a6-1e563f0c3d1f.png)

## Live Demo
Check out the <a href="https://jayant11.github.io/global-events-tone-visualizer/">Live Demo</a>!

## Dataset
Global Database of Events, Language and Tone (<a href="https://www.gdeltproject.org/data.html#rawdatafiles">GDELT</a>)
Data format is well explained in the following <a href="http://data.gdeltproject.org/documentation/GDELT-Event_Codebook-V2.0.pdf">codebook</a>.

### Note
- Unzip `processed_data.csv.zip` in project root to save time and resources. Please ensure that it unzips to a file named `processed_data.csv`
- If `processed_data.csv` is not found then program will automatically generate it during execution.

## Steps
1. Run `python -m pip install -r requirements.txt` to install the required packages. Windows users can run `py -m pip install -r requirements.txt`.
2. Run `python main.py` to execute the program.
3. On completion, a `covid_visualizer.html` file would be generated which can be hosted live or shared with you team for interactive simulations.

## Methodology
The design of our solution pipeline can be grouped into three main categories, namely, data extraction, data processing, and data visualization.

#### 1. Data Extraction
In our `extract.py` module, we call the download method, which uses a date range to download the dataset from the GDELT servers to the `dataset` folder at the root directory, which is then extracted in a `temp` directory. As most of the systems would be unable to read and process this massive amount of information, we use the power of parallel computing via Spark (or PySpark) to extract the data from CSV into a Spark data frame.

#### 2. Data Processing
While we are using parallel processing to extract the data in our program, the data is still massive to fit in the memory. There are 61 attributes in the raw data with an overall size of 43.8 GB. Therefore, we use the technique of feature reduction to select only the most essential attributes required for data processing. These tasks are handled by the data transformation module `transformer.py`. We then web scrape the URLs of news articles to perform text analysis and select the top 2000 artcles for each date according to their COVID-19 relavency.

#### 3. Data Visualization
To create our visualizer, we use the geodata of the news article (provided by the GDELT project as a feature) to map the simulation and display how positive and negative pandemic news travels across the globe. The package used for the visualizer is 'keplergl,' which is written mainly in Javascript and Python. It is a powerful open-source library for geospatial analysis that can be used with extremely large datasets. For the final step, we use the `load.py` module in our program to load the processed data into the visualizer map and export it as `covid_visualizer.html` file. This file can be shared or even hosted online for public access.

## Results
The Data Extraction part of the Methodology section, using Spark significantly improved resource allocation. Looking closer, we observed that the CPU performance improved by 36% and the memory performance also improved by 14%.

In our simulation as in figure below, we observed that, at the very beginning of year 2020, news-hotspots were present in China, India, and a few European countries. But it was sparse and not widespread. The slider in our simulation allows us to look at the simulation at other times, such as the latter part of 2020, when the news got around the world.

![insights_hotspot_1_starts_china](https://user-images.githubusercontent.com/22005866/143729790-102189c1-5a98-4924-9334-a78fcdfa486f.png)

The simulation slider is moved to March 2020 (more specifically, 03/10/2020 - 03/24/2020). We chose this time period to observe the simulation results when the World Health Organization (WHO) declared COVID-19 to be a global pandemic (WHO, 2020). The yellow dots symbolize higher density of the news spread.

![insights_hotspot_4_max_news_events](https://user-images.githubusercontent.com/22005866/143729806-65cd0156-2b87-4185-a3dc-0d7abd05d27a.png)

At the beginning of 2020 (precisely 01/16/2020 - 01/17/2020), the COVID-19 news originated from China and travelled to many other regions in Asia (e.g.: India, Nepal, Pakistan and China), North America (e.g.: the United States and Canada) and Europe (the United Kingdom and France). The yellow arc lines emphasize a more significant impact of the news that spread, whereas red lines symbolize less impact news.

![insights_arc_1_china_linked](https://user-images.githubusercontent.com/22005866/143729811-42e8d4c7-7197-4fab-9931-2380ce262eb9.png)

In the next figure, we can clearly see how much the news of COVID-19 had spread by the 11th of March in 2020 (03/11/2020 - 03/13/2020). The news announced by the WHO propelled the discussion about the pandemic, its impact on society, and ways to understand and combat it.

![insights_arc_2_who_declared_global_pandemic_11march](https://user-images.githubusercontent.com/22005866/143729818-2715c3c4-433b-46b4-87a7-6be3bfe449cd.png)
