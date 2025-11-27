# urban-network-analysis


This repository contains the source code for the research article [The 15-minute city in the Global South: Modeling spatial accessibility and measuring social equity across seven major Iranian cities](https://www.sciencedirect.com/science/article/pii/S2667091725000706) published in the Journal of Urban Mobility. With this code in hand, you will be able to automatically (1) retrieve Point of Interests (POIs) from OpenStreetMap (OSM), (2) assign them into eight different amenity categories, including education, entertainment, grocery, health, posts and banks, parks, sustenance, and shops, and then (3) compute walking time from every network node (orgin) to the nearest POI in each category types. Overall, using `final_version.ipynb`, you can develop your own 15-minute framework for any city worldwide,  simply provide an appropriate CRS and assign a city name in predefined locations. To showcase your final result(s), you can also use this `Pydeck_15MinC_Tehran.ipynb` to allow potential users to engage with maps in an interactive environment. 

<img src= "https://github.com/user-attachments/assets/bda2eb95-1e9d-4216-a17a-ed3896048b46" alt=" Analytical workflow for computing the walking travel time matrix" align="center" width="600px">

## Citation

If this work was useful, please make sure to cite it as follows:


#### APA:
> Badakhshan, B., Sharifi, A., & Ramezani, S. (2025). The 15-minute city in the Global South: Modeling spatial accessibility and measuring social equity across seven major Iranian cities. Journal of Urban Mobility, 8, 100168. https://doi.org/10.1016/j.urbmob.2025.100168

#### BibTeX:



```
Babak Badakhshan, Ayyoob Sharifi, Samira Ramezani,
The 15-minute city in the Global South: Modeling spatial accessibility and measuring social equity across seven major Iranian cities,
Journal of Urban Mobility,
Volume 8,
2025,
100168,
ISSN 2667-0917,
https://doi.org/10.1016/j.urbmob.2025.100168.
(https://www.sciencedirect.com/science/article/pii/S2667091725000706)
Abstract: As cities around the globe strive to improve urban sustainability and resilience while tackling challenges like climate change, Moreno's 15-minute city model is becoming increasingly popular in urban planning research and practice. Several previous studies have applied different spatial modeling frameworks to assess whether contemporary cities align with the vision of this model. To date, few studies have focused on the applicability of this model in Global South cities. As such, further empirical research is required to advance our understanding of the global relevance of the 15-minute city concept beyond narratives predominantly rooted in Western urbanism. Our study aims to fill this gap by operationalizing the model for seven major Iranian cities and highlighting the relationships between social exclusion and inequitable access to everyday needs. We show significant variation in the levels of walking access to different activity location categories within and across the study cities, with inner areas exhibiting better access and marginal areas showing poorer access to essential services. Furthermore, residents’ deprivation level was strongly associated with a higher probability of reaching everyday services beyond a 15-minute walk— except for two cities. We discuss that although in study cities essential amenities are, to some extent, accessible within a 15-minute walk or bike ride, significant socio-cultural, institutional, and infrastructural barriers; such as, imposed restrictions on women’s cycling, inadequate active travel infrastructure, and the persistent non-recognition of walking as a legitimate mode of transportation continue to hinder the meaningful implementation of the model in Iranian context.
Keywords: 15-minute city; Walkability; Accessibility; Urban planning; Neighborhood; Chrono-urbanism
```


## Maintainer(s)


Babak Badakhshan, MSc


## License


This project is licensed under the terms of [the MIT license](https://opensource.org/license/mit).
