# Hosted mathematical verification

The read-only [workflow](../../.github/workflows/hosted-math.yml) checks the exact proposed source on GitHub at widths 1440 and 760 pixels. It first probes the repository overview, then compares every mathematical expression on all tracked Markdown pages with the pinned source. The capture includes accessible mathematical structure, HTML and screenshots; the contract also checks the headline work values and limiting formula.

The bundled [collector](capture_hosted_math.cjs), [checker](check_rendered_math.py) and [probe](probe_hosted_math.cjs) have Git blob identities `6f36ee03223a82d0075da2fe903f21bc5a45a75b`, `1d3bf9810d0dfadb844a48b354af80f9b66924bc` and `f83ea9da799bee0b53bd5c57315ae2b4b2d9de43`, respectively.

For a local run with Node 18 or later, Python 3.10 or later, Git, Playwright 1.56.1, MathJax 3.2.1 and its Chromium runtime available:

```bash
node verification/hosted_math/capture_hosted_math.cjs \
  --root . --repository GoGoKo699/Collective-Fluctuation-Work \
  --revision FULL_COMMIT_SHA \
  --contract verification/hosted_math/contract.json \
  --output /absolute/new-empty-evidence-directory
```

Replace the revision and output placeholders with the intended commit and a new empty directory. The command reads Git objects rather than dirty working files. The workflow grants only `contents: read`, uses no secrets and does not persist checkout credentials. Artifacts are retained for 14 days; they are diagnostic outputs rather than a permanent scientific record.

An automated structural pass does not establish legibility, scientific truth or correct interpretation. Screenshots need separate visual inspection, and the [scientific checks](../README.md) establish a different part of verification. A failed or unavailable capture remains a failed or unavailable check.
