$$
\hat{y}(x) = w_0 + \sum_{i=1}^{n}w_i x_i + \sum_{i=1}^{n} \sum_{j=i+1}^{n} \langle \textbf v_i, \textbf v_j \rangle x_i x_j
$$

$$
\sum_{i=1}^{n} \sum_{j=i+1}^{n} \langle \textbf v_i, \textbf v_j \rangle x_i x_j = 
\frac{1}{2} \sum_{f=1}^{k} \Big( \big(\sum_{i=1}^{n} v_f^{(i)} x_i \big)^2 - \sum_{i=1}^{n}v_f^{(i) 2} x_i^2 \Big) = 
\frac{1}{2} \sum_{f=1}^{k} \Big( S_{1,f}^2 - S_{2,f} \Big) =
\frac{1}{2} \Big( S_{1}^2 - S_{2} \Big)
$$

$$
X = \begin{bmatrix}
x_1^{(1)} & \dots & x_n^{(1)}\\
 \vdots \ & \ddots \ & \vdots \\ 
x_1^{(M)} & \dots & x_n^{(M)} \\
\end{bmatrix}
$$

$$
V = \begin{bmatrix}
v_1^{(1)} & \dots & v_k^{(1)}\\
 \vdots \ & \ddots \ & \vdots \\ 
v_1^{(n)} & \dots & v_k^{(n)} \\
\end{bmatrix}
$$

$$
XV = \begin{bmatrix}
\sum_{i=1}^{n} v_f^{(1)} x_i^{(1)}  & \dots &  \sum_{i=1}^{n} v_f^{(k)} x_i\\
 \vdots \ & \ddots \ & \vdots \\ 
\sum_{i=1}^{n} v_f^{(1)} x_i^{(M)} & \dots & \sum_{i=1}^{n} v_f^{(k)} x_i^{(M)} \\
\end{bmatrix} = 
\begin{bmatrix}
S_{1,1}^{(1)}  & \dots &  S_{1,k}^{(1)}\\
 \vdots \ & \ddots \ & \vdots \\ 
S_{1,1}^{(M)}  & \dots & S_{1,k}^{(M)} \\
\end{bmatrix}
$$

$$
\hat{\textbf{y}}(X) = \frac{1}{2} ( square(XV) - (square(X) \times square(V) )).sum(col)
$$

$$
\frac{\partial}{\partial \theta} y(\mathbf{x}) = \left \{ \begin{array}{ll} 1,         & \text{if}\; \theta\; \text{is}\; w_0  \\ x_i     & \text{if}\; \theta\; \text{is}\; w_i \; \\ x_i \sum_{j=1}^{n} v_{j,f} x_j - v_{i,f} x_i^2, & \text{if}\; \theta\; \text{is}\; v_{i,f} \end{array} \right.
$$

