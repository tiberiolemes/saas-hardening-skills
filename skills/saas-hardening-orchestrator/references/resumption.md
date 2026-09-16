# Safe resumption

When a run is interrupted:

1. Read docs/audit/AUDIT-STATUS.md and the current stage report.
2. Re-run the Git preflight and compare the current commit and working tree with the last checkpoint.
3. Identify changes made after the checkpoint, including changes made by another person or agent.
4. Revalidate any finding, test, or gate that depends on the changed surface.
5. Re-check blockers and decision ownership; do not silently reinterpret an unresolved blocker as fixed.
6. Continue at the earliest incomplete stage. A later report cannot substitute for an earlier missing gate.
7. Update the checkpoint before further mutations.

If audit artifacts are missing or contradictory, mark the affected stage NOT_VERIFIED and reconstruct evidence before continuing.
