# Maintenance Log

## 2026-04-30

### Issue #1: Incorrect discount logic in calculate_discount function

- **Issue ID:** #1
- **Repository:** s0l0l0b0/demo-agent-project
- **Status:** Fixed

**Root Cause:**
The `calculate_discount` function was incorrectly applying a 50% discount to the unit price (`price * 0.5 * quantity`) instead of applying a 10% discount to the total price (`total * 0.9`).

**Business Logic:**
The function should apply a 10% discount (pay 90%) when the total price exceeds $1000.

**Fix Applied:**
Changed:
```python
# Before (buggy):
return (price * 0.5) * quantity

# After (fixed):
return total * 0.9
```

**PR Link:** https://github.com/s0l0l0b0/demo-agent-project/pull/2