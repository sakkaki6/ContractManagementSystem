# Contract Management System

A comprehensive contract management system with advanced features for drafting, approving, tracking, and managing contracts.

## Features

- **User Management & Authentication:** Role-based access control, OAuth2 with JWT, MFA support
- **Contract Drafting & Storage:** Rich-text editor, templates, versioning, full-text search
- **Approval Workflow:** Multi-step approvals, e-signature integration, notifications
- **Lifecycle Tracking:** Renewals, expirations, automated reminders
- **Collaboration & Communication:** Commenting, internal messaging, real-time updates
- **Reporting & Analytics:** Contract status tracking, exportable reports, compliance monitoring
- **Integrations:** ERP/CRM, cloud storage, external API support

## Tech Stack

### Frontend

- Vue.js 3 with Composition API
- Vite for fast development
- PrimeVue/Vuetify for UI components
- Pinia for state management
- Tailwind CSS for styling
- WebSockets for real-time updates

### Backend

- FastAPI for high-performance API
- PostgreSQL for database
- SQLAlchemy for ORM
- Pydantic for data validation
- OAuth2 with JWT for authentication
- Celery + Redis for background tasks

### Deployment

- Docker for containerization
- AWS (EC2/Lambda, S3, CloudFront) for cloud deployment
- CI/CD with GitHub Actions/GitLab CI/CD

### Monitoring

- Prometheus + Grafana for metrics
- ELK Stack for logging

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 16+
- PostgreSQL 13+
- Redis 6+

### Backend Setup

1. Navigate to the backend directory:

   ```
   cd backend
   ```

2. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   ```
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Run migrations:

   ```
   alembic upgrade head
   ```

6. Start the backend server:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```
   cd frontend
   ```

2. Install dependencies:

   ```
   npm install
   ```

3. Start the development server:
   ```
   npm run dev
   ```

## Project Structure

```
ContractManagementSystem/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── utils/
│   ├── tests/
│   ├── .env
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── composables/
│   │   ├── layouts/
│   │   ├── router/
│   │   ├── stores/
│   │   ├── views/
│   │   └── App.vue
│   ├── .env
│   └── package.json
├── docker/
│   ├── backend/
│   ├── frontend/
│   └── docker-compose.yml
└── docs/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
