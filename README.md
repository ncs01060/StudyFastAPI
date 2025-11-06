## 가상환경

```bash
python3 -m venv pythonDiscordVenv
source pythonWebVenv/bin/activate

# 가상환경 나가기

deactivate
```

## 실행

```python
python3 -m uvicorn main:app --reload --port 5050
```
