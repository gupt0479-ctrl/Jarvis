---
type: class
status: archived
created: 2025-10-10
updated: 2025-11-01
area:
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Midterm - 1]]"
  - "[[Final]]"
  - "[[Quiz]]"
tags:
  - "#class"
  - "#Textbook"
  - "#Homework"
  - "#Lecture"
  - "#Jupyter"
  - "#Quiz"
next: "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Week - 5]]"
---
# #Textbook Textbook (Ch - 4) 
## Chapter 4: Clustering
### 4.1 Clustering
Clustering aims to partition a collection of N vectors $(x_1, …, x_N)$ into k groups or clusters. The goal is for vectors within the same cluster to be "close" to each other, measured by the distance between them. Contextual Details:
- In most real applications, the vectors are high-dimensional $(n>2)$, so visual inspection (like a scatter plot) is not possible.  
- Real data often exhibits "messy" clustering, meaning points may lie between clusters, and the ideal number of clusters (k) may not be immediately clear.  
- Vectors typically represent features of objects.
**Applications of Clustering** (Examples):
- Topic Discovery: Clustering documents based on their word histograms (word count vectors) can automatically group them by topic, genre, or author.  
- Patient Clustering: Grouping patients based on their feature vectors (e.g., symptoms, test results) identifies groups of similar patients.  
- Customer Market Segmentation: Clustering customers based on their purchasing history vectors groups them into segments with similar buying habits.  
- Survey Response Clustering: Grouping respondents based on numerical encodings of their answers (such as a Likert scale) identifies groups with similar opinions.  
- Weather Zones: Clustering geographic areas (e.g., counties) based on vectors summarizing annual weather patterns (monthly temperature and rainfall averages) groups them into zones with similar climates.
### 4.2 A clustering objective
This section formalizes how to mathematically judge the quality of a clustering.
1. Specifying the Clustering:
	**Assignment Vector ($c$)**: The clustering is specified by an N-vector $c$, where the i-th entry, $c_i$, is the number (1 to k) of the group that the vector $x_i$ belongs to.  
	**Index Sets ($G_j$)**: The cluster groups themselves are defined by index sets $G_j = \{ i \mid c_i = j \}$, meaning $G_j$ contains the indices of all vectors assigned to group j.
2. Group Representatives (**Centroids**): Each group j has an associated n-vector representative, $z_j$. These representatives do not have to be actual data points. The goal is for $z_{c_i}$ (the representative for $x_i$) to be close to $x_i$.
3. **The Objective Function** ($J_{clust}$): The standard measure of clustering quality is the mean square distance from the vectors to their assigned representatives: $$
     J_{clust} = \frac{1}{N} \sum_{i=1}^{N} \|x_i - z_{c_i}\|^2
     $$ The goal of clustering is to minimize $J_{clust}$. A smaller value means a better clustering.
4. Optimizing Representatives (Fixed Assignment): If the cluster assignments (c) are fixed, the value of the representative $z_j$ that minimizes $J_{clust}$ for that specific group j is simply the average (centroid) of all vectors belonging to group j.
### 4.3 The k-means algorithm
The k-means algorithm is the most common heuristic method used to solve the clustering objective. It uses alternating optimization, leveraging the simple solution for the optimal representative described above. **Algorithm 4.1 Steps**:
The algorithm requires a list of N vectors $(x_1, …, x_N)$ and an initial list of k representative vectors $(z_1, …, z_k)$.
1. **Partition the vectors (Assignment Step)**:  
   For every vector $x_i$, assign it to the group associated with the representative $z_j$ that is its nearest neighbor (the closest one).
2. **Update Representatives (Update Step)**:  
   For each new group j, calculate the new representative $z_j$ by setting it to the mean (average) of all vectors currently assigned to that group.
Details and Mechanics: 
- **Convergence**: Since $J_{clust}$ decreases or remains the same in every step, the algorithm is guaranteed to converge. It stops when the group assignments remain the same in successive iterations.  
- Interpretation of Representatives: The resulting representatives $z_j$ are highly interpretable, as they represent the average characteristics (or archetype) of the data points in that cluster.  
- Computational Cost (**Complexity**): The complexity per iteration is approximately $(3k + 1)Nn$ flops, meaning the computational cost scales linearly with the total number of data points (N), the dimension (n), and the number of clusters (k).
### 4.4 Examples
The k-means algorithm is highly effective at discovering structure in data based solely on distance.
- Image Clustering (MNIST Digits): K-means was applied to $N = 60000$ handwritten digit images (represented as 784-vectors).
	Clustering into $k = 20$ groups successfully produced representatives that were recognizable digits. This demonstrates that the algorithm "discovered" the digits without any prior knowledge of what a digit is or that the vector entries represent image pixels.
- Document Topic Discovery (Wikipedia): K-means was applied to $N = 500$ Wikipedia articles, represented by long word histogram vectors.
	Clustering the documents into $k = 9$ groups resulted in groups with clear, separate themes (e.g., movies, actors, holidays). The success of this clustering shows that the simple measure of document dissimilarity (distance between word count histogram vectors) is effective.
### 4.5 Applications
Clustering provides valuable insight into large data sets and can be used for specific tasks.
- Exploratory Data Analysis: Clustering helps visualize and interpret a large collection of vectors. By examining the group representatives, users can often understand and assign labels or descriptions to the groups.  
- Classification: K-means can be used to build a rudimentary classifier by clustering known data and then assigning a new, unseen vector to the category of its nearest group representative.  
- Imputing Missing Entries: If a vector x has missing entries, k-means can estimate them. The algorithm is first run on complete data. Then, for the incomplete vector x, the nearest representative $z_j$ is found using only the known entries. The missing entries of x are then estimated using the corresponding entries of the nearest representative $z_j$.

---
# #Lecture Lecture
## #Jupyter Jupyter
[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Week - 3|Week - 3]]
## #Quiz Quiz


---
# #Homework Coding HW
2. `heapq.nsmallest(_n_, _iterable_, _key=None_)` [Link to this definition](https://docs.python.org/3/library/heapq.html#heapq.nsmallest) 
	Return a list with the _n_ smallest elements from the dataset defined by _iterable_. _key_, Equivalent to: `sorted(iterable, key=key)[:n]`.
	- **k smallest distances**, i.e., the **closest training samples** to your test image. If k=7 you want the indices of the **7 closest points**. This is the heart of the **k-Nearest Neighbors (kNN)** algorithm. [[#4.3 The k-means algorithm]]
```python
# test vector to play with
test_vec = X_test[22]
# k-value (number of neighbors to find)
k = 7

###################################################################
# insert your code here
#indices = [None for i in range(k)]
indices = sorted(range(N_train), key=lambda i: distances[i])[:k]
# assumes: distances list was filled above, and k is defined

# extract the training labels for the indices of the k-nearest neighbors
labels = y_train[indices]
```
- `range(N_train)`:Creates a list `[0, 1, 2, …, N_train−1]` representing the **indices** of all training images.
- `sorted(..., key=lambda i: distances[i])`This means: “Sort all indices based on their distance values.” So the index with the smallest distance (closest vector) comes first.
- `[:k]`: Takes only the **first k indices**, i.e., the k smallest distances → the nearest neighbors.
- `labels = y_train[indices]`: Looks up the corresponding labels (digits 0–9) for those k nearest images.
4. The frequency count is a simple method to determine a majority vote in a list of votes (in this case predicted labels). Use your frequency count vector to determine which label occurs the maximum number of times. 
```python
# step: pick the label with the largest count (first max wins)
max_count  = counts[0]
prediction = 0
for i in range(1, 10):
    if counts[i] > max_count:
        max_count  = counts[i]
        prediction = i
```
5. Combination of the entire lab - See the lab itself.

---
