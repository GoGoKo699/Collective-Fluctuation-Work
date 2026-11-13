# The science of collective fluctuation work

A passive source stores energy that a single cyclic unitary cannot extract. For a non-Gibbs source, unrestricted control across many copies can activate an extensive work supply. This project determines the work accessible when every operation must commute with the permutations of one fixed ensemble.

The restriction conserves the Schur-sector label. Within a typical sector, the source lies only a finite energy above its lowest state. Its remaining spectrum approaches a fixed collection of geometric oscillator modes. The central theorem identifies the full optimized work of those fluctuations, including the optimization and the unbounded-energy tails.

## Proof route

| Question | Authoritative account |
|---|---|
| What is the exact task, allowed unitary class and result? | [Model and main theorem](model_and_main_theorem.md) |
| How do tableaux give the exact finite-sector state and energy spectra? | [Schur sectors and the tableau spectrum](schur_tableau_spectrum.md) |
| Why does sorting an infinite spectrum define attainable work, and how is its error bounded? | [Passive rearrangement](passive_rearrangement.md) |
| How do the sector bound and typical-sector limit give the many-copy theorem? | [Fluctuation-work limit](fluctuation_limit.md) |
| When is the limit positive, and what do fixed control classes change? | [Control consequences](consequences.md) |
| What can symmetry-compatible reversible classical operations extract? | [Classical comparison](classical_comparison.md) |
| What does the theorem predict for an explicit three-level source? | [Qutrit example and certified calculations](qutrit_example.md) |

## Attribution and verification

The [primary source locators](theorem_source_locators.md) identify the Schur, tableau and concentration results used in the proof. The [related-work account](../references/RELATED_WORK.md) compares the operational models and credits the established fluctuation-state description and classical stabilizer mechanism.

The [verification route](../verification/README.md) reconstructs the finite-size values and the limiting-work enclosure with exact arithmetic, supplemented by independent low-dimensional tensor-space projector identities. Numerical agreement supports the example; the preceding analytical pages establish the arbitrary fixed dimension and source result.

Every conclusion retains the fixed strict spectrum, closed cyclic work criterion and exact unitary symmetry of the [model](model_and_main_theorem.md). The oscillator limit is a mathematical spectral representation, with no added physical bath or work source.
