# Beershop

**Tres amigos** entran a un bar donde solo venden cerveza. El lugar ofrece **promociones esporádicas**.

1. **Implementa un endpoint en python para obtener el estado de la orden***. Ganas puntos extra si:
   - Sigues convenciones
   - Agregas tests
   - Implementas capas, a nosotros nos gusta la arquitectura limpia
   - Usas Django o FastAPI en el backend

2. **Implementa una interfaz de usuario con ReactJS que muestra la información de la orden**. Ganas puntos extra si:
    - Sigues convenciones
    - Agregas tests
    - Usas typescript
    - Usas NextJS
    - Usas tailwind para estilos
> En la visualización de las órdenes se prefiere ver también las rondas o un subtotal por cerveza? Esta bien mostrar solo el subtotal

3. Sube tu código en un repositorio en un proyecto en Github y compartelo con nosotros.
4. Incluye un README con instrucciones para ejecutar el código.

**No uses una base de datos, es suficiente con mantener la información en memoria**. Te sugerimos esta estructura de datos:

## Stock
stock: Esta estructura tiene los datos
```json
{
    "last_updated": "2024-09-10 12:00:00",
    "beers": [
        {
            "name": "Corona",
            "price": 115,
            "quantity": 2
        },
        {
            "name": "Quilmes",
            "price": 120,
            "quantity": 0
        },
        {
            "name": "Club Colombia",
            "price": 110,
            "quantity": 3
        }
    ]
}
```

## Order
*order: Esta estructura incluye la cuenta de lo ordenado hasta ahora y te permite saber lo que vas a pagar.
```json
{
    "created": "2024-09-10 12:00:00",
    "paid": false,
    "subtotal": 0,
    "taxes": 0,
    "discounts": 0,
    "items": [],
    "rounds": [
        {
            "created":  "2024-09-10 12:00:30",
            "items": [
                {
                    "name": "Corona",
                    "quantity": 2
                },
                {
                    "name": "Club Colombia",
                    "quantity": 1
                }
            ]
        },
        {
            "created":  "2024-09-10 12:20:31",
            "items": [
                {
                    "name": "Club Colombia",
                    "quantity": 1
                },
                {
                    "name": "Quilmes",
                    "quantity": 2
                }
            ]
        },
        {
            "created":  "2024-09-10 12:43:21",
            "items": [
                {
                    "name": "Quilmes",
                    "quantity": 3
                }
            ]
        }
    ]
}
```

## Item
item: esta estructura representa las cervezas pedidas dentro de una orden

```json
{
        "name": "Quilmes",
        "price_per_unit": 0,
        "total": 0
}
```

> El total hace referencia a la cantidad. El único valor calculado es el precio total de la orden.