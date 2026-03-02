Step-by-Step Deployment Process

1. Launch EC2 Instance

- Selected Ubuntu 24.04
- Created key pair (.pem)
- Allowed SSH (port 22)
- Later opened port 8000 for FastAPI

2. Connect via SSH
```
ssh -i your-key.pem ubuntu@YOUR_PUBLIC_IP
```

3. Install Required Python Tools

Ubuntu 24 uses PEP 668 (externally managed environment), so system-wide pip installs are restricted.

Installed required packages:
```
sudo apt update
sudo apt install -y python3-pip
sudo apt install -y python3-venv
```

4. Create Virtual Environment
```
mkdir fastapi_project
cd fastapi_project
python3 -m venv venv
source venv/bin/activate
```

Why?
Ubuntu 24 prevents modifying system Python packages. A virtual environment is required for safe dependency management.

5. Install FastAPI and Uvicorn
Inside the activated virtual environment:

```
pip install --upgrade pip
pip install fastapi uvicorn
```

6. Run the API Server
```
uvicorn main:app --host 0.0.0.0 --port 8000
```

7. Configure AWS Security Group
Added inbound rule:

- Type: Custom TCP
- Port: 8000
- Source: My IP (for safety)

8. Run Server in Background Using Screen
```
sudo apt install screen -y
```
```
screen -S fastapi
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000
```
```
Ctrl + A, then D
```
```
screen -r fastapi
```

Problems Encountered & Lessons Learned
PEP 668 – Externally Managed Environment
Error:
```
externally-managed-environment
```

Solution:

- Do NOT install packages system-wide
- Use python3 -m venv
- Install dependencies inside virtual environment