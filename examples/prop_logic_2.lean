theorem exmpl1 : (p : Prop) → (q : Prop) → (r : Prop) → (p → q → r) → ((p ∧ q) → r) := by
  intro p
  intro q
  intro r
  intro f
  intro h
  apply f
  exact h.left
  exact h.right

theorem exmpl2 : (p : Prop) → (q : Prop) → ¬p → ¬ q → ¬ (p ∨ q) := by
  intro p
  intro q
  intro h1
  intro h2
  intro h
  rcases h with a | b
  exact h1 a
  exact h2 b
