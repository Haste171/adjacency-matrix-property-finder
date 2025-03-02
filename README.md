# Adjacency Matrix Property Finder

![Example](image.png)

# Relations in Matrix Representation

## Self-Loop
A **self-loop** is defined in a matrix by an element \( x \) pointing to itself.

Example:
```
    a  b
  ┌──────┐
a │ 1  0 │
b │ 0  1 │
  └──────┘
```
Here, both `a` and `b` have self-loops.

## Reflexive Relation
A relation is **reflexive** if every element in the relation has a self-loop.

- **Condition:** \( G^x \) for all \( x \) in the relation.

## Anti-Reflexive Relation
A relation is **anti-reflexive** if every element in the relation **does not** have a self-loop.

- **Condition:** No element in the relation has \( G^x \).

## Symmetric Relation
A relation is **symmetric** if, whenever \( x \) points to \( y \), \( y \) also points to \( x \).

Example:
```
    a  b
  ┌──────┐
a │ 0  1 │
b │ 1  0 │
  └──────┘
```
This represents \( a \leftrightarrow b \).

### Important Note:
Elements that **do not point to anything** and **are not pointed to by anything** are **ignored** when assessing symmetry.

## Anti-Symmetric Relation
A relation is **anti-symmetric** if, whenever \( x \) points to \( y \), \( y \) **does not** point to \( x \), except in the case of self-loops.

Example:
```
    a  b
  ┌──────┐
a │ 0  1 │
b │ 0  0 │
  └──────┘
```
This represents \( a \to b \), but **not** \( b \to a \).

## Transitive Relation
A relation is **transitive** if, whenever \( x \) points to \( y \) and \( y \) points to \( z \), then \( x \) must also point to \( z \).

Example:
```
x → y → z  ⟹  x → z
```
- If any part of the relation does **not** satisfy this property, then the relation is **not transitive**.