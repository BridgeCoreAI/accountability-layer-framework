# BridgeCore AI Accountability Layer Framework v4.0

*A companion to the Execution Governance Model*

BridgeCore AI LLC — Governance Systems Engineering Lab (GSEL)

---

## Section 1 — Purpose and Relationship to v3.0

### 1.1 The Gap v3.0 Does Not Close

The Execution Governance Model v3.0 answers a narrow and specific question: does the system enforce what it claims to enforce, at the moment of execution. Complete Mediation, Deterministic Adjudication, Bounded Fail-Closed Evaluation, Escalation Integrity, Binding Consistency, and Evidence Continuity are verified guarantees about runtime behavior. They are formally specified. They are adversarially tested. They hold.

But a runtime guarantee is not an organizational guarantee. G4 — Escalation Integrity — guarantees that when the system cannot resolve a decision on its own, it surfaces that decision to a named authority rather than defaulting silently in either direction. What G4 cannot guarantee is what happens next. It cannot guarantee that the named authority exists in any meaningful sense. It cannot guarantee that the person receiving the escalation has what they need to decide well. It cannot guarantee that the decision holds when it is inconvenient, expensive, or politically costly to hold. And it cannot guarantee that the organization learns anything when the decision is made badly.

That is the gap v4.0 closes. The enforcement layer closes the execution gap — the space between what a policy says and what a system actually does. The accountability layer closes the organizational gap — the space between a decision being surfaced and a decision being owned.

### 1.2 Two Layers, Two Failure Modes

Each layer exists because the other layer's failure mode is different, and neither substitutes for the other.

A technical enforcement failure looks like this: the system silently defaults to Execute when it should have escalated, or evaluates a permission check inconsistently across two code paths, or loses the evidence trail linking a decision to its outcome. v3.0 exists to make these failures structurally impossible, not merely unlikely.

An accountability failure looks different. The system does exactly what it should — it surfaces the decision, it identifies that a human must decide, it waits. And then the decision goes to someone who was never told they held that authority. Or it goes to the right person, but arrives with no risk assessment and no deadline, so it sits. Or it arrives complete and on time, and the person approves it anyway because escalating further felt like it would slow down a launch, and there was no organizational cost to being wrong quietly. The system held. The organization did not.

v3.0 cannot detect or prevent this second failure mode, because it is not a system failure. It is a governance failure that happens entirely inside human decision-making, after the system has already done its job correctly. This is precisely why v4.0 is necessary as a distinct layer rather than an extension of v3.0 — it governs a different actor, under a different set of pressures, with different failure signatures.

### 1.3 v4.0 Is a Companion, Not a Replacement

v4.0 does not modify, extend, or supersede any guarantee in the Runtime Assurance Layer. The six guarantees of v3.0 remain the complete and final specification of what the technical enforcement layer must do. v4.0 sits above that layer and answers a separate question: once the enforcement layer has done its job and surfaced a decision, what organizational architecture ensures a human does their job in response.

This positioning is deliberate. Framing v4.0 as an extension of v3.0 would suggest that better technical enforcement could eventually absorb the accountability problem — that a sufficiently sophisticated system could guarantee good human decision-making the way it guarantees consistent policy evaluation. It cannot, and treating the two as convergent would misrepresent what each layer is capable of. v3.0 makes bad system behavior structurally impossible. v4.0 makes bad organizational behavior structurally costly — visible, attributable, and reviewable — but it cannot make it impossible, because it is governing people, not code.

### 1.4 What v4.0 Specifies

The remainder of this document specifies the accountability architecture as a system with four load-bearing components, corresponding to Sections 2 through 6:

- **Named Authority Registration** (Section 2) — who owns a surfaced decision, and how ownership is tiered and formally accepted rather than assumed.
- **The Escalation Information Package** (Section 3) — the six elements that must accompany every escalation reaching a named authority, so that "the decision was surfaced" and "the decision was decidable" are not treated as the same thing.
- **What Holds Under Pressure** (Section 4) — the organizational design requirements that keep Escalate the path of least resistance when Execute is faster and Refuse is safer.
- **Adversarial Escalation Scenario** (Section 5) — a documented case demonstrating the framework holding under exactly the conditions most likely to break it.
- **When Accountability Fails** (Section 6) — the post-incident structure that converts a failure of this layer into organizational learning rather than a repeated failure.

### 1.5 Relationship to v1.0

This specification formalizes and extends the BridgeCore AI Accountability Layer Framework v1.0 (github.com/BridgeCoreAI/accountability-layer-framework). v1.0 established the foundational principles — Named Ownership, Escalation Clarity, Enforced Follow-Through, and the Closure Standard — as organizational commitments. v4.0 takes each of those principles and specifies them to the same standard of rigor already applied to the enforcement layer: named, tiered, evidenced, and reviewable. Where v1.0 states a principle, v4.0 specifies the mechanism that makes the principle hold.

---

*Governance is not what is defined. It is what is enforced at execution.*
