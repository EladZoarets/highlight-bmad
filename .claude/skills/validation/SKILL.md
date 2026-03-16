---
name: validation
description: Validate implementation behavior against intended logic.
user-invocable: false
---

# Use this skill when:
- checking correctness of results
- verifying scoring calculations
- verifying sorting and ranking
- reviewing edge cases
- confirming alignment with requirements

# Implementation Requirements:
- compare expected and actual behavior
- check scoring rule compliance
- verify sorting logic
- identify concrete issues only
- avoid unnecessary redesign

# Output Format:
- validation summary
- expected behavior
- observed behavior
- mismatches if any
- concrete fixes

# What this is NOT:
- not writing new implementation
- not redefining the architecture
- not root-cause analysis
- not feature expansion