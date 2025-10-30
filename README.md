``` markdown
MIGX - Full Stack Application

A full-stack application with FastAPI backend, MongoDB database, and Vue.js (Vite) frontend.

## 🚀 Quick Start with Docker

### Prerequisites
- Docker
- Docker Compose

### Running the Application

The application can be run in two modes: **Production** and **Development**.

---

## 📦 Production Mode

Production mode builds optimized versions of the application with Nginx serving the frontend.

### Start All Services
```

bash
Build and start all services
docker-compose up --build
Run in detached mode (background)
docker-compose up --build -d``` 

### View Logs
```

bash
View all service logs
docker-compose logs -f
View logs since last 100 lines
docker-compose logs -f --tail=100
View logs with timestamps
docker-compose logs -f -t``` 

### Stop Services
```

bash
Stop all services (keeps containers)
docker-compose stop
Stop and remove containers
docker-compose down
Stop and remove containers + volumes (⚠️ deletes database data)
docker-compose down -v
Stop and remove containers + volumes + images
docker-compose down -v --rmi all``` 

---

## 🔧 Individual Service Management

### Rebuild Specific Service
```

bash
Rebuild and restart backend only
docker-compose up --build backend
Rebuild and restart frontend only
docker-compose up --build frontend
Rebuild and restart mongodb only
docker-compose up --build mongodb``` 

### Start/Stop Specific Service
```

bash
Start specific service
docker-compose start backend docker-compose start frontend docker-compose start mongodb
Stop specific service
docker-compose stop backend docker-compose stop frontend docker-compose stop mongodb
Restart specific service
docker-compose restart backend docker-compose restart frontend docker-compose restart mongodb``` 

### View Logs for Specific Service
```

bash
View MongoDB logs
docker-compose logs -f mongodb
View backend logs
docker-compose logs -f backend
View frontend logs
docker-compose logs -f frontend
View logs with tail
docker-compose logs -f --tail=50 backend``` 

### Execute Commands in Running Container
```

bash
Access backend container shell
docker-compose exec backend bash
Access MongoDB shell
docker-compose exec mongodb mongosh
Access MongoDB with authentication
docker-compose exec mongodb mongosh -u admin -p admin123
Run Python commands in backend
docker-compose exec backend python -c "print('Hello')"
Install additional Python packages
docker-compose exec backend pip install <package-name>
Access frontend container (production)
docker-compose exec frontend sh``` 

### Check Service Status
```

bash
List all running containers
docker-compose ps
Check service health
docker-compose ps mongodb
View container resource usage
docker stats``` 

---

## 🛠️ Development Mode

Development mode provides hot-reload for both frontend and backend.
```

bash
Start development environment
docker-compose -f docker-compose.dev.yml up
In detached mode
docker-compose -f docker-compose.dev.yml up -d
Stop development environment
docker-compose -f docker-compose.dev.yml down``` 

---

## 🌐 Access Points

### Production Mode
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **API ReDoc**: http://localhost:8000/redoc
- **MongoDB**: localhost:27017

### Development Mode
- **Frontend (Vite Dev Server)**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **MongoDB**: localhost:27017

---

## 🗄️ Database Management

### MongoDB Connection

**Connection String:**
```

mongodb://admin:admin123@localhost:27017/migx?authSource=admin``` 

### MongoDB Commands
```

bash
Connect to MongoDB shell
docker-compose exec mongodb mongosh -u admin -p admin123
Backup database
docker-compose exec mongodb mongodump --username admin --password admin123 --authenticationDatabase admin --db migx --out /data/backup
Restore database
docker-compose exec mongodb mongorestore --username admin --password admin123 --authenticationDatabase admin --db migx /data/backup/migx
Export collection to JSON
docker-compose exec mongodb mongoexport --username admin --password admin123 --authenticationDatabase admin --db migx --collection <collection_name> --out /data/export.json
Import collection from JSON
docker-compose exec mongodb mongoimport --username admin --password admin123 --authenticationDatabase admin --db migx --collection <collection_name> --file /data/import.json``` 

---

## 🔍 Troubleshooting

### View Container Details
```

bash
Inspect container
docker-compose exec backend env
Check container networking
docker network ls docker network inspect migx_migx-network
View volume details
docker volume ls docker volume inspect migx_mongodb_data``` 

### Clear Everything and Start Fresh
```

bash
Stop all services and remove everything
docker-compose down -v
Remove all unused images
docker image prune -a
Remove all unused volumes
docker volume prune
Start fresh
docker-compose up --build``` 

### Common Issues

**Port Already in Use:**
```

bash
Check what's using the port
lsof -i :8000 lsof -i :3000 lsof -i :27017
Kill the process or change ports in .env file``` 

**Permission Issues:**
```

bash
Fix volume permissions
sudo chown -R USER:USER .``` 

**Container Won't Start:**
```

bash
Check logs for errors
docker-compose logs backend
Check container status
docker-compose ps
Remove and rebuild
docker-compose rm backend docker-compose up --build backend``` 

---

## 📝 Environment Variables

Configure the application by editing the `.env` file:
```

bash
MongoDB Configuration
MONGO_ROOT_USERNAME=admin MONGO_ROOT_PASSWORD=admin123 MONGO_DATABASE=migx MONGO_PORT=27017
Backend Configuration
BACKEND_PORT=8000
Frontend Configuration
FRONTEND_PORT=3000
API URL for frontend
VITE_API_URL=http://localhost:8000``` 

---

## 🧹 Maintenance Commands

### Clean Up

```bash
# Remove stopped containers
docker-compose rm

# Prune unused images
docker image prune

# Prune unused volumes (⚠️ careful with data)
docker volume prune

# Clean everything (⚠️ nuclear option)
docker system prune -a --volumes
```
```

Update Images``` bash
# Pull latest base images
docker-compose pull

# Rebuild with latest images
docker-compose up --build --force-recreate
```

 
📚 Tech Stack
Backend: Python 3.11.7 + FastAPI
Database: MongoDB 7.0
Frontend: Vue.js 3.5.22 + Vite + TypeScript
Styling: TailwindCSS 4.1.16 + PrimeVue 4.4.1
State Management: Pinia 3.0.3