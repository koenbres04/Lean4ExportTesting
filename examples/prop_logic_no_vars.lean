/-
Propositional logic examples.
-/



def exmpl1 : (p : Prop) → (q : Prop) → (r : Prop) → (p → q → r) → ((p ∧ q) → r) :=
  λ p ↦ λ q ↦ λ r ↦ λ f ↦ λ h ↦ f h.left h.right

def exmpl2 : (p : Prop) → (q : Prop) → (r : Prop) → (p → q → r) → ((p ∧ q) → r) := by
  intro p
  intro q
  intro r
  intro f
  intro h
  apply f
  exact h.left
  exact h.right

theorem exmpl3 : (p : Prop) → (q : Prop) → ¬p → ¬ q → ¬ (p ∨ q) :=
  λ p ↦ λ q ↦ λ h1 ↦ λ h2 ↦ λ h ↦ Or.elim h (λ a ↦ h1 a) (λ b ↦ h2 b)

theorem exmpl4 : (p : Prop) → (q : Prop) → ¬p → ¬ q → ¬ (p ∨ q) := by {
  intro p
  intro q
  intro h1
  intro h2
  intro h
  rcases h with a | b
  exact h1 a
  exact h2 b
}
