prelude

axiom A : Type
axiom B : Type
axiom b : B

noncomputable def const_function : A → B := λ a ↦ b
