## OVERVIEW
# total doctors
import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
total = df["name"].nunique()
print(total)

# total cities  
import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
total = df["city"].nunique()
print(total)

# total specializations 
import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
total = df["categoryName"].nunique()
print(total)

##  GEOGRAPHIC ANALYSIS
# total doctors by city 
import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
total = df.groupby("city")["name"].nunique().sort_values(ascending=False)
print(total)

# total doctors by street 
import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
total = df.groupby("street")["name"].nunique().sort_values(ascending=False)
print(total)


## SPECIALIZATION ANALYSIS
# doctors per specializations 
import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
spec = df.groupby("categoryName")["name"].nunique().sort_values(ascending=False)
print(spec)

# rare specialization doctors per specializations total doctors by street total doctors by city total specializations total cities  total doctors
import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
spec = df.groupby("categoryName")["name"].nunique().sort_values(ascending=False)
print(spec.tail(10))


##POPULARITY ANALYSIS
# top reviewed doctors 
import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
top = df[["name", "reviewsCount"]].sort_values(
    by="reviewsCount",
    ascending=False
)

print(top.head(10))



# avg reviews by specialization
import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
avg = (
    df.groupby("categoryName")["reviewsCount"]
      .mean()
      .sort_values(ascending=False)
)

print(avg.head(10))

# avg reviews by city
import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
avg = (
    df.groupby("city")["reviewsCount"]
      .mean()
      .sort_values(ascending=False)
)

print(avg)

## DIGITAL PRESENECE
# doctors with website
import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
total = df[df["website"].notna()]["name"].nunique()

print(total)

# website vs reviews
import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
df["has_website"] = df["website"].notna()
result = df.groupby("has_website")["reviewsCount"].mean()

print(result)


# Top 10 hospitals/locations by doctor count
# import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
hospital = (
    df.groupby("place_id")["name"]
      .nunique()
      .sort_values(ascending=False)
)

print(hospital.head(10))


# Cities with highest specialization diversity
import pandas as pd
df = pd.read_csv("oncologists_nyc.csv")
diversity = (
    df.groupby("city")["categoryName"]
      .nunique()
      .sort_values(ascending=False)
)

print(diversity)