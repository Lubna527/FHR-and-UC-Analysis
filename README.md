# FHR-and-UC-Analysis
 Analyzing FHR (Fetal Heart Rate) and UC (Uterine Contractions) and plotting the graphs. Perform FHR analysis over time epochs, and analyzing peaks in the UC graph to provide insights.
a. Introduction
The goal of this project is to analyze Fetal Heart Rate (FHR) and Uterine Contractions (UC) data for monitoring fetal well-being. The analysis involves generating visualizations, detailed epoch-based statistics for FHR, and detecting UC peaks.

b. Methodology
    1. Data Loading and Preprocessing: The dataset is loaded from a CSV file, and time values are converted from milliseconds to seconds for ease of understanding.
    2. Data Visualization: Line plots are created to visualize trends in FHR and UC over time.
    3. Epoch Analysis: FHR is analyzed in 3.75-second epochs, and the average FHR in BPM and corresponding pulse intervals are computed.
    4. Peak Detection: The UC signal is analyzed to detect peaks. The duration of these peaks is measured, and the number of peaks wider than 30 seconds is calculated.
    
c. Results
Plots effectively demonstrate the variations in FHR and UC over time.
Detailed epoch analysis provides insights into average FHR and pulse intervals.
Peak detection identifies significant UC peaks, with detailed statistics on their widths and average durations.

d. Comparison of Approaches
While the current approach uses a straightforward method for epoch analysis and peak detection, several alternatives could be considered:
    1. Machine Learning: Utilizing supervised learning methods for classification tasks related to fetal distress could provide deeper insights.
    2. Signal Processing Techniques: Advanced methods like wavelet transforms could enhance peak detection and noise filtering.
    
e. Conclusion
The proposed methodology successfully analyzes FHR and UC data, providing crucial insights into fetal well-being. Future work could explore more advanced techniques for improved accuracy and insight generation.
