---
tags:
  - property
  - association type
  - attribute
hide:
  - navigation
---

# offers

Attribute and association type

## Schema.org
https://schema.org/offers

Inverse-property: [itemOffered](itemOffered)


## Graph

``` mermaid
graph TB
  Product --> |offers| Offer
```

### Beispiel

``` mermaid
graph TB
  Product("Eintritt Museum") --> |offers| Offer1("Erwachsene 15.-")
  Product --> |offers| Offer2("Jugenliche 10.-")
  Product --> |offers| Offer3("Kinder 5.-")
```