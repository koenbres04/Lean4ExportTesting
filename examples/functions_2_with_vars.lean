prelude

def comp {A B C : Type} (f : A → B) (g : B → C) : A → C := λ a ↦ g (f a)

def example_application (A : Type) (f : A → A) : A → A := comp f f
