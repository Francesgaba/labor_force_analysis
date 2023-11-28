# labor_force_analysis
Woman labor force analysis 
# introduction 

The dataset I've chosen for examination is the 'Mroz' data frame from the Panel Study of Income Dynamics (PSID), sourced from R's dataset collection. This dataset contains observations of married women in the U.S., focusing on their labor force participation and its influencing factors. Each entry in this dataset is associated with a specific married woman, highlighting details about her and her family's demographic and economic conditions. It comprises eight attributes: lfp, k5, k618, age, wc, hc, lwg, and inc.

source from :https://vincentarelbundock.github.io/Rdatasets/doc/carData/Mroz.html
        
the core research question we are going to analyze is How do factors such as the number of children, age, educational background of both the wife and husband influence the labor-force participation of married women in the U.S.

Here is the description variable:

| Variable of dataset   | description                                                                                                                                                                                                 |
|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| lfp                      | Labor-force participation; a factor with levels: no; yes                                                                                                                             |
| k5                       | Number of children 5 years old or younger                                                                                                                                            |
| k618                     | Number of children 6 to 18 years old                                                                                                                                                 |
| age                      | Age in years                                                                                                                                                                         |
| wc                       | Wife's college attendance; a factor with levels: no; yes                                                                                                                             |
| hc                       | Husband's college attendance; a factor with levels: no; yes                                                                                                                          |
| lwg                      | Log expected wage rate; for women in the Labor force, the actual wage rate; for women not in the labor force, an imputed value based on the regression of lwg on the other variables |
| inc                      | Family income exclusive of wife's income                                                                                                                                      
