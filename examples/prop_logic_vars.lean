/-
Propositional logic examples, but now with variables!
-/

variable {p q r : Prop}

def exmpl1 : (p → q → r) → ((p ∧ q) → r) :=
  λ f ↦ λ h ↦ f h.left h.right

def exmpl2 : (p → q → r) → ((p ∧ q) → r) := by
  intro f
  intro h
  apply f
  exact h.left
  exact h.right

theorem exmpl3 : ¬p → ¬ q → ¬ (p ∨ q) :=
  λ h1 ↦ λ h2 ↦ λ h ↦ Or.elim h (λ a ↦ h1 a) (λ b ↦ h2 b)

theorem exmpl4 : ¬p → ¬ q → ¬ (p ∨ q) := by {
  intro h1
  intro h2
  intro h
  rcases h with a | b
  exact h1 a
  exact h2 b
}
