---
name: chaos-testing
description: Stress-test the solution using adversarial scenarios and zero-trust validation.
user-invocable: false
---

# Use this skill when:
- validating behavior under adversarial or ambiguous input
- challenging assumptions in the scoring logic
- testing whether outputs are trustworthy
- exposing fragile or accidental correctness
- applying zero-trust thinking

# Implementation Requirements:
- focus on assumption breaking
- test edge cases and adversarial inputs
- identify where behavior is fragile or misleading
- explain why the output should or should not be trusted
- propose the smallest correction if a weakness is found

# Output Format:
- challenged assumption
- adversarial scenario
- observed behavior
- weakness or risk
- minimal recommendation

# What this is NOT:
- not a normal code review
- not feature redesign
- not implementation generation
- not standard root-cause analysis after a bug