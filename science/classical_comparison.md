# A precisely restricted classical comparison

## Model and inherited mechanism

Let $`H=\sum_{i=1}^d E_i|i\rangle\langle i|`$, with $`E_1<\cdots<E_d`$, and let $`p_1>\cdots>p_d>0`$. The input is the iid distribution $`p^{\otimes n}`$ on product energy-basis strings $`x\in[d]^n`$. The energy of a string is $`E(x)=\sum_jE_{x_j}`$.

The allowed classical operation is a bijection $`f:[d]^n\to[d]^n`$ satisfying

```math
f(\pi x)=\pi f(x)\qquad(\pi\in S_n).
```

We may also allow independent convex mixtures of these bijections. Phases attached to the corresponding quantum basis permutations do not change the energy of this diagonal input. There is no ancillary memory, bath, feedback, postselection, stochastic reset, or nonsymmetric operation hidden by averaging.

The **stabilizer obstruction is prior work**. Yadin, Morris, and Adesso, [“Mixing indistinguishable systems leads to a quantum Gibbs paradox,” Nature Communications 12, 1471 (2021)](https://www.nature.com/articles/s41467-021-21620-7), Supplementary Note 1, Eqs. (25)–(28), analyze the reversible equivariance constraint and explain how quantum superpositions escape the classical obstruction. The full supplement is included in [arXiv:2006.12482v2](https://arxiv.org/pdf/2006.12482v2). Their physical task is bath-assisted mixing of initially separated gases. The calculation below applies that mechanism to closed cyclic work from fixed strictly passive iid fuel.

## Stabilizers force preservation of the count multiset

For any string, write

```math
\operatorname{Stab}(x)=\{\pi\in S_n:\pi x=x\}.
```

Equivariance gives $`\operatorname{Stab}(x)\subseteq\operatorname{Stab}(f(x))`$. Since the inverse of an equivariant bijection is equivariant, the reverse inclusion holds as well. Thus the stabilizers agree as actual subgroups of $`S_n`$, not merely as abstract groups or groups of equal size.

The orbits of this stabilizer on the sites are precisely the sets of positions bearing each occupied symbol, including singleton sets. Therefore $`f(x)`$ can only relabel the occupied symbols injectively. It cannot split an equal-symbol block, since that would remove a stabilizing transposition; it cannot merge distinct blocks, since that would add one. Consequently the unordered multiset of occupation counts is preserved pointwise.

Let $`N_i(x)`$ count the occurrences of symbol $`i`$. If

```math
N_1(x)\geq N_2(x)\geq\cdots\geq N_d(x),
```

the current assignment already minimizes energy among all permitted relabelings: the largest count is assigned to the smallest energy, by the rearrangement inequality. Such a string cannot contribute positive work under any allowed bijection.

## Exact finite-copy optimum by count-multiset sorting

For a type $`N=(N_1,\ldots,N_d)`$ with $`\sum_iN_i=n`$, let $`\mathcal O_N`$ be its orbit of product-basis strings. Its cardinality, per-string probability, and energy are

```math
|\mathcal O_N|=\frac{n!}{\prod_iN_i!},\qquad
w_N=\prod_i p_i^{N_i},\qquad
e_N=\sum_i E_iN_i.
```

An equivariant bijection maps a whole transitive orbit to a whole transitive orbit. Two such type orbits admit an equivariant bijection exactly when their count multisets agree. Necessity follows from conjugacy of their stabilizers, or from the pointwise stabilizer argument above. For sufficiency, choose a bijection from the occupied input symbols to the occupied output symbols that matches their block sizes, and apply this fixed relabeling to every word in the orbit. This map and its inverse commute with every site permutation.

Consequently any permutation of type orbits within one count-multiset class is realizable. The relabelings can be chosen independently on disjoint input orbits and patched into a global bijection. Repeated positive counts merely give several valid matching choices. Zero counts are unoccupied symbols and require no site mapping. No additional compatibility condition arises from either case.

Let $`\gamma`$ be a nonincreasing list of $`d`$ nonnegative counts summing to $`n`$, including zero padding. Let $`\mathcal C_\gamma`$ contain its **distinct** coordinate permutations and write $`t_\gamma=|\mathcal C_\gamma|`$. Define the common orbit size $`m_\gamma=n!/\prod_i\gamma_i!`$. If $`w_{\gamma,k}^{\downarrow}`$ and $`e_{\gamma,k}^{\uparrow}`$ are the probabilities and energies of these types sorted in opposite order, the exact optimum is

```math
\boxed{
W_{n,\mathrm{cl}}^{\mathrm{sym}}
=\sum_\gamma m_\gamma\left[
\sum_{N\in\mathcal C_\gamma}w_Ne_N
-\sum_{k=1}^{t_\gamma}w_{\gamma,k}^{\downarrow}e_{\gamma,k}^{\uparrow}
\right].
}
```

This follows from the rearrangement inequality and the attainability of every type-orbit permutation just proved. Equal probabilities or energies can be ordered arbitrarily. Equal counts must not be included multiple times in $`\mathcal C_\gamma`$. The formula uses per-string probabilities with the common orbit-size factor; using both full orbit probabilities and that factor would double-count multiplicity. Independent mixtures cannot improve this linear objective.

## Exponential upper bound

Set $`\delta=\min_{i<d}(p_i-p_{i+1})>0`$ and $`\Delta E=E_d-E_1`$. For each adjacent pair, write

```math
N_i-N_{i+1}=\sum_{j=1}^nY_j,\qquad
Y_j=\mathbf 1_{X_j=i}-\mathbf 1_{X_j=i+1}\in[-1,1],
\qquad\mathbb E Y_j=p_i-p_{i+1}.
```

Hoeffding's inequality and a union bound give

```math
\Pr\{(N_1,\ldots,N_d)\text{ is not nonincreasing}\}
\leq\sum_{i=1}^{d-1}e^{-n(p_i-p_{i+1})^2/2}
\leq(d-1)e^{-n\delta^2/2}.
```

Every string has an energy decrease at most $`n\Delta E`$. Ordered-count strings have nonpositive energy decrease, so dropping their contributions gives an upper bound valid for each allowed bijection. Maximizing, and using the identity for the lower bound, yields

```math
\boxed{0\leq W_{n,\mathrm{cl}}^{\mathrm{sym}}
\leq n\Delta E\,(d-1)e^{-n\delta^2/2}.}
```

Convex mixtures obey the same bound by linearity. No claim of a matching optimal exponential rate is made.

Together with the [quantum fluctuation-work theorem](model_and_main_theorem.md), this gives a finite quantum residue versus exponentially vanishing work in the specified classical reversible model. The positive quantum constant requires the separate limiting theorem; a two-copy example alone does not imply it.

## Concrete two-copy separation

Take levels $`(0,1,5)`$ and populations $`(0.6,0.25,0.15)`$, using labels $`0,1,2`$ in this example. The symmetric state

```math
|s_{02}\rangle=(|02\rangle+|20\rangle)/\sqrt2
```

has input eigenvalue $`0.6\times0.15=0.09`$ and energy $`5`$, whereas $`|11\rangle`$ has eigenvalue $`0.25^2=0.0625`$ and energy $`2`$. Swapping these two vectors, while acting as the identity elsewhere, commutes with the two-particle exchange and extracts

```math
(0.09-0.0625)(5-2)=0.0825.
```

An equivariant classical bijection cannot exchange the one-element orbit $`\{11\}`$ with the two-element orbit $`\{02,20\}`$. More generally, the diagonal orbits and the off-diagonal orbits are separately already passive for a strictly passive qutrit pair: their probabilities and energies have opposite order. Thus the classical optimum here is zero.

The quantum operation makes use of the symmetric superposition within the orbit. This is the previously identified mechanism; the numerical example and iid exponential estimate instantiate it in the current model.

## Interpretation limits

1. “Classical” means permutations of the **product** energy-basis strings. A Schur basis contains superpositions of such strings, including within degenerate total-energy eigenspaces. Calling every permutation in an arbitrarily chosen energy basis classical would erase the intended distinction.
2. The theorem does not bound arbitrary permutation-covariant stochastic maps. Such a map can use a bath, entropy sink, or averaged addressing operation outside this reversible model.
3. A supplied pure memory that records distinguishability information is a resource. The 2021 supplement explicitly discusses how such additions change the allowed type transformations.
4. The contrast is a difference in extractable mean work within matched algebraic models. It does not establish an efficient quantum circuit, a finite-power advantage, or an advantage over every classical thermodynamic device.
