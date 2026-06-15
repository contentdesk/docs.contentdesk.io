---
tags:
  - concept
hide:
  - navigation
---

# Produkte, Varianten und Angebote


## Übersicht von Möglichkeiten

- Einfaches Produkt [Product]

    * ohne weitere Angebote
    * mit weiteren Angeboten - via Verknüpfung [offers]

- Produkt mit Variante [ProductGroup]

    * nach Farbe [color]
    * nach Material [material]
    * etc.

- Angebot [Offer]

    * Ein zusätzliches Angebot, das nur in Kombination mit dem ersten Basisangebot erhältlich ist (z.B. Zuschläge und Verlängerungen, die gegen einen Aufpreis erhältlich sind). [addOn]

- Service [Service]

    * 

## Use-Case / Beispiele

### Produkt Tagespass mit Angeboten / Leistungen

Die Angebote / Leistungen sind von anderen Leistungsträgern

### Produkte / Dienstleistungen mit Varianten

* Marketing zum Mitmachen

## Contentdesk und Schema.org Typen

| Contentdesk       | Schema.org         | Bemerkung                              |
| -----------       | --------------     | ------------------------------------   |
| Product-Model / Variante    | ProductGroup       | Produkt Variante                       |
| Product           | Product            |                                        |
|                   | ProductModel?      | Für Ähnlich wie Product mit weiteren spezifischen Properties wie isVariantOf, predecessorOf,successorOf |
| Group             | ProductCollection? |                                        |


### Mapping
``` mermaid
flowchart LR
    subgraph Contentdesk.io
        direction TB
        ContentdeskProduct[Product] -->|offers| ContentdeskOffer[Offer]
        ContentdeskOffer -->|addOn| ContentdeskOffer
        ContentdeskOffer -->|itemOffered| ContentdeskProduct
        ContentdeskOffer -->|itemOffered| ContentdeskService[Service]
    end

    subgraph discover.swiss
        direction TB
        discoverProduct[Product] -->|offers| discoverOffer[Offer?]
        discoverOffer -->|addOn| discoverOffer
        discoverOffer -->|itemOffered| discoverProduct
        discoverOffer -->|itemOffered| discoverService[Service?]
    end

    Contentdesk.io --> discover.swiss
```




## Schema.org "Varianten"

### Schema
``` mermaid
flowchart TB
    Product -->|offers| Offer
    Offer-->|addOn| Offer
    Offer-->|itemOffered| Product
    Offer-->|itemOffered| Service
```

* Product / ProductModel
* Product with offers
* ProductGroup with Variant
* 
* Offer with addOn
* 

### isVariantOf / hasVariant
https://schema.org/isVariantOf

https://schema.org/hasVariant

### offers



## Offene Punkte 

* [Service]



## Übersicht Gesamt mit allen Verknüpfungen und Schemas
``` mermaid
graph TB
    subgraph Site
        direction TB
        Directory --> Product-Detail
        Teaser --> Product-Detail
        Link --> Product-Detail

        Product-Detail -->|"offers ✅👁️"| Offer-Detail
        Place-Detail --> |"makesOffer ✅👁️"| Offer-Detail
        Place-Detail --> |"?❌👁️"| Product-Detail
        subgraph New-Detail-Site
            direction TB
            Place-Detail("LocalBusiness")
        end
        subgraph Detail-Site
            direction TB
            Offer-Detail --> |"availableAtOrFrom ✅👁️"|Place-Detail
            Offer-Detail --> |"itemOffered ✅"| Product-Detail
        end
        
    end
    subgraph schema.org
        direction TD
        Product --> |"offers"| Offer
        Offer --> |"itemOffered"| Product
        Offer --> |"availableAtOrFrom ✅"| LocalBusiness
        Offer --> |"areaServed "| LocalBusiness
        LocalBusiness --> |"makesOffer ✅"| Offer
        Offer --> |"offeredBy ✅"| LocalBusiness
        LocalBusiness --> |"hasPOS"| Place
        LocalBusiness --> |"location"| Place
        LocalBusiness --> |"areaServed"| Place
        LocalBusiness --> |"owner"| Organization
        LocalBusiness --> |"hasOfferCatalog"| OfferCatalog
    end

    subgraph discover.swiss
        direction TB
        GuestCard["GuestCard (Product)"] -->|isRelatedTo| OfferDS["Offer(Product)"]
        OfferDS -->|itemOffered| ProductDS["Produkt / Service (Product)"]
        OfferDS -->|areaServed| LocalBusinessDS["POI (LocalBusiness)"]
        ProductDS -->|areaServed| LocalBusinessDS
    end

```

[Mermaid Live Editor](https://mermaid.ai/live/edit#pako:eNqVlF2vmjAYx78K6dWWqAdERbjYMg_ZsuQkmmnOxcYuKn2ERqCmLW4e9Zvtbl9spVVhDufGVfvw_z3vsEcxI4AClHC8Sa3FJCos9YhyaQxzKsGYqiekHGLJ-M7qdt9YM85IGctuCBLTTJumqxXwk6HGFoAF8BamljzRYv1XwSzDMdwP9Yfslr8mboQN0sigIFfdEHEKOe4xntSOiO4JZYW1CBt5mLDa8yFCrIomInQwca_SOKtUr3NtAFJJTz5uiPFWJYqXGbyTU_6es9x6sJ6Br37-SJaYa76q6BbNAc-Bb4Eo7ImCerVUcWmctpD6eibfWvfKYKaEyU4LeYIL-oKrDjX0DesZy_EahPHbEqAFSLGYTedtlbaIMxabHP5NXvenBWisx9WCECpitgXeE9-oEK1LMqmtH0oQ8hFz8iVCl7P16jT31xH6WqVzoOITZFgCWbBTX8K5IvSpKb4aRzg3dL1Ul5XSvD6vpZp_VShVE77vrG7LqSnG0_SjYqvr7-Ql2n-yurOoo_5JlKBA8hI6KAee4-qK9pUoQlJ9ihChQB0JrHCZyQhFxVFhG1x8Ziw_k5yVSYqCFc6EupUboloZUqwGll-sXIUE_sjKQqLAGY097QUFe_Rd3XuDgd_3fW846Nue6zpOB-1Q4Lq94cj1-o7t-o4_Hg-PHfSi4zo9u287nmfbI_V64I9Gx18ofarM)


### Links / Verknüpfungen

* [offers](../../schemaArchiv/offers)
* [itemOffered](../../schemaArchiv/itemOffered)
* [availableAtOrFrom](../../schemaArchiv/availableAtOrFrom)
* [makesOffer](../../schemaArchiv/makesOffer)

#### weiter offene Verknüpfungen

* [hasOfferCatalog](../../schemaArchiv/hasOfferCatalog)
* [areaServed](../../schemaArchiv/areaServed)
* [offeredBy](../../schemaArchiv/offeredBy)
* [seller](../../schemaArchiv/seller)
* [hasPOS](../../schemaArchiv/hasPOS)
* [location](../../schemaArchiv/location)
* [owner](../../schemaArchiv/owner)