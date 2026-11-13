# Exact Schur and tableau spectrum

Throughout, use the assumptions and notation of the [main theorem](model_and_main_theorem.md). This section gives an exact finite-dimensional description. The tableau basis and its density eigenvalues are inherited from Kahn–Guţă, Theorem 5.2 and Eq. (5.9); see the [source locators](theorem_source_locators.md).

## Schur reduction of the optimization

Schur–Weyl duality gives a unitary decomposition

```math
(\mathbb C^d)^{\otimes n}
=\bigoplus_{\substack{\lambda\vdash n\\ \ell(\lambda)\le d}}
V_\lambda\otimes M_\lambda.
```

Here $`V_\lambda`$ carries the irreducible polynomial representation $`\pi_\lambda`$ of $`\mathrm{GL}(d)`$, and $`M_\lambda`$ carries an irreducible representation of $`S_n`$. Pad each partition with zeros to obtain $`\lambda_1\ge\cdots\ge\lambda_d\ge0`$, and put $`m_\lambda=\dim M_\lambda`$.

In this decomposition,

```math
\rho^{\otimes n}
=\bigoplus_\lambda\pi_\lambda(\rho)\otimes I_{M_\lambda},
\qquad
H_n=\bigoplus_\lambda H_\lambda\otimes I_{M_\lambda},
```

where $`H_\lambda`$ is the generator determined by
$`\pi_\lambda(e^{-itH})=e^{-itH_\lambda}`$.
The permutation commutant is exactly

```math
U=\bigoplus_\lambda U_\lambda\otimes I_{M_\lambda},
\qquad U_\lambda\in\mathsf U(V_\lambda).
```

Define

```math
s_\lambda(p)=\mathrm{Tr}\pi_\lambda(\rho),\qquad
q_\lambda=\frac{\pi_\lambda(\rho)}{s_\lambda(p)},\qquad
P_n(\lambda)=m_\lambda s_\lambda(p).
```

The numbers $`P_n(\lambda)`$ form a probability distribution. Because every block unitary is independently available,

```math
W_n^{\rm sym}
=\sum_\lambda P_n(\lambda)\,
  \mathcal W(q_\lambda,H_\lambda).
```

This equality optimizes over every unitary in the commutant, including entangling collective controls.

## Tableau occupation coordinates

Semistandard Young tableaux of shape $`\lambda`$ with entries in $`\{1,\ldots,d\}`$ index a weight basis of $`V_\lambda`$. Their rows are weakly increasing and their columns strictly increasing. Every entry in row $`i`$ is at least $`i`$.

For a tableau $`T`$, let

```math
m_{ij}(T)
=\#\{\text{entries equal to }j\text{ in row }i\},
\qquad 1\le i\lt j\le d.
```

The remaining $`\lambda_i-\sum_{j>i}m_{ij}`$ entries in row $`i`$ equal $`i`$. The occupation vector $`\boldsymbol m=(m_{ij})`$ uniquely determines the tableau, since its rows are sorted. Let $`S_\lambda\subset\mathbb N_0^{\mathcal R}`$ be the finite set of occupation vectors that give valid tableaux.

If $`w_i`$ is the total number of entries equal to $`i`$, then

```math
w_i
=\lambda_i-\sum_{j>i}m_{ij}
+\sum_{h\lt i}m_{hi}.
```

Consequently the joint state-energy eigenvalues are

```math
\prod_i p_i^{w_i}
=p^\lambda\prod_{i\lt j}r_{ij}^{m_{ij}},
\qquad
p^\lambda:=\prod_i p_i^{\lambda_i},
```

and

```math
\sum_i E_iw_i
=e_\lambda+\sum_{i\lt j}\omega_{ij}m_{ij},
\qquad
e_\lambda:=\sum_iE_i\lambda_i.
```

The vacuum occupation is valid: fill row $`i`$ entirely with $`i`$. Thus $`e_\lambda`$ is the smallest block energy. Set

```math
K_\lambda=H_\lambda-e_\lambda I\ge0.
```

### Why a nonorthogonal tableau basis is sufficient

The standard tableau basis is generally nonorthogonal. It must not be treated as an orthonormal basis for arbitrary operator identities. Here only the joint spectrum of diagonal $`\rho`$ and $`H`$ is needed.

Each tableau vector is a weight vector for the diagonal unitary torus. Distinct torus weights are orthogonal because this torus acts unitarily. Within one weight space, both $`\pi_\lambda(\rho)`$ and $`H_\lambda`$ act as scalars, with the eigenvalues displayed above. Choose an orthonormal basis within each such weight space and label it by the tableaux of that weight. This preserves both operators and their multiplicities.

Mapping these orthonormal vectors to the corresponding occupation vectors defines an isometry

```math
J_\lambda:V_\lambda\longrightarrow\mathcal F,
\qquad
\mathrm{ran}J_\lambda
=\mathrm{span}\{|\boldsymbol m\rangle:\boldsymbol m\in S_\lambda\}.
```

This is a joint spectral identification. It makes no assertion that finite-dimensional raising and lowering operators become exact oscillator operators.

## Exact restricted geometric state

Let $`\Pi_\lambda=J_\lambda J_\lambda^\dagger`$. Define

```math
Z_\lambda
=\sum_{\boldsymbol m\in S_\lambda}
 \prod_{i\lt j}r_{ij}^{m_{ij}}
=\frac{s_\lambda(p)}{p^\lambda},
\qquad
t_\lambda=\frac{Z_\lambda}{Z_\infty}.
```

The spectral formulas give the exact identities

```math
J_\lambda q_\lambda J_\lambda^\dagger
=\frac{\Pi_\lambda\tau_\infty\Pi_\lambda}{t_\lambda},
\qquad
J_\lambda K_\lambda J_\lambda^\dagger
=\Pi_\lambda K_\infty\Pi_\lambda.
```

The second equality is understood as an operator on the embedded finite-dimensional range, or as its extension by zero on the orthogonal complement. Since $`\boldsymbol0\in S_\lambda`$,

```math
1\le Z_\lambda\le Z_\infty,
\qquad
\frac1{Z_\infty}\le t_\lambda\le1.
```

## Elementary stabilization of every finite occupation set

Put

```math
g(\lambda)=\min_{1\le i\lt d}(\lambda_i-\lambda_{i+1}),
\qquad
|\boldsymbol m|_1=\sum_{i\lt j}m_{ij}.
```

**Lemma.** Every occupation vector satisfying $`|\boldsymbol m|_1\le g(\lambda)`$ belongs to $`S_\lambda`$.

**Proof.** Write $`M_i=\sum_{j>i}m_{ij}`$. The assumed bound implies

```math
\lambda_i-M_i\ge\lambda_{i+1}\qquad(i\lt d).
```

Construct each row by placing its $`\lambda_i-M_i`$ copies of $`i`$ first, followed by the prescribed larger entries in increasing order. All row lengths are nonnegative and correct. In every column that continues into row $`i+1`$, the entry in row $`i`$ is $`i`$, because the first $`\lambda_{i+1}`$ positions in that row are all $`i`$. The entry below is at least $`i+1`$. Hence every column is strictly increasing. The final row is filled with $`d`$. The resulting tableau is semistandard. ∎

It follows that every finite occupation set lies in $`S_\lambda`$ once $`g(\lambda)`$ is sufficiently large. In particular, along any sequence with $`g(\lambda)\to\infty`$, the indicators $`1_{S_\lambda}(\boldsymbol m)`$ converge pointwise to one. No nesting of the sets $`S_\lambda`$ is required.

## Uniform excitation and energy tails

Let

```math
a_{\boldsymbol m}
=\langle\boldsymbol m|\tau_\infty|\boldsymbol m\rangle,
\qquad
k_{\boldsymbol m}
=\sum_{i\lt j}\omega_{ij}m_{ij}.
```

For any nonnegative function $`f`$ of the excitation energy,

```math
\mathrm{Tr}\!\left[q_\lambda f(K_\lambda)\right]
=\frac1{t_\lambda}
  \sum_{\boldsymbol m\in S_\lambda}a_{\boldsymbol m}f(k_{\boldsymbol m})
\le Z_\infty\mathrm{Tr}\!\left[\tau_\infty f(K_\infty)\right].
```

Apply this first to $`f(k)=k`$ and then to $`f(k)=k\,1_{\{k>L\}}`$:

```math
\mathrm{Tr}(q_\lambda K_\lambda)
\le Z_\infty\mu_\infty=C(p,E),
```

```math
\mathrm{Tr}\!\left[q_\lambda K_\lambda
      1_{\{K_\lambda>L\}}\right]
\le Z_\infty
   \mathrm{Tr}\!\left[\tau_\infty K_\infty
      1_{\{K_\infty>L\}}\right].
```

The right side tends to zero as $`L\to\infty`$. Therefore the block excitation energies are uniformly integrable. Ergotropy is nonnegative and cannot exceed the initial excitation above the block ground, giving

```math
0\le\mathcal W(q_\lambda,H_\lambda)
=\mathcal W(q_\lambda,K_\lambda)\le C(p,E).
```

Averaging proves the uniform bound in the main theorem. The geometric tails and their use in the oscillator approximation are already present in Kahn–Guţă, Section 7.6; the estimate here records explicitly the energy observable needed by the work optimization.

## Deep-sector state and energy convergence

If $`g(\lambda)\to\infty`$, finite-set stabilization and summability yield

```math
t_\lambda\longrightarrow1,\qquad
\left\|J_\lambda q_\lambda J_\lambda^\dagger-\tau_\infty\right\|_1
=2(1-t_\lambda)\longrightarrow0.
```

The exact norm identity follows by summing the diagonal differences separately inside and outside $`S_\lambda`$. Because $`\sum_{\boldsymbol m}a_{\boldsymbol m}k_{\boldsymbol m}\lt \infty`$, dominated convergence also gives

```math
\mathrm{Tr}(q_\lambda K_\lambda)
=\frac1{t_\lambda}\sum_{\boldsymbol m\in S_\lambda}
  a_{\boldsymbol m}k_{\boldsymbol m}
\longrightarrow\mu_\infty.
```

Trace-norm convergence alone would not justify this last step for an unbounded Hamiltonian. The exact spectrum and energy domination do.
