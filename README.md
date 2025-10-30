MIGX - Full Stack Application

A full-stack application with FastAPI backend, MongoDB database, and Vue.js (Vite) frontend.

## 📚 Tech Stack
 - Backend: Python 3.11.7 + FastAPI
 - Database: MongoDB 7.0
 - Frontend: Vue.js 3.5.22 + Vite + TypeScript
 - Styling: TailwindCSS 4.1.16 + PrimeVue 4.4.1 
 - State Management: Pinia 3.0.3

## 🚀 Quick Start with Docker

### Prerequisites
- Docker
- Docker Compose

---
### Running the Application

```sh
docker-compose up --build
```
#### Access the application
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- MongoDB: localhost:27017

> #### View logs
> ```shell
> docker-compose logs -f
> ```
> Last 100 logs
> ```shell
> docker-compose logs -f --tail=100
> ```
> Timestamps
> ```shell
> docker-compose logs -f -t
> ``` 


> ### Stop Services
> Stop all services (keeps containers)
> ```shell
> docker-compose stop
> ```
> Stop and remove containers
> ```shell
> docker-compose down
> ```
> Stop and remove containers + volumes (⚠️ deletes database data)
> ```shell
> docker-compose down -v
> ```
> Stop and remove containers + volumes + images
> ```shell
> docker-compose down -v --rmi all
> ```