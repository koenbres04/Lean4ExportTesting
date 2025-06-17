prelude

inductive MyList (T) where
| empty : MyList T
| add : T → MyList T → (MyList T)
