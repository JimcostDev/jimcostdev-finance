# JimcostDev Finance

JimcostDev Finance es un proyecto personal desarrollado para gestionar y administrar mis finanzas personales. Está construido usando Django y PostgreSQL, aprovechando el sistema de administración de Django para gestionar usuarios y autenticación. Además, utiliza Django REST Framework para proporcionar una API completa.

## Características

- **Gestión de ingresos**: Registro de los ingresos mensuales, clasificados por categorías.
- **Gestión de gastos**: Registro de los gastos mensuales, clasificados por categorías.
- **Reportes financieros**: Generación de reportes personalizados con cálculos de ingresos netos, gastos totales, contribuciones a la iglesia (diezmos y ofrendas), y balance mensual.
- **Sistema de usuarios**: Cada usuario puede gestionar sus propias finanzas de forma privada.

## Tecnologías Utilizadas

- **Backend**: Django 5.1 con Django REST Framework
- **Base de Datos**: PostgreSQL
- **Autenticación**: Sistema de auth integrado de Django
- **Documentación de la API**: DRF Spectacular

## Instalación

1. Clona este repositorio:
   ```bash
   git clone  https://github.com/JimcostDev/jimcostdev-finance.git
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura la base de datos PostgreSQL creando un archivo `.env` con la cadena de conexión adecuada. Ejemplo:
   ```env
   DATABASE_URL=postgres://usuario:contraseña@localhost:5432/nombre_base_datos
   ```

5. Aplica las migraciones:
   ```bash
   python manage.py migrate
   ```

6. Crea un superusuario:
   ```bash
   python manage.py createsuperuser
   ```

7. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

8. Accede a la aplicación en tu navegador: [http://localhost:8000](http://localhost:8000)

## Uso

- Registra tus ingresos y gastos a través de los endpoints de la API o el panel de administración de Django.
- Genera reportes mensuales accediendo a la ruta `/api/reports/` con los parámetros `start_date` y `end_date`.

## API Endpoints

- **CRUD de ingresos**: `/api/incomes/`
- **CRUD de gastos**: `/api/expenses/`
- **Reportes**: `/api/reports/` (GET con parámetros `start_date` y `end_date`)

## Ejemplo de Reporte

Solicitud:
```bash
GET /api/reports/?start_date=2024-12-01&end_date=2024-12-31
```

Respuesta:
```json
{
    "start_date": "2024-12-01",
    "end_date": "2024-12-31",
    "total_income": 80.0,
    "total_expenses": 30.0,
    "tithe": 8.0,
    "offering": 3.2,
    "church_contribution": 11.2,
    "net_income": 68.8,
    "final_balance": 38.8
}
```
¡Gracias por usar JimcostDev Finance! 😊
