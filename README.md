# ONCOLOGY HEALTHCARE NETWORK ANALYSIS – NEW YORK

**Tools:** Pandas, Excel, Power BI, DAX

**Project Type:** End-to-End Healthcare Network Analytics Project

---

## 1. Project Overview

This project analyzes the healthcare network across New York, focusing on the distribution of oncology specialists, healthcare accessibility, specialization diversity, and patient engagement. The analysis was performed using Pandas and Power BI to identify patterns within the healthcare provider network.

---

## 2. Business Problem

The analysis aims to evaluate the healthcare network across New York by examining the distribution of oncology specialists, healthcare accessibility, specialization diversity, and patient engagement.

### Key Questions Addressed

- Which cities have the highest number of doctors?
- Which cities have the greatest diversity of doctor specializations?
- Which cities appear to have limited healthcare coverage and specialist diversity?
- Which specializations receive the highest patient engagement?
- Which specializations are most common and which are least represented?
- Is there a relationship between website availability and patient review counts?

---

## 3. Dataset Description

A structured directory of 640 oncologists, hematologists, and cancer care specialists across New York City, sourced from the Google Places API.

### Dataset Size

- Records: 640
- Domain: Healthcare
- Source: Google Places API

### Dataset Columns

- place_id
- name
- categoryName
- categories
- address
- street
- city
- state
- countryCode
- phone
- website
- reviewsCount
- url

---

## 4. Tools Used

- **Pandas** – Data exploration, KPI calculation, and business analysis
- **Excel** – Data exploration and insight discovery
- **Power BI** – Dashboard development and data visualization
- **DAX** – KPI and measure creation within Power BI

---

## 5. Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. KPI Calculation
5. Insight Generation
6. Dashboard Development
7. Business Recommendations

---

## 6. Challenges Faced

- Handling missing values in review data.
- Determining whether website presence influences patient engagement.
- Extracting meaningful insights from a directory-based dataset.
- Converting business questions into Pandas analysis.
- Interpreting healthcare specializations and categories.

---

## 7. KPIs Analyzed

The following KPIs were analyzed to understand the healthcare network across New York:

- Total Doctors
- Total Cities
- Total Specializations
- Total Doctors by City
- Doctors by Specialization
- Rare Specializations
- Top Reviewed Doctors
- Average Reviews by Specialization
- Average Reviews by City
- Doctors with Website

---

## 8. Dashboard

### Dashboard Preview

![Dashboard Preview](dashboard.png)

### KPI Cards

| KPI | Description |
|------|-------------|
| Total Doctors | Total number of healthcare professionals in the dataset. |
| Total Specializations | Total number of unique medical specializations represented. |
| Total Cities | Total number of cities covered in the dataset. |
| Doctors with Website | Total number of doctors maintaining an online presence through a website. |

### Visualizations

- Total Doctors by City
- Total Doctors by Specialization
- Top Reviewed Doctors
- Specialization Diversity by City
- Average Patient Reviews by Specialization
- Total Doctors by Street

---

## 9. Key Insights

### Geographic Concentration of Specialists

New York City accounts for approximately 63.7% of all doctors in the dataset. Brooklyn ranks second, indicating that specialist healthcare resources are heavily concentrated in a few locations.

### High-Density Medical Locations

160 E 53rd Street emerged as the most concentrated medical location, hosting 52 doctors. This suggests the presence of a major healthcare facility or a specialized medical cluster.

### Oncology Dominates the Healthcare Network

Nearly 40% of doctors in the dataset belong to the Oncology specialization. In contrast, specialties such as Neurosurgery, Radiotherapy, Medical School, and Health Care have significantly lower representation.

### Highly Reviewed Doctors Are Mostly Oncology Specialists

The majority of top-reviewed doctors are associated with Oncology and Cancer Treatment Centers, suggesting higher patient engagement in these specialties.

### Website Presence Does Not Show a Strong Relationship with Reviews

Although doctors with websites generally appear to have higher average review counts, extreme outliers prevent a clear conclusion. The data does not provide strong evidence that website availability directly influences patient reviews.

### Larger Cities Offer Greater Specialization Diversity

New York City, Brooklyn, and Staten Island rank highly in both doctor count and specialization diversity, indicating broader healthcare service availability.

---

## 10. Recommendations

- Expand healthcare services in underserved locations with lower doctor availability.
- Improve specialist diversity in cities with limited healthcare coverage.
- Study highly reviewed oncology centers to understand drivers of patient satisfaction.
- Encourage healthcare providers to strengthen their digital presence.
- Monitor geographic concentration of specialists to improve healthcare accessibility.

---

## 11. What I Learned

- Performed end-to-end healthcare data analysis using Pandas.
- Improved proficiency in groupby(), aggregation, filtering, and KPI generation.
- Built a Power BI dashboard from analytical findings.
- Learned to validate insights before drawing conclusions.
- Improved business storytelling and recommendation writing.

---

## 12. Conclusion

This analysis examined the distribution of oncologists and cancer-care specialists across New York. The findings revealed a strong concentration of doctors in New York City, a significant dominance of Oncology as a specialization, and noticeable differences in healthcare coverage across cities. The study also highlighted variations in specialization diversity and patient engagement. These insights can help healthcare organizations identify expansion opportunities, improve specialist coverage, and enhance patient access to cancer-care services.
