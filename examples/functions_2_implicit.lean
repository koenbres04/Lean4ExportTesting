prelude

def comp : {A : Type} → {B : Type} → {C : Type} → (f : A → B) → (g : B → C) → (A → C) :=
   λ {A} ↦ λ {B} ↦ λ {C} ↦ λ f ↦ λ g ↦ λ a ↦ (g (f a))

def example_application (A : Type) (f : A → A) : A → A := comp f f
