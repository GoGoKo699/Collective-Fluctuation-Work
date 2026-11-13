# Convergence to the fluctuation work

The [exact spectral account](schur_tableau_spectrum.md) provides a uniform block work bound and convergence of the input excitation energy. The [passive-rearrangement account](passive_rearrangement.md) identifies the infinite optimal final energy and gives finite permutation approximations. This section proves that the optimized work itself converges and then averages it over Schur sectors.

## Convergence within a deep sector

Write

```math
W_\lambda=\mathcal W(q_\lambda,K_\lambda),\qquad
\mu_\lambda=\mathrm{Tr}(q_\lambda K_\lambda),\qquad
F_\lambda=\min_{U_\lambda}
 \mathrm{Tr}(U_\lambda q_\lambda U_\lambda^\dagger K_\lambda).
```

The subtraction of the block floor does not change work, so $`W_\lambda=\mu_\lambda-F_\lambda`$. For finite-dimensional $`V_\lambda`$, descending population eigenvalues $`a_{\lambda,j}`$ and ascending excitation energies $`e_{\lambda,j}`$ give

```math
F_\lambda=\sum_{j=1}^{\dim V_\lambda}a_{\lambda,j}e_{\lambda,j}.
```

We prove that

```math
g(\lambda)\longrightarrow\infty
\quad\Longrightarrow\quad
W_\lambda\longrightarrow W_\infty.
```

### Upper bound on the limiting work

The block energies form a subset, with multiplicity, of the full fluctuation energies. Hence

```math
e_{\lambda,j}\ge e_j
\qquad(1\le j\le\dim V_\lambda).
```

Fix an integer $`M`$. Choose occupation vectors carrying the first $`M`$ population eigenvalues $`a_1,\ldots,a_M`$ of $`\tau_\infty`$. They form a finite set, and the stabilization lemma places them in $`S_\lambda`$ for all sufficiently large $`g(\lambda)`$. The normalized block eigenvalues then satisfy

```math
a_{\lambda,j}=\frac{a_j}{t_\lambda}
\qquad(1\le j\le M).
```

Ties cause no difficulty: the chosen finite list includes the required number of copies of each eigenvalue, and a subset cannot contain a population larger than its corresponding full-list order statistic. Consequently,

```math
F_\lambda\ge\frac1{t_\lambda}\sum_{j=1}^{M}a_je_j.
```

As $`g(\lambda)\to\infty`$, we have $`t_\lambda\to1`$. Taking the lower limit, and then increasing $`M`$, gives

```math
\liminf F_\lambda\ge F_\infty.
```

The already proved convergence $`\mu_\lambda\to\mu_\infty`$ yields

```math
\limsup W_\lambda\le\mu_\infty-F_\infty=W_\infty.
```

### Lower bound on the limiting work

Fix a finite energy cutoff $`L`$. Its finite sorting permutation $`V_L`$ is supported on $`A_L`$. The stabilization lemma implies $`A_L\subseteq S_\lambda`$ once $`g(\lambda)`$ is sufficiently large. Thus $`V_L`$, restricted to the embedded block and extended by the identity within that block, is an allowed block unitary.

Inside $`S_\lambda`$, each normalized block population equals its full fluctuation population divided by $`t_\lambda`$, and the excitation energies agree exactly. Therefore this operation extracts exactly

```math
\frac{W_L}{t_\lambda}
```

from the normalized block state. In particular,

```math
W_\lambda\ge\frac{W_L}{t_\lambda}.
```

Taking the lower limit gives $`\liminf W_\lambda\ge W_L`$. The cutoff certificate implies $`W_L\to W_\infty`$ as $`L\to\infty`$, so

```math
\liminf W_\lambda\ge W_\infty.
```

Combining the bounds proves block work convergence.

### Uniformity in the minimum row gap

The preceding statement applies to every sequence of partitions with $`g(\lambda)\to\infty`$. Equivalently, for every $`\varepsilon>0`$ there exists $`G\lt \infty`$ such that

```math
g(\lambda)\ge G
\quad\Longrightarrow\quad
|W_\lambda-W_\infty|\lt \varepsilon.
```

If such a $`G`$ did not exist, one could choose a sequence with $`g(\lambda_k)\ge k`$ and error at least $`\varepsilon`$, contradicting the proved sequential convergence. This uniformity is what is needed for averaging; a limit along a single selected family of diagrams would not suffice.

## Concentration of the Schur distribution

Under

```math
P_n(\lambda)=m_\lambda s_\lambda(p),
```

the normalized Young shape converges in probability to the ordered spectrum:

```math
\frac{\lambda}{n}\xrightarrow[n\to\infty]{\Pr}p.
```

This is the spectrum-estimation concentration statement of Keyl–Werner, Eq. (10), with the Schur probabilities identified in their Eq. (17). Their large-deviation theorem is stronger than required here. See the [source locators](theorem_source_locators.md).

Let

```math
\Delta_p=\min_{1\le i\lt d}(p_i-p_{i+1})>0.
```

On the event $`\|\lambda/n-p\|_\infty\lt \Delta_p/4`$,

```math
\lambda_i-\lambda_{i+1}
\ge n\left[(p_i-p_{i+1})-\frac{\Delta_p}{2}\right]
\ge\frac{n\Delta_p}{2},
```

for every adjacent pair. Therefore $`g(\lambda)\to\infty`$ in probability under $`P_n`$.

## Averaging the optimized work

The Schur reduction gives

```math
W_n^{\rm sym}=\mathbb E_{P_n}[W_\lambda],
\qquad
0\le W_\lambda\le C(p,E).
```

Also $`0\le W_\infty\le\mu_\infty\le C(p,E)`$. Given $`\varepsilon>0`$, choose $`G`$ from uniform deep-sector convergence. Split the expectation according to whether $`g(\lambda)\ge G`$:

```math
|W_n^{\rm sym}-W_\infty|
\le\varepsilon
+C(p,E)\Pr_{P_n}\{g(\lambda)\lt G\}.
```

The probability tends to zero. Since $`\varepsilon`$ is arbitrary,

```math
\lim_{n\to\infty}W_n^{\rm sym}=W_\infty.
```

The uniform excitation bound is essential here: it prevents rare Young sectors from contributing macroscopic work. The proof does not interchange an unbounded energy observable with trace-norm convergence, and it does not assume convergence of optimal finite-dimensional unitaries.
