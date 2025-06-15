theorem exmpl1 : (p : Prop) → (q : Prop) → (r : Prop) → (p → q → r) → ((p ∧ q) → r) :=
  λ p ↦ λ q ↦ λ r ↦ λ f ↦ λ h ↦ f h.left h.right

theorem exmpl2 : (p : Prop) → (q : Prop) → ¬p → ¬ q → ¬ (p ∨ q) :=
  λ p ↦ λ q ↦ λ h1 ↦ λ h2 ↦ λ h ↦ Or.rec h1 h2 h
