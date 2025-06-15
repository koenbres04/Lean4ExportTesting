variable (p q r : Prop)

theorem exmpl1 : (p → q → r) → ((p ∧ q) → r) := by
  intro f
  intro h
  apply f
  exact h.left
  exact h.right

theorem exmpl2 : ¬p → ¬ q → ¬ (p ∨ q) := by {
  intro h1
  intro h2
  intro h
  rcases h with a | b
  exact h1 a
  exact h2 b
}
