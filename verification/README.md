# Exact numerical verification of collective fluctuation work

This directory verifies the qutrit example

```math
\rho=\mathrm{diag}(3/5,1/4,3/20),\qquad H=\mathrm{diag}(0,1,5).
```

The source is strictly passive and non-Gibbs. Energies and work are measured in units of the first excitation gap. A collective unitary may be entangling, but must commute with every permutation of the copies. All optimizations in this directory are for closed, cyclic unitary operations. No bath, auxiliary entropy sink, measurement, or discarded subsystem is included.

The limiting root-mode ergotropy is certified by the exact interval

```math
\boxed{2.894208160219019088\ \le W_\infty\le\ 2.894208160219019768.}
```

The [analytical qutrit account](../science/qutrit_example.md) connects this calculation to the main theorem; the [passive-rearrangement proof](../science/passive_rearrangement.md) supplies the general approximation lemma.

Every endpoint is rounded outward from an exact rational number. The certificate controls the possible **work error**, including the effect of omitted states on passive rearrangement. It does not infer an energy error from a small trace tail.

## Reproduce and verify the results

The repository includes:

| Artifact | Repository path |
|---|---|
| Exact calculation | [certify_collective_work.py](certify_collective_work.py) |
| Reproduction and reference comparison | [run_all.py](run_all.py) |
| Pinned numerical and plotting dependencies | [requirements.txt](requirements.txt) |
| Exact fractions, certified intervals, and check outcomes | [certified_results.json](results/certified_results.json) |
| Scientific figure, editable vector version | [collective_work_finite_size.svg](../assets/collective_work_finite_size.svg) |

From the repository root, install the dependencies and verify the checked-in scientific results:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The verification wrapper executes the canonical calculation with `--skip-plot` in a temporary directory. It compares every scientific JSON field with the checked-in reference, excluding only the top-level `reproducibility` metadata. It also checks local file targets of Markdown links throughout the repository. A failed calculation, changed scientific field, or missing local target produces a nonzero exit status. The wrapper leaves the checked-in results unchanged.

To deliberately regenerate the results and all three figure formats:

```bash
python verification/certify_collective_work.py \
  --output-dir verification/results --figure-dir assets
```

To reproduce the exact certificate, all finite-size values, the independent projector checks, and the Gibbs check without generating figures:

```bash
python verification/certify_collective_work.py \
  --output-dir verification/results --skip-plot
```

To regenerate only the figure from the saved exact results:

```bash
python verification/certify_collective_work.py \
  --plot-from verification/results/certified_results.json \
  --figure-dir assets
```

The checked-in figure is SVG. Figure regeneration also creates PDF and PNG versions in `assets/`.

The recorded environment was Python **3.12.14**, NumPy **2.3.5**, and Matplotlib **3.10.8**, on Linux x86-64. Exact enumeration, sorting, tail control, and directed decimal conversion use Python integers and `fractions.Fraction`. NumPy is used only for small integer matrix checks at `n <= 4`; Matplotlib is used only for the figure. The saved run took about 1.14 seconds before plotting in the recorded environment; this is an observation, not a performance guarantee. Runtime and platform metadata can differ between reruns. No external input data, stochastic sampling, optimization solver, or SciPy dependency is required.

The default copy numbers are `1 2 3 4 6 10 20 30 40 60`; the limiting-state energy cutoffs are 80 and 320. `--sizes` and `--root-cutoff` override these choices. The script requires its largest root-cutoff certificate to have width less than `1e-12`; an insufficiently large cutoff deliberately fails that assertion. Run without Python's `-O` flag so the mathematical consistency assertions remain enabled.

## Why the limiting interval is rigorous

### Complete energy cutoff

Let a diagonal state $`\tau`$ have finite mean energy under a nonnegative Hamiltonian $`K`$ with discrete spectrum and finite degeneracies. For the complete spectral subspace

```math
A_R=\{K\le R\},
```

sort the **original, unnormalized** probabilities inside $`A_R`$ onto its increasing energy list. Extend that permutation by the identity outside $`A_R`$. Let $`W_R`$ denote the work of this operation on the full state. Then

```math
0\le\mathcal W(\tau,K)-W_R
\le T_R,\qquad
T_R=\mathrm{Tr}\bigl[\tau K\mathbf 1_{K>R}\bigr].
```

To see the upper bound, write the full eigenvalues in decreasing order as $`a_1\ge a_2\ge\cdots`$, and the eigenvalues retained in the cutoff as $`b_1\ge\cdots\ge b_D`$. The order-statistic inequality gives $`b_i\le a_i`$. Because the cutoff contains every state up to its energy boundary, its energies are exactly the first $`D`$ entries $`e_1\le\cdots\le e_D`$ of the full energy list, including degeneracies. Consequently,

```math
F_R=\sum_{i=1}^D b_i e_i
\le\sum_{i=1}^D a_i e_i\le F_\infty,
```

where $`F_\infty`$ is the fully passive energy. Writing the initial energies as $`E_R`$ and $`E_\infty`$,

```math
\mathcal W(\tau,K)-W_R
=(E_\infty-E_R)-(F_\infty-F_R)\le T_R.
```

The lower bound follows because the finite permutation is an allowed unitary. No normalization of the retained state is performed.

This argument specifically uses a complete energy cutoff. An occupation cube can omit low-energy states while retaining higher-energy states, so its restricted energy list is not the beginning of the full list. A small omitted probability for such a cube does not by itself certify the passive energy or work to the same accuracy.

### Exact qutrit reduction

The limiting state has independent root occupations $`(a,b,c)=(n_{12},n_{13},n_{23})`$, ratios

```math
(r_{12},r_{13},r_{23})=(5/12,1/4,3/5),
```

and gaps $`(1,5,4)`$. Its probability per root Fock state and energy are

```math
q(a,b,c)=\frac7{40}(5/12)^a(1/4)^b(3/5)^c,
\qquad K(a,b,c)=a+5b+4c.
```

Set $`u=a+b`$ and $`v=b+c`$. Because $`r_{13}=r_{12}r_{23}`$, the spectrum reduces to

```math
q(u,v)=\frac7{40}(5/12)^u(3/5)^v,
\qquad K(u,v)=u+4v,
\qquad m(u,v)=\min(u,v)+1.
```

The multiplicity follows by choosing $`b`$ from 0 through $`\min(u,v)`$. At energy cutoff $`R`$, all retained probabilities have the common denominator

```math
D_R=40\,12^R\,5^{\lfloor R/4\rfloor},
```

and the exact integer numerator

```math
w_R(u,v)=7\,12^{R-u}\,5^{\lfloor R/4\rfloor+u-v}\,3^v,
\quad u+4v\le R.
```

The script sorts these integer numerators, with multiplicity, against integer energies. It never sorts rounded logarithms or floating-point probabilities. The full initial root energy is

```math
E_\infty=
\frac{5}{7}+5\frac{1}{3}+4\frac{3}{2}
=\frac{176}{21}.
```

Thus $`T_R=176/21-E_R`$ is also an exact rational number.

| Energy cutoff | Retained basis dimension | Distinct $`(u,v)`$ labels | Attainable work $`W_R`$, rounded | Certified omitted energy, rounded |
|---:|---:|---:|---:|---:|
| 80 | 5,201 | 861 | 2.892266544720082 | 0.003735050287593 |
| 320 | 287,361 | 13,041 | 2.894208160219019 | $`6.785195183034335\times10^{-16}`$ |

The table's short decimal displays are for readability; exact fractions and directed endpoints are stored in the JSON. At $`R=320`$, the omitted probability is about $`2.06656\times10^{-18}`$. The certified work interval is based on the omitted **energy**, not that probability.

## Exact finite-ensemble optimization

For each three-row Young diagram $`\lambda=(a,b,c)\vdash n`$, the script enumerates the Gelfand–Tsetlin patterns

```math
b\le u\le a,\quad c\le v\le b,\quad v\le z\le u.
```

Their weights are $`\mu=(z,u+v-z,n-u-v)`$. Each weight has exact population numerator $`12^{\mu_1}5^{\mu_2}3^{\mu_3}`$, common denominator $`20^n`$, and energy $`\mu_2+5\mu_3`$. Degenerate weights are retained with their exact multiplicities. Population-energy sorting is performed separately in each irrep, then multiplied by the Schur multiplicity

```math
m_\lambda=
\frac{n!(a-b+1)(a-c+2)(b-c+1)}{(a+2)!(b+1)!c!}.
```

The irrep dimension is $`(a-b+1)(a-c+2)(b-c+1)/2`$. The code verifies exactly that the total trace is one, that $`\sum_\lambda m_\lambda\dim V_\lambda=3^n`$, and that the initial energy is $`n`$. No normalized-sector probability approximation is used.

The following numbers are rounded displays of exact rational outputs.

| Copies $`n`$ | Permutation-invariant quantum work | Equivariant basis-permutation work | Unrestricted quantum work |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 2 | 0.082500000000 | 0 | 0.082500000000 |
| 3 | 0.236250000000 | 0.185625000000 | 0.236250000000 |
| 4 | 0.343625000000 | 0.184200000000 | 0.351187500000 |
| 6 | 0.551745875000 | 0.227901093750 | 0.602128843750 |
| 10 | 0.912633119243 | 0.307554543422 | 1.107609927950 |
| 20 | 1.568210375767 | 0.354201258961 | 2.334683845207 |
| 30 | 1.977343381661 | 0.280557305930 | 3.554375701163 |
| 40 | 2.236961562299 | 0.202076432155 | 4.769170652028 |
| 60 | 2.523923873461 | 0.085145102519 | 7.195051588108 |

The calculations are consistent with the proven asymptotic limits, but the table is not a proof of convergence. In particular, at $`n=60`$ the collective quantum work remains about 0.370284 below its limiting value. No convergence exponent or finite-size rate has been fitted.

### Why the classical sorting is exact

The [classical comparison](../science/classical_comparison.md) gives the general statement and attribution. The following argument explains the finite calculation.

Here the classical comparator consists specifically of **bijective permutations of the product energy basis that commute with every permutation of the sites**. It does not cover arbitrary stochastic thermodynamic operations.

Let $`x`$ be a word of length $`n`$ over the three energy labels, and let $`F`$ be such an equivariant bijection. Equivariance gives $`\mathrm{Stab}(x)\subseteq\mathrm{Stab}(F(x))`$, and applying the inverse bijection gives equality. The stabilizer is the product of symmetric groups on the equal-letter position blocks. Its coordinate orbits determine those blocks, including singleton blocks. Therefore $`F(x)`$ has the same multiset of symbol counts as $`x`$.

Conversely, two type orbits whose count triples differ only by a relabeling of the symbols are equivariantly isomorphic: use that symbol relabeling on every word of the orbit. Any permutation of the type orbits in a fixed count-multiset block can be implemented by choosing such isomorphisms separately on the source orbits. All orbits in the block have the same size $`n!/(a!b!c!)`$. Their populations and energies are constant on each orbit. Hence sorting orbit populations against orbit energies within each count-multiset block is attainable and optimal. The equal orbit sizes ensure that the grouped sorting is an assignment of entire orbits, with no fractional splitting. The script checks this equal-size condition explicitly.

The unrestricted benchmark is obtained by the same exact type grouping but a single global population-energy sort. It includes every product-basis state with its multinomial multiplicity without expanding the full $`3^n`$-dimensional Hilbert space.

## Independent checks actually performed

### Direct tensor-space decomposition for $`n=1,2,3,4`$

The code constructs all site-permutation matrices on dimensions 3, 9, 27, and 81, and forms the scaled central projectors
```math
Q_\lambda=n!P_\lambda
=m_\lambda\sum_{\pi\in S_n}\chi_\lambda(\pi)U_\pi.
```
It verifies the exact integer identities $`Q_\lambda^2=n!Q_\lambda`$, self-adjointness, mutual orthogonality, and $`\sum_\lambda Q_\lambda=n!I`$. Traces on every occupation subspace agree with the independently enumerated Gelfand–Tsetlin weight multiplicities. Direct sector sorting reproduces the finite-size work. These checks use fixed character tables of $`S_n`$ for $`n\le4`$; the relevant integer matrix entries and products are far below the `int64` limit.

### Exactly Gibbs input

For the same energies, $`p=(32,16,1)/49`$ is Gibbs at $`\beta=\log2`$. Finite-copy work is exactly zero at $`n=2,4,10`$, and the root-state energy-cutoff work is exactly zero at $`R=40`$. The test uses rational probabilities ordered by the exact energy, not a numerical tolerance around zero.

### Normalization, dimension and energy at each enumerated size

These are checked with exact arithmetic, including $`n=60`$, whose full Hilbert-space dimension is $`3^{60}`$. The Schur calculation enumerates 1,159,400 irrep basis states at that size, with their multiplicities handled symbolically.

### Certified limiting-state truncation

The two energy cutoffs are independently sorted, and the exact omitted first moment is recorded. The largest cutoff has work-error bound smaller than $`10^{-12}`$, as an explicit assertion. The resulting error here is much smaller, approximately $`6.79\times10^{-16}`$.

## Explicit extraction operations

### Two copies

With single-qutrit energy labels 0, 1, 2, swap

```math
|11\rangle\quad\longleftrightarrow\quad
\frac{|02\rangle+|20\rangle}{\sqrt2},
```

and act as the identity on the orthogonal complement. Both vectors are symmetric under exchange of the two copies, so the unitary commutes with the copy permutation. Their energies are 2 and 5, and their populations are $`(1/4)^2`$ and $`(3/5)(3/20)`$. The extracted work is

```math
(5-2)\left(\frac35\frac3{20}-\frac1{16}\right)
=\frac{33}{400}=0.0825,
```

which equals the exact two-copy optimum.

### Root-mode swap and finite approximations

Swap the entire 12 and 23 fluctuation modes, leaving the 13 mode untouched. The mean occupations of the two swapped modes are $`5/7`$ and $`3/2`$, with gaps 1 and 4. This operation extracts

```math
W_{\mathrm{swap}}=(4-1)\left(\frac32-\frac57\right)
=\frac{33}{14}=2.357142857\ldots,
```

about 81.44% of the limiting optimum. This is an explicit benchmark; no claim of optimality within a restricted class of controls is needed.

For a finite permutation, restrict all three root occupations to the cube $`0\le a,b,c\le M`$, swap $`a`$ and $`c`$ inside that invariant cube, and act as the identity outside it. The work values for $`M=1,3,8,20`$ are recorded exactly in the JSON and approach $`33/14`$. Alternatively, the complete energy-cutoff sorting at $`R=80`$ is an explicit finite permutation on 5,201 states, extracting $`2.892266544720081\ldots`$, over 99.9% of the certified limit. The theoretical embedding of finite root permutations in sufficiently deep Schur sectors provides asymptotic collective-unitary extraction. These examples establish attainability; they do not provide an efficient laboratory compilation of the required unitary.

## Figure caption

**Finite-copy work from a passive qutrit source.** Exact optimization for $`p=(0.60,0.25,0.15)`$ and $`E=(0,1,5)`$, comparing unrestricted unitaries, permutation-invariant quantum unitaries, and equivariant permutations of the product energy basis. Panel (a) shows total work; panel (b) shows work per copy. Markers are the exactly enumerated copy numbers. **Straight line segments only guide the eye between those points.** The dashed line is the certified limiting quantum work $`W_\infty\simeq2.894208`$; its rigorous interval is much narrower than the line width. No curve fit or finite-size convergence-rate inference is shown. The PNG, PDF, and SVG share the same data and layout.
