# LLM App TDD(Test Driven Development) Template / Usecase

## 250323

- pytest module로 작성할 때
	- .vscode/settings.json에 다음과 같이 작성한다. (.venv 쓰는 경우 / Windows 기준)
	```json
	{
	    //Python settings
	    "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe",
	    "python.envFile": "${workspaceFolder}/.env",
	
	    //Test settings
	    "python.testing.cwd": "${workspaceFolder}/tests",
	    "python.testing.pytestEnabled": true,
	    "python.testing.pytestArgs": ["tests"]
	}
	```
	- test 명령어는 `pytest tests` (tests는 폴더 이름)
	- tests가 다른 Module 인식하기 위해서는 tests 내부에 `__init__.py` 있어야 함!
	- method 이름에 항상 `test_` 필요
	- request module test 시에는 @patch(경로)
- LangChain 이용할 경우에 API docs 잘 읽어보면서 `FakeListChatModel`, `FakeChatModel` 이용

LLM App 개발에 TDD를 위한 초석

---

TODO
- Tools 어떻게 이용할 지 작성 - 사용해보면서 test 확장
- FastAPI 경우에도 등록
