# Passive rearrangement and finite energy cutoffs

This section supplies the infinite-dimensional optimization used in the [main theorem](model_and_main_theorem.md). Its role is to justify optimizing over all unitaries after taking the fluctuation limit, and to provide a rigorous finite approximation.

## The sorted-spectrum minimum

Consider the fluctuation pair $`(\tau_\infty,K_\infty)`$. Every mode frequency is positive, so every finite-energy subspace is finite-dimensional:

```math
\#\{\boldsymbol m:k_{\boldsymbol m}\le L\}\lt \infty
\qquad\text{for every finite }L.
```

List the energies with multiplicity as

```math
0=e_1\le e_2\le\cdots,\qquad e_j\longrightarrow\infty,
```

and the eigenvalues of $`\tau_\infty`$ with multiplicity as

```math
a_1\ge a_2\ge\cdots>0,\qquad \sum_{j=1}^{\infty}a_j=1.
```

Such a descending enumeration exists: only finitely many eigenvalues exceed any fixed positive threshold. Degeneracies can be ordered arbitrarily.

Define the candidate passive energy

```math
F_\infty=\sum_{j=1}^{\infty}a_je_j.
```

**Lemma.** This series is finite, and

```math
\inf_V\mathrm{Tr}(V\tau_\infty V^\dagger K_\infty)
=F_\infty.
```

The infimum is attained by a unitary that matches descending populations to ascending energies.

**Proof.** For any rank-$`D`$ projection $`Q`$ and any unitary $`V`$,

```math
\mathrm{Tr}(QV\tau_\infty V^\dagger)
\le\sum_{j=1}^{D}a_j.
```

Indeed, in a population eigenbasis the left side is $`\sum_j a_jc_j`$, where $`0\le c_j\le1`$ and $`\sum_jc_j=D`$. Moving the available coefficient weight to the first $`D`$ positions maximizes this expression.

Put $`D(t)=\mathrm{rank}1_{\{K_\infty\le t\}}`$. For any density operator $`\sigma`$, spectral calculus and Tonelli's theorem give, with infinite values allowed,

```math
\mathrm{Tr}(\sigma K_\infty)
=\int_0^\infty
 \left[1-\mathrm{Tr}\!\left(\sigma\,1_{\{K_\infty\le t\}}\right)\right]dt.
```

The projection inequality therefore implies

```math
\mathrm{Tr}(V\tau_\infty V^\dagger K_\infty)
\ge\int_0^\infty
 \left[1-\sum_{j=1}^{D(t)}a_j\right]dt
=\sum_{j=1}^{\infty}a_je_j.
```

Applying this inequality to the identity unitary shows $`F_\infty\le\mu_\infty\lt \infty`$. Finally, map a complete population eigenbasis, in descending order, to a complete energy eigenbasis, in ascending order. The resulting basis permutation extends to a unitary and has final energy $`F_\infty`$. ∎

Thus

```math
W_\infty=\mu_\infty-F_\infty
```

is the full unitary ergotropy. The argument does not rely on continuity of ergotropy under trace norm.

## A certified finite-cutoff approximation

For $`L\ge0`$, use the complete energy cutoff

```math
A_L=\{\boldsymbol m:k_{\boldsymbol m}\le L\},\qquad
D_L=|A_L|,\qquad
T_L=\sum_{\boldsymbol m\notin A_L}a_{\boldsymbol m}k_{\boldsymbol m}.
```

Here $`a_{\boldsymbol m}=\langle\boldsymbol m|\tau_\infty|\boldsymbol m\rangle`$ denotes an occupation-basis population; $`a_j`$ above denotes the descending ordering of the same populations.

Sort only the populations in $`A_L`$ onto the energies in $`A_L`$, and act as the identity outside this subspace. Let $`V_L`$ be that finite permutation. Define its work on the full, normalized fluctuation state by

```math
W_L
=\mathrm{Tr}\!\left[
 K_\infty(\tau_\infty-V_L\tau_\infty V_L^\dagger)\right].
```

No renormalization of the truncated state enters this definition. This distinction is necessary for the certificate and for its later use in finite Schur blocks.

Let $`b_1\ge\cdots\ge b_{D_L}`$ be the unnormalized populations drawn from $`A_L`$. Since this list is a subset of the full population list,

```math
b_j\le a_j\qquad(1\le j\le D_L).
```

Because the cutoff includes every state below its threshold, its energies are exactly the first $`D_L`$ full energies, including every degeneracy at the threshold. The final energy of $`V_L`$ is consequently

```math
T_L+\sum_{j=1}^{D_L}b_je_j.
```

Optimality of the global passive rearrangement gives the lower inequality below; $`b_j\le a_j`$ gives the upper one:

```math
\boxed{0\le W_\infty-W_L
=T_L+\sum_{j=1}^{D_L}b_je_j-F_\infty
\le T_L.}
```

Since $`T_L\to0`$, finite permutations achieve work arbitrarily close to $`W_\infty`$. The certificate controls all omitted states, including any favorable population inversions connecting the retained and omitted parts.

This proof requires a complete energy cutoff. An arbitrary occupation truncation can still give a valid lower bound on work, but the displayed error certificate does not follow merely from its omitted probability mass.
