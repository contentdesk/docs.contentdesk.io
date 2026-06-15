---
tags:
  - property
hide:
  - navigation
---

# isRelatedTo
[https://schema.org/isRelatedTo](https://schema.org/isRelatedTo)

Hinweis auf ein anderes oder verwandtes Produkt.

## Graph

``` mermaid
graph TB
  Product --> |isRelatedTo| Product
  Product --> |isRelatedTo| Offer("Offer(Product)")
```

### Beispiel

``` mermaid
graph TB
  Product("Gästekarte "Community Pass"") --> |isRelatedTo| Offer1("Erwachsene 15.-")
  Product --> |offers| Offer2("Jugenliche 10.-")
  Product --> |offers| Offer3("Kinder 5.-")
```