library(AppliedPredictiveModeling)
library(e1071)
library(caret)
data(segmentationOriginal)
true <- TRUE
True <- TRUE

# segmentation data for teh cell
segData <- subset(segmentationOriginal, Case == "Train")

cellID <- segData$Cell
class <- segData$Class
case <- segData$Case

segData <- segData[, -(1:3)]

statusColNum <- grep("Status", names(segData))
segData <- segData[, -statusColNum]


### Transformations
skewness(segData$AngleCh1)
# > skewness(segData$AngleCh1)
# [1] -0.02426252


# 2 means over columns, 1 means over rows
skewValues <- apply(segData, 2, skewness)
# > head(skewValues) 
#    AngleCh1     AreaCh1 AvgIntenCh1 AvgIntenCh2 AvgIntenCh3 AvgIntenCh4
# -0.02426252  3.52510745  2.95918524  0.84816033  2.20234214  1.90047128

### Area CH1 is skewed, you can use BoxCox to transform data into a normal
### distribution.


Ch1AreaTrans <- BoxCoxTrans(segData$AreaCh1)
Ch1AreaTrans
# Box-Cox Transformation

# 1009 data points used to estimate Lambda

# Input data summary:
#    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
#   150.0   194.0   256.0   325.1   376.0  2186.0

# Largest/Smallest: 14.6
# Sample Skewness: 3.53

# Estimated Lambda: -0.9

head(segData$AreaCh1)
# [1] 819 431 298 256 258 358

## After transformation

predict(Ch1AreaTrans, head(segData$AreaCh1))
#[1] 1.108458 1.106383 1.104520 1.103554 1.103607 1.105523

(819 ^(-.9) - 1) / (-.9)
# [1] 1.108458
### END BOX COX


### begin caret.preprocess, this is for PCA

# In summary, PCA is being used here to extract the most important patterns from your dataset, reduce its complexity, and make it easier to analyze and visualize.

#PRCOMP Principal Component (analysis)
pcaObject <- prcomp(segData, center = TRUE, scale. = TRUE)


percentVariance <- pcaObject$sd^2/sum(pcaObject$sd^2)*100
# percentVariance <- pcaObject$sd^2/sum(pcaObject$sd^2)*100 calculates the percentage of the total variance in the dataset that is captured by each principal component.

percentVariance[1:3]
# [1] 20.91236 17.01330 11.88689
# percentVariance[1:3] shows the percentage of total variance captured by the first three principal components. In your case, PC1 explains about 20.91%, PC2 about 17.01%, and PC3 about 11.89% of the variance.





# Centered and stored in sub object X 
head(pcaObject$x[,1:5])
#           PC1        PC2         PC3       PC4        PC5
# 2   5.0985749  4.5513804 -0.03345155 -2.640339  1.2783212
# 3  -0.2546261  1.1980326 -1.02059569 -3.731079  0.9994635
# 4   1.2928941 -1.8639348 -1.25110461 -2.414857 -1.4914838
# 12 -1.4646613 -1.5658327  0.46962088 -3.388716 -0.3302324
# 15 -0.8762771 -1.2790055 -1.33794261 -3.516794  0.3936099
# 16 -0.8615416 -0.3286842 -0.15546723 -2.206636  1.4731658

# -> sub object "rotation" stores variable loadings where predictor variables and columns are associated with components.

head(pcaObject$rotation[,1:3])
# > head(pcaObject$rotation[,1:3])
#                      PC1         PC2          PC3
# AngleCh1     0.001213758 -0.01284461  0.006816473
# AreaCh1      0.229171873  0.16061734  0.089811727
# AvgIntenCh1 -0.102708778  0.17971332  0.067696745
# AvgIntenCh2 -0.154828672  0.16376018  0.073534399
# AvgIntenCh3 -0.058042158  0.11197704 -0.185473286


trans <- preProcess(segData, method = c("BoxCox", "center", "scale", "pca"))
trans
# Created from 1009 samples and 58 variables

# Pre-processing:
#   - Box-Cox transformation (47)
#   - centered (58)
#   - ignored (0)
#   - principal component signal extraction (58)
#   - scaled (58)

# Lambda estimates for Box-Cox transformation:
#     Min.  1st Qu.   Median     Mean  3rd Qu.     Max. 
# -2.00000 -0.50000 -0.10000  0.05106  0.30000  2.00000 

# PCA needed 19 components to capture 95 percent of the variance

# apply thee transformations
transformed <- predict(trans, segData)
head(transformed[,1:5])
#           PC1        PC2        PC3       PC4        PC5
# 2   1.5684742  6.2907855 -0.3333299 -3.063327 -1.3415782
# 3  -0.6664055  2.0455375 -1.4416841 -4.701183 -1.7422020
# 4   3.7500055 -0.3915610 -0.6690260 -4.020753  1.7927777
# 12  0.3768509 -2.1897554  1.4380167 -5.327116 -0.4066757
# 15  1.0644951 -1.4646516 -0.9900478 -5.627351 -0.8650174
# 16 -0.3798629  0.2173028  0.4387980 -2.069880 -1.9363920



### Filtering / correlations plot 
nearZeroVar(segData)
correlations <- cor(segData)
correlations[1:4, 1:4]

## find the correlations plot
library(corrplot)
corrplot(correlations, order = "hclust")



# now filter out and find higher correlations. 
highCorr <- findCorrelation(correlations, cutoff =.75)
highCorr
length(highCorr)
filteredSegData <- segData[, -highCorr]


# Assuming 'highCorr' contains the indices of highly correlated variables
filteredCorrelations <- correlations[, highCorr][highCorr, ]

# Plot the filtered correlation matrix
corrplot(filteredCorrelations, order = "hclust")



## Dummy Variables