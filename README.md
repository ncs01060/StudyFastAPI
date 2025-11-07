연습용으로 게시판을 만들어 본 프로젝트입니다.

## 가상환경

```bash
python3 -m venv pythonFastAPIVenv
source pythonWebVenv/bin/activate

# 가상환경 나가기

deactivate
```

## 실행

```python
python3 -m uvicorn main:app --reload --port 5050
```
