run_docker:
	docker-compose up -d

run_fastapi:
	uvicorn main:app --reload